import numpy as np
import matplotlib.pyplot as plot
from scipy import pi
from scipy.fftpack import fft
import librosa as lr
import librosa.display

audio='arabic6'
y, sr = lr.load('./{}.wav'.format(audio))
signalAmplitude   = np.sin(y)
plot.subplot(211)
plot.plot(y, signalAmplitude,'bs')
plot.xlabel('time')
plot.ylabel('amplitude')
plot.subplot(212)
plot.magnitude_spectrum(signalAmplitude,Fs=4)
plot.show()
