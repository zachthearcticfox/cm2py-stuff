import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

rate, data = wav.read('swi.wav')

if len(data.shape) > 1:
    data = data.mean(axis=1)

n = len(data)
frequencies = np.fft.fftfreq(n, d=1/rate)
fft_values = np.fft.fft(data)

fft_magnitude = np.abs(fft_values)

positive_frequencies = frequencies[:n // 2]
positive_magnitude = fft_magnitude[:n // 2]

plt.plot(positive_frequencies, positive_magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.show()

print(positive_frequencies)