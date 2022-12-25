#Objective:
    # To test and check the conditions

#importing all the libraries
import librosa
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile,join
import csv
import time
#-------------------------------------------------
global number

def feature_extract(path):
    #opening and setting up the csv file
    
    number =1
   
    id=0 #Song ID
    songid=0
    data_content=[]
    header_flag=0#please note... this is a trial and not sure if this variable is working or not
    # ---------------------------------------------------
    
    total_time=0
    #creating the path for each audio to be read
    file_data=[f for f in listdir(path) if isfile(join(path,f))]
    path=path+"/"
    for song in file_data:
        if(song[-4:]=='.mp3'):
            song=song[:-4]#extracting the song name
            
                #creating the path for each song
            songpath=path+song+".mp3"
        # READING THE AUDIO SIGNAL
        
        a=0
        b=0
        
        a=time.time()
        
        y, sr = librosa.load(songpath, duration=60)
        S = np.abs(librosa.stft(y))
           
        id=id+1   
           
        #extraction of features
        #Individual Feature Vectors
        
        #1.tempo and beats
        tempo,beats=librosa.beat.beat_track(y=y,sr=sr)  
        total_beats=np.sum(beats)
        average_beats=np.average(beats)
        #2.chromagram stft
        chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
        chroma_stft_mean=np.mean(chroma_stft)
        chroma_stft_std=np.std(chroma_stft)
        chroma_stft_var=np.var(chroma_stft)
        #3.chromagram const q transform
        chroma_cq = librosa.feature.chroma_cqt(y=y, sr=sr)
        chroma_cq_mean=np.mean(chroma_cq)
        chroma_cq_std=np.std(chroma_cq)
        chroma_cq_var=np.var(chroma_cq)
        #4.chormagram cens
        chroma_cens = librosa.feature.chroma_cens(y=y, sr=sr)
        chroma_cens_mean=np.mean(chroma_cens)
        chroma_cens_std=np.std(chroma_cens)
        chroma_cens_var=np.var(chroma_cens)  
        #5.melspectrogram
        melspectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
        melspectrogram_mean=np.mean(melspectrogram)
        melspectrogram_std=np.std(melspectrogram)
        melspectrogram_var=np.var(melspectrogram)
        #6.mfcc
        mfcc = librosa.feature.mfcc(y=y, sr=sr)
        mfcc_mean=np.mean(mfcc)
        mfcc_std=np.std(mfcc)
        mfcc_var=np.var(mfcc)
        #7.mfcc delta
        mfcc_delta = librosa.feature.delta(mfcc)
        mfcc_delta_mean=np.mean(mfcc_delta)
        mfcc_delta_std=np.std(mfcc_delta)
        mfcc_delta_var=np.var(mfcc_delta)
        #8. rmse
        rmse = librosa.feature.rms(y=y)
        rmse_mean=np.mean(rmse)
        rmse_std=np.std(rmse)
        rmse_var=np.var(rmse)
        #9.cent-spectral_centroid
        cent = librosa.feature.spectral_centroid(y=y, sr=sr)
        cent_mean=np.mean(cent)
        cent_std=np.std(cent)
        cent_var=np.var(cent)
        #10. speactral_bandwith
        spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
        spec_bw_mean=np.mean(spec_bw)
        spec_bw_std=np.std(spec_bw)
        spec_bw_var=np.var(spec_bw)
        #11.contrast
        contrast = librosa.feature.spectral_contrast(S=S, sr=sr)
        contrast_mean=np.mean(contrast)
        contrast_std=np.std(contrast)
        contrast_var=np.var(contrast)
        #12.rolloff
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
        rolloff_mean=np.mean(rolloff)
        rolloff_std=np.std(rolloff)
        rolloff_var=np.var(rolloff)
        #13. polynomial features
        poly_features = librosa.feature.poly_features(S=S, sr=sr)
        poly_mean=np.mean(poly_features)
        poly_std=np.std(poly_features)
        poly_var=np.var(poly_features)
        #14. tonnetz
        tonnetz = librosa.feature.tonnetz(y=y, sr=sr)
        tonnetz_mean=np.mean(tonnetz)
        tonnetz_std=np.std(tonnetz)
        tonnetz_var=np.var(tonnetz) 
        #15. zero crossing rate
        zcr = librosa.feature.zero_crossing_rate(y)
        zcr_mean=np.mean(zcr)
        zcr_std=np.std(zcr)
        zcr_var=np.var(zcr)
        #16. harmonic
        harmonic = librosa.effects.harmonic(y)
        harmonic_mean=np.mean(harmonic)
        harmonic_std=np.std(harmonic)
        harmonic_var=np.var(harmonic)
        #17. percussive
        percussive = librosa.effects.percussive(y)
        perc_mean=np.mean(percussive)
        perc_std=np.std(percussive)
        perc_var=np.var(percussive)
        #18. onset frames
        onset_frames = librosa.onset.onset_detect(y=y, sr=sr)
        frames_to_time = librosa.frames_to_time(onset_frames[:20], sr=sr)
        frame_mean=np.mean(frames_to_time)
        frame_std=np.std(frames_to_time)
        frame_var=np.var(frames_to_time)
            #-----------------------------------------------------
        
        
        data_header=['id','songname','tempo','total_beats','average_beats','chroma_stft_mean','chroma_stft_std','chroma_stft_var','chroma_cq_mean','chroma_cq_std','chroma_cq_var','chroma_cens_mean','chroma_cens_std','chroma_cens_var','melspectrogram_mean','melspectrogram_std','melspectrogram_var','mfcc_mean','mfcc_std','mfcc_var','mfcc_delta_mean','mfcc_delta_std','mfcc_delta_var','rmse_mean','rmse_std','rmse_var','cent_mean','cent_std','cent_var','spec_bw_mean','spec_bw_std','spec_bw_var','contrast_mean','contrast_std','contrast_var','rolloff_mean','rolloff_std','rolloff_var','poly_mean','poly_std','poly_var','tonnetz_mean','tonnetz_std','tonnetz_var','zcr_mean','zcr_std','zcr_var','harmonic_mean','harmonic_std','harmonic_var','perc_mean','perc_std','perc_var','frame_mean','frame_std','frame_var']
        
        data_features=[]
            
    
            #appending the values of all the features extracted
        data_features.append(id)
        data_features.append(song)
        data_features.append(tempo)
        data_features.append(total_beats)
        data_features.append(average_beats)
        data_features.append(chroma_stft_mean)
        data_features.append(chroma_stft_std)
        data_features.append(chroma_stft_var)
        data_features.append(chroma_cq_mean)
        data_features.append(chroma_cq_std)
        data_features.append(chroma_cq_var)
        data_features.append(chroma_cens_mean)
        data_features.append(chroma_cens_std)
        data_features.append(chroma_cens_var)
        data_features.append(melspectrogram_mean)
        data_features.append(melspectrogram_std)
        data_features.append(melspectrogram_var)
        data_features.append(mfcc_mean)
        data_features.append(mfcc_std)
        data_features.append(mfcc_var)
        data_features.append(mfcc_delta_mean)
        data_features.append(mfcc_delta_std)
        data_features.append(mfcc_delta_var)
        data_features.append(rmse_mean)
        data_features.append(rmse_std)
        data_features.append(rmse_var)
        data_features.append(cent_mean)
        data_features.append(cent_std)
        data_features.append(cent_var)
        data_features.append(spec_bw_mean)
        data_features.append(spec_bw_std)
        data_features.append(spec_bw_var)
        data_features.append(contrast_mean)
        data_features.append(contrast_std)
        data_features.append(contrast_var)
        data_features.append(rolloff_mean)
        data_features.append(rolloff_std)
        data_features.append(rolloff_var)
        data_features.append(poly_mean)
        data_features.append(poly_std)
        data_features.append(poly_var)
        data_features.append(tonnetz_mean)
        data_features.append(tonnetz_std)
        data_features.append(tonnetz_var)
        data_features.append(zcr_mean)
        data_features.append(zcr_std)
        data_features.append(zcr_var)
        data_features.append(harmonic_mean)
        data_features.append(harmonic_std)
        data_features.append(harmonic_var)
        data_features.append(perc_mean)
        data_features.append(perc_std)
        data_features.append(perc_var)
        data_features.append(frame_mean)
        data_features.append(frame_std)
        data_features.append(frame_var)
        #Attributes
        b=time.time()
        t=b-a
        total_time=total_time+t
        print(f'song {number}-{song} features extracted!') 
        print(f'time spent to extract= {t} sec')
        
        
        number=number+1
        
         #-----------------------------------------------------------------
         #appending the features of one song to the csv file       
        data_content.append(data_features)
        
        #Writing into the csv file
        with open('c://Users/hp/Documents/Github/signal_processing/dataset/data_values/Emotion.csv','w') as file:
            writer =csv.writer(file)
            if(header_flag==0):
                writer.writerow(data_header)
                header_flag==1
            writer.writerows(data_content)  
        
    print(f'total time allocated is {total_time/60} min')
#calling the feature extraction function
feature_extract('c://Users/hp/Documents/Github/signal_processing/dataset/inputs')
