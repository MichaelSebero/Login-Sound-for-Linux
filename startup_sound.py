from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("/-CoolRune-/System_Sounds/login.wav")
play(song)
