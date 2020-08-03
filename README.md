# yt-sampler
Randomly sample audio from Youtube!

Random audio can be useful for musical inspiration. :)

# Installation

1. Clone or download yt-sampler from git. (yt-sampler is not registered with PyPI)

2. Install dependencies with `pip`
    > pip install -r requirements.txt

3. Copy **ytsampler.py** into your working directory

# Example

```python
from ytsampler import generate_keywords, search_youtube, download_audio

keywords = generate_keywords()
links = search_youtube(keywords)
download_audio(links[:2], output_path='samples')
```