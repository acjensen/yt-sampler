from youtube_search import YoutubeSearch
from random_words import RandomWords
from pytube import YouTube, Stream
from auditok import split
from typing import List
import os


def generate_keywords() -> List[str]:
    ''' Return two random english words. '''
    rw = RandomWords()
    words = rw.random_words()[0:1]
    return words  # ['polyrhythm', 'Handies Peak']


def search_youtube(keywords: List[str]):
    ''' Return youtube links from provided keywords. '''
    result = {}
    while not result:
        result = YoutubeSearch(
            ' '.join(keywords), max_results=10).to_dict()
        links = ['http://youtube.com/' + r['url_suffix'] for r in result]
    return links


def process_audio(stream: Stream, source_filepath: str) -> None:
    ''' Process the audio stream in the |source_filepath|. '''
    audio_regions = split(source_filepath, energy_threshold=50,
                          max_dur=10, min_dur=1)
    os.remove(source_filepath)
    os.mkdir(source_filepath + '\\')
    for region in audio_regions:
        filename = region.save(source_filepath + "\\{meta.start:.3f}.wav")
        print("sample saved as: {}".format(filename))


def download_audio(links: List[str], output_path: str = None) -> None:
    ''' Download audio from youtube |link|. '''
    for link in links:
        try:
            yt = YouTube(link)
            yt.register_on_complete_callback(process_audio)
            yt.streams.filter(only_audio=True)[
                0].download(output_path=output_path)
        except:
            print(f'Could not download {link}')


if __name__ == "__main__":
    keywords = generate_keywords()
    links = search_youtube(keywords)
    download_audio(links[:2], 'samples')
