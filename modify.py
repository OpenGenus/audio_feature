import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr

audio='arabic6'
y, sr = lr.load('./{}.wav'.format(audio))
y_fast = lr.effects.time_stretch(y, 2.0)
time = np.arange(0,len(y_fast))/sr
fig, ax = plt.subplots()
ax.plot(time,y_fast)
ax.set(xlabel='Time(s)',ylabel='sound amplitude')
plt.show()#compress to be twice as fast

y_slow = lr.effects.time_stretch(y, 0.5)
time = np.arange(0,len(y_slow))/sr
fig, ax = plt.subplots()
ax.plot(time,y_slow)
ax.set(xlabel='Time(s)',ylabel='sound amplitude')
plt.show()#half the original speed
