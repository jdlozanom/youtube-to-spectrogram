from setuptools import setup, find_packages

setup(
    name="ytspectro",
    version="0.0.1",
    packages=find_packages(where='ytspectro'),
    url='https://github.com/jdlozanom/youtube-to-spectrogram',
    description="Spectrogram maker from youtube audios",
    author="Juan Diego Lozano",
    license="MIT",
    install_requires=[
        'ffmpeg-python~=0.2.0',
        'librosa~=0.7.2',
        'numba==0.48.0',
        'pytube3~=9.6.4'
    ]
)
