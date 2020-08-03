# yt-sampler
Randomly sample audio from Youtube!

Very useful for musical inspiration :)

# Installation

1. Clone or download the repo. yt-sampler is not on PyPI.
2. Install dependencies with `pip`
> pip install -r requirements.txt
3. Copy ytsampler.py into the same directory as your script

# Example

> from ytsampler import generate_keywords, search_youtube, download_audio
>
> keywords = generate_keywords()
> links = search_youtube(keywords)
> download_audio(links, output_path='C://')