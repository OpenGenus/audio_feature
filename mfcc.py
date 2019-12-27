import librosa
import numpy as np
import numpy as geek 
  
RATE = 24000
N_MFCC = 13

def get_wav(language_num):
    '''
    Load wav file from disk and down-samples to RATE
    :param language_num (list): list of file names
    :return (numpy array): Down-sampled wav file
    '''

    y, sr = librosa.load('./{}.wav'.format(language_num))
    return(librosa.core.resample(y=y,orig_sr=sr,target_sr=RATE, scale=True))

def to_mfcc(wav):
    '''
    Converts wav file to Mel Frequency Ceptral Coefficients
    :param wav (numpy array): Wav form
    :return (2d numpy array: MFCC
    '''
    return(librosa.feature.mfcc(y=wav, sr=RATE, n_mfcc=N_MFCC))

if __name__ == '__main__':
    
    audio = 'arabic6'
    X= get_wav(audio)
    X=to_mfcc(X)
    c = geek.savetxt('file.txt', X, delimiter =', ')    
    a = open("file.txt", 'r')# open file in read mode 
  
    print("the file contains:") 
    print(a.read()) 
