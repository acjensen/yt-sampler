# yt-sampler
Randomly sample audio from Youtube!

Random audio can be useful for musical inspiration. :)

# Installation

`python -m pip install -e "git+http://github.com/acjensen/youtube-sampler.git"`

# Example

```python
from youtubesampler import generate_keywords, search_youtube, download_audio

keywords = generate_keywords()
links = search_youtube(keywords)
download_audio(links[:2], output_path='samples')
```