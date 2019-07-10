import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr


audio='arabic6'
y, sr = lr.load('./{}.wav'.format(audio))
time = np.arange(0,len(y))/sr
fig, ax = plt.subplots()
ax.plot(time,y)
ax.set(xlabel='Time(s)',ylabel='sound amplitude')
plt.show()
