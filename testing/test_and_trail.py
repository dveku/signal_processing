import os
import librosa
import numpy as np
import csv
# file_data = [f for f in listdir(path) if isfile (join(path, f))]
#     for line in file_data:
#         if ( line[-1:] == '\n' ):
#             line = line[:-1]

#         # Reading Song
#         songname = path + line
path=("c://Users/hp/Documents/GitHub/signal_processing/dataset/inputs/")

# print(os.listdir(path))
# print(os.path.isfile("c:/Users/hp/Documents/GitHub/dsp_project/dataset/inputs/Attention.mp3"))

y,sr=librosa.load('c:/Users/hp/Documents/GitHub/signal_processing/dataset/inputs/Attention.mp3',duration=1)  
s= np.abs(librosa.stft(y))
mfcc = librosa.feature.mfcc(y=y, sr=sr)
f=open('C://Users/hp/Documents/GitHub/signal_processing/testing/test.txt','w')
f.write('MFCC\n')
f.write(str(mfcc))
f.close()