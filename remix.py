import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr

audio='arabic6'
y, sr = lr.load('./{}.wav'.format(audio))
_, beat_frames = lr.beat.beat_track(y=y, sr=sr,hop_length=512)
beat_samples = lr.frames_to_samples(beat_frames)
intervals = lr.util.frame(beat_samples, frame_length=2,hop_length=1).T
y_out = lr.effects.remix(y, intervals[::-1])
time = np.arange(0,len(y_out))/sr
fig, ax = plt.subplots()
ax.plot(time,y_out)
ax.set(xlabel='Time(s)',ylabel='sound amplitude')
plt.show()
