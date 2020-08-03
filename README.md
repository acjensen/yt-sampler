# yt-sampler
Randomly sample audio from Youtube

Very useful for musical inspiration :)

# Installation
There is no official installation hook for ytsampler. Download ytsampler.py from git to the same directory as your script

Install dependencies with `pip`
> pip install -r requirements.txt

# Example

> from ytsampler import generate_keywords, search_youtube, download_audio
>
> keywords = generate_keywords()
> links = search_youtube(keywords)
> download_audio(links, output_path='C://')