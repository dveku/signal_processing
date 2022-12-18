import numpy as np
import pandas as pd
import csv


data=pd.read_csv('c://Users/hp/Documents/Github/signal_processing/dataset/data_values/Emotion.csv')
print(data[data['songname']=='Attention']['tempo']['chroma_stft_mean'])