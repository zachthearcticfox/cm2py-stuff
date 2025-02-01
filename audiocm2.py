import numpy as np
from scipy.signal import stft
from pydub import AudioSegment
import cm2py as cm2
import pyperclip as pyclip

blocks, connections, save = [], [], cm2.Save()

def get_frequency_dict(file_path):
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1)  # Mono
    sr = audio.frame_rate
    samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
    samples /= np.max(np.abs(samples))  # Normalize

    # STFT parameters
    hop_length = int(sr * 0.001)  # 1 ms step
    n_fft = 2048
    overlap = n_fft - hop_length

    # Compute STFT
    freqs, _, Zxx = stft(samples, fs=sr, nperseg=n_fft, noverlap=overlap, window='hann')
    magnitudes = np.abs(Zxx)

    # Build dictionary {time_ms: frequency}
    frequency_dict = {}
    for frame_idx, frame in enumerate(magnitudes.T):
        time_ms = frame_idx  # 1 ms per step
        if np.max(frame) > 1e-6:  # Silence threshold
            dominant_freq = freqs[np.argmax(frame)]
        else:
            dominant_freq = 0.0
        frequency_dict[time_ms] = float(dominant_freq)  # Convert to native Python float

    return frequency_dict

# Example usage
frequency_dict = get_frequency_dict("non-python/swi.wav")
xc = 0
zc = 0

for i in frequency_dict.values():
    blocks.append(save.addBlock(cm2.SOUND, (xc,0,zc), False, properties=[i if i < 16000 else 16000]))
    xc += 1
    if xc % 10 == 0: zc += 1

for i in range(len(blocks)):
    try:
        connections.append(save.addConnection(blocks[i], blocks[i+1]))
    except IndexError as e:
        break

asciisave = save.exportSave()
pyclip.copy(asciisave)