import os
import librosa
import numpy as np
# file_data = [f for f in listdir(path) if isfile (join(path, f))]
#     for line in file_data:
#         if ( line[-1:] == '\n' ):
#             line = line[:-1]

#         # Reading Song
#         songname = path + line
path=("c://Users/hp/Documents/GitHub/dsp_project/dataset/inputs/")

# print(os.listdir(path))
# print(os.path.isfile("c:/Users/hp/Documents/GitHub/dsp_project/dataset/inputs/Attention.mp3"))

file_data = [f for f in os.listdir(path) if os.path.isfile (os.path.join(path, f))]
for line in file_data:
    if ( line[-4:] == '.mp3' ):
        line = line[:-4]

        # Reading Song
        songname = path + line+".mp3"
        print(songname)

    
y,sr=librosa.load(songname,duration=60)  
s= np.abs(librosa.stft(y))
onset_env=librosa.onset.onset_strength(y=y,sr=sr)
tempo,beats=librosa.beat.beat_track(y=y,sr=sr)   
print("tempo is\n",tempo)
print("beats is\n",beats)

chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
print('chroma_stft is \n',chroma_stft)
print(np.mean(chroma_stft))
print(np.std(chroma_stft))