import numpy as np
import matplotlib.pyplot as plt 
from glob import glob
import librosa as lr


audio='arabic6' #change with the name of your audio
y, sr = lr.load('./{}.wav'.format(audio)) #you just need to make sure your audio is in the same folder in which you are coding or else you can change the path as per your requirement
time = np.arange(0,len(y))/sr
print(time) #prints timeline of arabic6
