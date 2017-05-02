from aubio import source
import librosa
#from pydub import AudioSegment

data, rate = librosa.load("Test.wav")
print(len(data), rate)