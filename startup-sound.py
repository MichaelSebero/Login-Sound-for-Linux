import subprocess

def play_audio(file_path):
    # Use subprocess to call aplay in the background
    process = subprocess.Popen(['aplay', file_path])
    process.wait()  # Wait for the audio playback to finish

if __name__ == "__main__":
    file_path = "YOUR_SOUND_PATH"  # Update this to your file path
    play_audio(file_path)
