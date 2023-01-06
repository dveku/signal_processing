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
try:
    Telugu="c://Users/hp/Documents/Github/signal_processing/testing/inputs/telugu/"
    dir_list = os.listdir(Telugu)
    print(dir_list[0:5])
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
    path.append(Telugu + i)
 

# Now check out the label count distribution 
Telugu_df = pd.DataFrame(emotion, columns = ['labels'])
Telugu_df['source'] = 'Telugu'
Telugu_df = pd.concat([Telugu_df, pd.DataFrame(path, columns = ['path'])], axis = 1)
print(Telugu_df.labels.value_counts())
