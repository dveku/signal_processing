# Import our libraries
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import pandas as pd
import os
import IPython.display as ipd  # To play sound in the notebook



#checking one of the music for excited category of emotion
path = "c://Users/hp/Documents/Github/signal_processing/testing/inputs/telugu/Appudo Ippudo_e.mp3"
X, sample_rate = librosa.load(path, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)  
mfcc = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13)
mean = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)


print(mfcc)

try:
# audio wave
    plt.figure(figsize=(20, 15))
    plt.subplot(3,1,1)
    librosa.display.waveshow(X, sr=sample_rate)
    plt.title('(EXCITED)Audio sampled at 44100 hrz')
    plt.show()
except:
    print("error plotting")
# MFCC
plt.figure(figsize=(20, 15))
plt.subplot(3,1,2)
librosa.display.specshow(mfcc, x_axis='time')
plt.ylabel('MFCC')
plt.title('EXCITED EMOTION MFCC PLOT')
plt.colorbar()
plt.show()

#mean
plt.figure(figsize=(20, 15))
plt.subplot(3,1,1)
plt.plot(mean)
plt.title('mean of mfcc')
plt.show()

#checking one of the music for HAPPY category of emotion
path = "c://Users/hp/Documents/Github/signal_processing/testing/inputs/telugu/Crazy Feeling_h.mp3"
X, sample_rate = librosa.load(path, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)  
mfcc = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13)
mean = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)

print(mfcc)

try:
# audio wave
    plt.figure(figsize=(20, 15))
    plt.subplot(3,1,1)
    librosa.display.waveshow(X, sr=sample_rate)
    plt.title('(HAPPY)Audio sampled at 44100 hrz')
    plt.show()
except:
    print("error plotting")
# MFCC
plt.figure(figsize=(20, 15))
plt.subplot(3,1,2)
librosa.display.specshow(mfcc, x_axis='time')
plt.title('HAPPY EMOTION MFCC PLOT')
plt.ylabel('MFCC')
plt.colorbar()
plt.show()

#mean
plt.figure(figsize=(20, 15))
plt.subplot(3,1,1)
plt.plot(mean)
plt.title('mean of mfcc')
plt.show()



#checking one of the music for RELAXED category of emotion
path = "c://Users/hp/Documents/Github/signal_processing/testing/inputs/telugu/Yenno Yenno_r.mp3"
X, sample_rate = librosa.load(path, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)  
mfcc = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13)
mean = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)

print(mfcc)

try:
# audio wave
    plt.figure(figsize=(20, 15))
    plt.subplot(3,1,1)
    librosa.display.waveshow(X, sr=sample_rate)
    plt.title('(RELAXED)Audio sampled at 44100 hrz')
    plt.show()
except:
    print("error plotting")
# MFCC
plt.figure(figsize=(20, 15))
plt.subplot(3,1,2)
librosa.display.specshow(mfcc, x_axis='time')
plt.title('RELAXED EMOTION MFCC PLOT')
plt.ylabel('MFCC')
plt.colorbar()
plt.show()

#mean
plt.figure(figsize=(20, 15))
plt.subplot(3,1,1)
plt.plot(mean)
plt.title('mean of mfcc')
plt.show()

#checking one of the music for SAD category of emotion
path = "c://Users/hp/Documents/Github/signal_processing/testing/inputs/telugu/Yevevo_s.mp3"
X, sample_rate = librosa.load(path, res_type='kaiser_fast',duration=2.5,sr=22050*2,offset=0.5)  
mfcc = librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13)
mean = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)

print(mfcc)

try:
# audio wave
    plt.figure(figsize=(20, 15))
    plt.subplot(3,1,1)
    librosa.display.waveshow(X, sr=sample_rate)
    plt.title('(SAD)Audio sampled at 44100 hrz')
    plt.show()
except:
    print("error plotting")
# MFCC
plt.figure(figsize=(20, 15))
plt.subplot(3,1,2)
librosa.display.specshow(mfcc, x_axis='time')
plt.title('SAD EMOTION MFCC PLOT')
plt.ylabel('MFCC')
plt.colorbar()
plt.show()

#mean
plt.figure(figsize=(20, 15))
plt.subplot(3,1,1)
plt.plot(mean)
plt.title('mean of mfcc')
plt.show()