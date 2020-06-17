from pytube import YouTube
import librosa
import ffmpeg


class YtSpectrogram:

    def __init__(self, path='./videos'):
        super().__init__()

        self.VIDEOS_PATH = path
        self.VIDEOS_EXTENSION = 'mp4'
        self.AUDIO_EXT = '.wav'

    def get_video_spectrogram(self, video_id):
        self.download_video(video_id)
        self.convert_to_spectrogram(video_id)
        return self.convert_to_spectrogram(video_id)

    def download_video(self, video_id):
        video_stream = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        video_stream.streams.filter(
            type="audio",
            file_extension=self.VIDEOS_EXTENSION
        )[0].download(self.VIDEOS_PATH, filename=video_id)

    def video_to_wav(self, video_id):
        ffmpeg.input(
            f'{self.VIDEOS_PATH}'
            f'/{video_id}'
            f'.{self.VIDEOS_EXTENSION}'
        ).output(
            f'{self.VIDEOS_PATH}'
            f'/{video_id}'
            f'{self.AUDIO_EXT}'
        ).run()

    def convert_to_spectrogram(self, audio_id):
        audio_ts, sr = librosa.load(f'{self.VIDEOS_PATH}/{audio_id}{self.AUDIO_EXT}')
        return librosa.feature.mfcc(y=audio_ts, sr=sr, n_mfcc=128)


if __name__ == "__main__":
    yts = YtSpectrogram()
    # yts.download_video('SOL1vobSELo')
    # yts.video_to_wav('SOL1vobSELo')
    print(yts.convert_to_spectrogram('SOL1vobSELo'))
