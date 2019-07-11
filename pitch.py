import numpy as np 
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr

audio='arabic6'
y, sr = lr.load('./{}.wav'.format(audio))
pitches, magnitudes = lr.piptrack(y=y, sr=sr)
print(pitches)
print('///')
print(magnitudes)
