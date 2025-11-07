import subprocess
import sounddevice as sd
import soundfile as sf

fs = 48000
duration = 5

print("🎙️ Recording... Speak now")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()
sf.write('input.wav', audio, fs)
print("✅ Recording complete.")

with open('input.wav', 'rb') as fin, open('output.wav', 'wb') as fout:
    subprocess.run(['rnnoise_demo.exe'], stdin=fin, stdout=fout)

data, fs = sf.read('output.wav')
sd.play(data, fs)
sd.wait()
print("✅ Done! Cleaned audio saved as output.wav")
