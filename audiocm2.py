import numpy as np
import librosa
import matplotlib.pyplot as plt

audio, sr = librosa.load('swi.wav', sr=None)

frame_length = 1024
hop_length = 512

D = librosa.stft(audio, n_fft=frame_length, hop_length=hop_length)

D_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

frequencies = librosa.fft_frequencies(sr=sr, n_fft=frame_length)
times = librosa.times_like(D)

plt.figure(figsize=(10, 6))
librosa.display.specshow(D_db, x_axis='time', y_axis='log', sr=sr, hop_length=hop_length)
plt.colorbar(label='Amplitude (dB)')
plt.title('Spectrogram')
plt.show()


frame_frequencies = D[:, i]
print(f"Frequencies at time {0.00}s: {frame_frequencies}")    
