import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from matplotlib.pyplot import specgram
import pandas as pd
import glob 
from sklearn.metrics import confusion_matrix
import IPython.display as ipd  # To play sound in the notebook
import os
import sys
import warnings
import csv
# ignore warnings 
if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning) 

#___________________________telugu category songs________________________________#
try:
    Telugu="c://Users/hp/Documents/Github/signal_processing/testing/inputs/telugu/"
    dir_list = os.listdir(Telugu)
except:
    print('failed')
    

# parse the filename to get the emotions
emotion=[]
path = []
for i in dir_list:
    if i[-6:-4]=='_h':
        emotion.append('happy')
    elif i[-6:-4]=='_e':
        emotion.append('excited')
    elif i[-6:-4]=='_r':
        emotion.append('relaxed')
    elif i[-6:-4]=='_s':
        emotion.append('sad')
    # elif i[-6:-4]=='_n':
    #     emotion.append('neutral')
    # elif i[-6:-4]=='_d':
    #     emotion.append('depressed')
    # elif i[-5:]=='su':
    #     emotion.append('male_surprise')
    else:
        emotion.append('error') 
        print(emotion)
    path.append(Telugu + i)
    
 

# Now check out the label count distribution 
Telugu_df = pd.DataFrame(emotion, columns = ['labels'])
Telugu_df['source'] = 'Telugu'
Telugu_df = pd.concat([Telugu_df, pd.DataFrame(path, columns = ['path'])], axis = 1)
print("Telugu")
print(Telugu_df.labels.value_counts())


#____________________________________Kannada category songs__________________________#

try:
    Kannada="c://Users/hp/Documents/Github/signal_processing/testing/inputs/kannada/"
    dir_list = os.listdir(Kannada)
except:
    print('failed')
    

# parse the filename to get the emotions
emotion=[]
path = []
for i in dir_list:
    if i[-6:-4]=='_h':
        emotion.append('happy')
    elif i[-6:-4]=='_e':
        emotion.append('excited')
    elif i[-6:-4]=='_r':
        emotion.append('relaxed')
    elif i[-6:-4]=='_s':
        emotion.append('sad')
    # elif i[-6:-4]=='_n':
    #     emotion.append('neutral')
    # elif i[-6:-4]=='_d':
    #     emotion.append('depressed')
    # elif i[-5:]=='su':
    #     emotion.append('male_surprise')
    else:
        emotion.append('error') 
    path.append(Kannada + i)
 

# Now check out the label count distribution 
Kannada_df = pd.DataFrame(emotion, columns = ['labels'])
Kannada_df['source'] = 'Kannada'
Kannada_df = pd.concat([Kannada_df, pd.DataFrame(path, columns = ['path'])], axis = 1)
print("Kannada")
print(Kannada_df.labels.value_counts())



df = pd.concat([Telugu_df, Kannada_df], axis = 0)
print("Combined")
print(df.labels.value_counts())
df.head()
df.to_csv("c://Users/hp/Documents/Github/signal_processing/testing/Data_path.csv",index=False)