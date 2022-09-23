from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("/-CoolRune-/System_Sounds/Login.wav")
play(song)
