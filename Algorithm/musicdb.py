import sqlite3
import csv
try:
    conn=sqlite3.connect('music.db')
    print("database connected successfully!")
except:
    print("Error connecting to database")
    
cr=conn.cursor()

# cr.execute("""CREATE TABLE music_feature(
#                 songid INTEGER PRIMARY KEY,          
#                 songname TEXT,
#                 tempo REAL,
#                 total_beats INTEGER,
#                 average_beats REAL,
#                 chroma_stft_mean REAL,
#                 chroma_stft_std REAL,
#                 chroma_stft_var REAL,
#                 chroma_cq_mean REAL,
#                 chroma_cq_std REAL,
#                 chroma_cq_var REAL,
#                 chroma_cens_mean REAL,
#                 chroma_cens_std REAL,
#                 chroma_cens_var REAL,
#                 melspectrogram_mean REAL,
#                 melspectrogram_std REAL,
#                 melspectrogram_var REAL,
#                 mfcc_mean REAL,
#                 mfcc_std REAL,
#                 mfcc_var REAL,
#                 mfcc_delta_mean REAL,
#                 mfcc_delta_std REAL,
#                 mfcc_delta_var REAL,
#                 rmse_mean REAL,
#                 rmse_std REAL,
#                 rmse_var REAL,
#                 cent_mean REAL,
#                 cent_std REAL,
#                 cent_var REAL,
#                 spec_bw_mean REAL,
#                 spec_bw_std REAL,
#                 spec_bw_var REAL,
#                 contrast_mean REAL,
#                 contrast_std REAL,
#                 contrast_var REAL,
#                 rolloff_mean REAL,
#                 rolloff_std REAL,
#                 rolloff_var REAL,
#                 poly_mean REAL,
#                 poly_std REAL,
#                 poly_var REAL,
#                 tonnetz_mean REAL,
#                 tonnetz_std REAL,
#                 tonnetz_var REAL,
#                 zcr_mean REAL,
#                 zcr_std REAL,
#                 zcr_var REAL,
#                 harmonic_mean REAL,
#                 harmonic_std REAL,
#                 harmonic_var REAL,
#                 perc_mean REAL,
#                 perc_std REAL,
#                 perc_var REAL,
#                 frame_mean REAL,
#                 frame_std REAL,
#                 frame_var REAL
#                 )""")


with open("c://Users/hp/Documents/Github/signal_processing/dataset/data_values/Emotion.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    music=[]
    data=['songid','songname','tempo','total_beats','average_beats','chroma_stft_mean','chroma_stft_std','chroma_stft_var','chroma_cq_mean','chroma_cq_std','chroma_cq_var','chroma_cens_mean','chroma_cens_std','chroma_cens_var','melspectrogram_mean','melspectrogram_std','melspectrogram_var','mfcc_mean','mfcc_std','mfcc_var','mfcc_delta_mean','mfcc_delta_std','mfcc_delta_var','rmse_mean','rmse_std','rmse_var','cent_mean','cent_std','cent_var','spec_bw_mean','spec_bw_std','spec_bw_var','contrast_mean','contrast_std','contrast_var','rolloff_mean','rolloff_std','rolloff_var','poly_mean','poly_std','poly_var','tonnetz_mean','tonnetz_std','tonnetz_var','zcr_mean','zcr_std','zcr_var','harmonic_mean','harmonic_std','harmonic_var','perc_mean','perc_std','perc_var','frame_mean','frame_std','frame_var']
    next(csvreader)
    for row in csvreader:
        if(row==[]):
            continue
        music.append(tuple(row))
        
        #Insert links into table

try:
    cr.executemany("""INSERT INTO music_feature(songid,songname,tempo,total_beats,average_beats,chroma_stft_mean,chroma_stft_std,chroma_stft_var,chroma_cq_mean,chroma_cq_std,chroma_cq_var,chroma_cens_mean,chroma_cens_std,chroma_cens_var,melspectrogram_mean,melspectrogram_std,melspectrogram_var,mfcc_mean,mfcc_std,mfcc_var,mfcc_delta_mean,mfcc_delta_std,mfcc_delta_var,rmse_mean,rmse_std,rmse_var,cent_mean,cent_std,cent_var,spec_bw_mean,spec_bw_std,spec_bw_var,contrast_mean,contrast_std,contrast_var,rolloff_mean,rolloff_std,rolloff_var,poly_mean,poly_std,poly_var,tonnetz_mean,tonnetz_std,tonnetz_var,zcr_mean,zcr_std,zcr_var,harmonic_mean,harmonic_std,harmonic_var,perc_mean,perc_std,perc_var,frame_mean,frame_std,frame_var) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """, music)
except:
            print("error entering data")
            
conn.commit()
    
cr.execute("SELECT songname FROM music_feature")

print(cr.fetchall())    
        
        


conn.commit()

conn.close()