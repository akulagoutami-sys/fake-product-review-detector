# Code Citations

## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure
```


## License: Apache-2.0
https://github.com/ikp4success/shopasource/blob/b56596f111548f852ff10ccc0115ffec87accd24/shops/nike.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
```


## License: unknown
https://github.com/xiangwenhu/py_vs_js/blob/3ddfd6a9db01009ece72926761cca588c5c2cea5/%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82/request_http.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
```


## License: unknown
https://github.com/sarvesh4396/zippyshare-downloader/blob/00d24c2798f20bc0c57b1c845ad6bc89cdda26b0/app.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
```


## License: unknown
https://github.com/catpersec/usecases/blob/59d1039b03889e331a01ea6b0f9c590824bbb16e/web%20scraping/web_scraping_case_4.py

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
```


## License: unknown
https://github.com/phucbao9x/web-likeness-ctf/blob/953cd1306394a02c6ec57c8898be9a269c2e4ff7/README.md

```
Perfect! I found the indentation error. The code inside the `async with httpx.AsyncClient()` block is incorrectly positioned—the response handling logic is trying to execute outside the block after the connection closes.

Here's the corrected `analyze_link()` function:

```python
@app.post("/analyze/link")
async def analyze_link(request: LinkRequest) -> Dict[str, object]:
    """Analyze reviews extracted from a product link using BeautifulSoup."""
    url = request.url.strip()

    if not url:
        raise HTTPException(
            status_code=400,
            detail="Please provide a valid product URL."
        )

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",
        "Upgrade-Insecure-Requests": "1",
```

