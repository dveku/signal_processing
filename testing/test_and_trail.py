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
onset_env=librosa.onset.onset_strength(y=y,sr=sr)
tempo,beats=librosa.beat.beat_track(y=y,sr=sr)   


chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
print('chroma_stft is \n',chroma_stft)
print("mean-",np.mean(chroma_stft))
print("std-",np.std(chroma_stft))
f=open('C://Users/hp/Documents/GitHub/signal_processing/testing/test.txt','w')
f.write('chromagram study\n')
f.write(str(chroma_stft))