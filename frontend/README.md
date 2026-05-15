# AI Review Detector Frontend

A futuristic cyberpunk-themed dashboard for the Fake Product Review Detector backend with neon UI, glassmorphism, and advanced animations.

## Features

- **Cyberpunk Neon UI**: Vibrant neon colors (cyan, pink, green, red) with glowing effects
- **Moving Gradient Background**: Animated shifting background gradients
- **Glassmorphism Cards**: Frosted glass effect with backdrop blur and transparency
- **Animated Glowing Borders**: Pulsing scan lines and glowing borders on cards
- **Prediction Meter**: Circular progress meter that fills based on confidence
- **Confidence Progress Bar**: Animated bar with shimmer effect showing prediction confidence
- **Color-Coded Results**: Green for genuine reviews, red for fake reviews
- **Animated Loading Spinner**: Cyberpunk-style spinner during analysis
- **Smooth Transitions**: Fluid animations throughout the interface
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Icons**: Font Awesome icons for visual enhancement
- **Real-time Stats**: Model accuracy and response time display

## Files

- `index.html`: Main dashboard with cyberpunk layout, prediction meter, and stats
- `styles.css`: Extensive CSS with cyberpunk theme, animations, and responsive design
- `script.js`: JavaScript handling API calls, meter updates, color changes, and animations

## Usage

1. Start the backend:

```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

2. Open `frontend/index.html` in your browser.
3. Enter a review and click `Analyze Review`.

The dashboard will display the analysis with animated meter, confidence bar, and color-coded results. The interface features cyberpunk aesthetics with smooth animations and glowing effects.
