const API_BASE = 'http://127.0.0.1:8000';

const tabButtons = document.querySelectorAll('.tab-button');
const tabPanels = document.querySelectorAll('.tab-panel');
const analyzeButton = document.getElementById('analyzeButton');
const buttonText = document.querySelector('.button-text');
const spinner = document.querySelector('.spinner');
const reviewInput = document.getElementById('reviewInput');
const fileInput = document.getElementById('fileInput');
const fileLabel = document.getElementById('fileLabel');
const resultCard = document.getElementById('resultCard');
const errorCard = document.getElementById('errorCard');
const errorMessage = document.getElementById('errorMessage');
const predictionStatus = document.getElementById('predictionStatus');
const confidenceTextLarge = document.getElementById('confidenceTextLarge');
const reviewCountText = document.getElementById('reviewCountText');
const trustScoreText = document.getElementById('trustScoreText');
const reviewSamplesList = document.getElementById('reviewSamplesList');
const chartCanvas = document.getElementById('reviewChart');
const analysisTextDisplay = document.getElementById('analysisTextDisplay');
const loadingOverlay = document.getElementById('loadingOverlay');

let activeMode = 'text';
let reviewChart;

function initChart() {
  const data = {
    labels: ['Fake', 'Genuine'],
    datasets: [{
      data: [0, 100],
      backgroundColor: ['rgba(255, 91, 127, 0.9)', 'rgba(74, 248, 255, 0.88)'],
      borderWidth: 0,
    }],
  };

  reviewChart = new Chart(chartCanvas, {
    type: 'doughnut',
    data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { color: '#b0c1dc' } },
        tooltip: { callbacks: { label: (context) => `${context.label}: ${context.parsed}%` } },
      },
      cutout: '72%',
    },
  });
}

function setActiveTab(mode) {
  activeMode = mode;
  tabButtons.forEach((button) => {
    button.classList.toggle('active', button.dataset.mode === mode);
  });
  tabPanels.forEach((panel) => {
    panel.classList.toggle('active', panel.id === `${mode}Panel`);
  });
  resetResult();
}

function setLoading(isLoading) {
  analyzeButton.disabled = isLoading;
  if (isLoading) {
    buttonText.style.opacity = '0';
    spinner.classList.remove('hidden');
    loadingOverlay.classList.remove('hidden');
  } else {
    buttonText.style.opacity = '1';
    spinner.classList.add('hidden');
    loadingOverlay.classList.add('hidden');
  }
}

function showError(message) {
  errorMessage.textContent = message;
  errorCard.classList.remove('hidden');
  resultCard.classList.add('hidden');
}

function updateChart(fakePercent, genuinePercent) {
  if (!reviewChart) return;
  reviewChart.data.datasets[0].data = [fakePercent, genuinePercent];
  reviewChart.update();
}

function renderSampleReviews(sampleReviews = []) {
  reviewSamplesList.innerHTML = '';
  if (!sampleReviews.length) {
    reviewSamplesList.innerHTML = '<p class="hint">No sample predictions yet.</p>';
    return;
  }

  sampleReviews.slice(0, 4).forEach((sample) => {
    const item = document.createElement('div');
    item.className = 'review-sample';
    item.innerHTML = `
      <p>${sample.text}</p>
      <div class="sample-meta">
        <span class="tag">${sample.prediction.toUpperCase()}</span>
        <span class="tag">${sample.confidence.toFixed(1)}%</span>
      </div>
    `;
    reviewSamplesList.appendChild(item);
  });
}

function getModeLabel() {
  return activeMode === 'text' ? 'Text Review' : 'Screenshot OCR';
}

async function fetchJson(endpoint, options) {
  const response = await fetch(`${API_BASE}${endpoint}`, options);
  const data = await response.json().catch(() => ({ detail: 'Invalid server response' }));
  if (!response.ok) {
    throw new Error(data.detail || data.message || `Server returned ${response.status}`);
  }
  return data;
}

function readFileAsBase64(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = () => reject(new Error('Failed to read image file.'));
    reader.readAsDataURL(file);
  });
}

function getAnalysisSourceText(data) {
  if (data.review_text) return data.review_text;
  if (data.extracted_text) return data.extracted_text;
  if (data.url) return data.url;
  return 'Input was analyzed successfully. Review summary is shown above.';
}

async function analyzeActiveMode() {
  const payload = { mode: activeMode };

  if (activeMode === 'text') {
    const text = reviewInput.value.trim();
    if (!text) throw new Error('Please paste a review text before analyzing.');
    payload.review = text;
  } else if (activeMode === 'screenshot') {
    const file = fileInput.files[0];
    if (!file) throw new Error('Please upload a screenshot image before analyzing.');
    payload.image_base64 = await readFileAsBase64(file);
  }

  const data = await fetchJson('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  const fakePercentage = Number(data.fake_percentage ?? 0);
  const genuinePercentage = Number(data.review_count ? 100 - fakePercentage : 0);
  const confidence = Number(data.confidence ?? 0);
  const trustScore = Number(data.trust_score ?? 0);
  const reviewCount = Number(data.review_count ?? 1);
  const prediction = data.prediction || (fakePercentage > 50 ? 'fake' : 'genuine');
  const sampleReviews = data.sample_reviews || [];

  resultCard.classList.remove('hidden');
  resultCard.classList.remove('fake', 'genuine');
  resultCard.classList.remove('visible');
  void resultCard.offsetWidth;
  resultCard.classList.add('visible');
  errorCard.classList.add('hidden');
  predictionStatus.textContent = prediction === 'genuine' ? 'Genuine' : 'Fake';
  predictionStatus.style.color = prediction === 'genuine' ? '#7cffb3' : '#ff5b7f';
  confidenceTextLarge.textContent = `${confidence.toFixed(1)}%`;
  trustScoreText.textContent = `${trustScore.toFixed(1)}%`;
  reviewCountText.textContent = `${reviewCount}`;
  renderSampleReviews(sampleReviews);
  updateChart(fakePercentage, genuinePercentage);
  analysisTextDisplay.textContent = getAnalysisSourceText(data);
  resultCard.classList.add(prediction === 'genuine' ? 'genuine' : 'fake');
}

async function handleAnalyzeClick() {
  setLoading(true);
  try {
    await analyzeActiveMode();
  } catch (error) {
    showError(error.message || 'Unable to connect to the backend. Ensure FastAPI is running at http://127.0.0.1:8000');
  } finally {
    setLoading(false);
  }
}

function handleFileLabel() {
  const file = fileInput.files[0];
  fileLabel.textContent = file ? file.name : 'Choose screenshot image';
}

function init() {
  tabButtons.forEach((button) => {
    button.addEventListener('click', () => setActiveTab(button.dataset.mode));
  });

  analyzeButton.addEventListener('click', handleAnalyzeClick);
  fileInput.addEventListener('change', handleFileLabel);
  initChart();
  resetResult();
}

function resetResult() {
  errorCard.classList.add('hidden');
  resultCard.classList.add('hidden');
  resultCard.classList.remove('visible', 'fake', 'genuine');
  predictionStatus.textContent = 'Ready';
  predictionStatus.style.color = '#ffffff';
  confidenceTextLarge.textContent = '0%';
  reviewCountText.textContent = '0';
  trustScoreText.textContent = '0%';
  reviewSamplesList.innerHTML = '<p class="hint">Analysis summary and samples will appear here.</p>';
  analysisTextDisplay.textContent = 'Paste text or upload a screenshot to begin.';
  updateChart(0, 100);
}

init();
