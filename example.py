from ytsampler import generate_keywords, search_youtube, download_audio

keywords = generate_keywords()
links = search_youtube(keywords)
download_audio(links[:2], 'samples')
