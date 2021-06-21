from distutils.core import setup

setup(
    name='youtubesampler',
    version='1.0',
    description='Youtube Sampler',
    author='Andrew Jensen',
    author_email='andrew.charles.jensen@gmail.com',
    url='https://github.com/acjensen/youtube-sampler',
    packages=['youtubesampler'],
    install_requires=[
        "auditok @ git+https://github.com/amsehili/auditok@271fd15dfb7a1e9da9eade6517cb4345eb56f096",
        "certifi==2020.6.20",
        "chardet==3.0.4",
        "idna==2.10",
        "pydub==0.24.1",
        "pytube==9.6.0",
        "pytube3==9.6.4",
        "RandomWords==0.3.0",
        "requests==2.24.0",
        "typing-extensions==3.7.4.2",
        "urllib3==1.26.5",
        "wincertstore==0.2",
        "youtube-search==1.1.0",
    ],
)