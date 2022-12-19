import mysql.connector


# #creating a connection to mysql

# db=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="dhanush2002"
# )

# cr=db.cursor()

#  cr.execute("SHOW DATABASES")

#  for i in cr:
#      print(i)
    
#  cr.execute("CREATE DATABASE TEST")

# cr.execute("SHOW DATABASES")

# for i in cr:
#     print(i)
  
db=mysql.connector.connect(host="localhost",user="root",password="dhanush2002",database="test")  
cr=db.cursor()  
    
cr.execute("CREATE TABLE features(id INT PRIMARY KEY AUTO_INCREMENT,songname VARCHAR(30),tempo FLOAT,total_beats FLOAT,average_beats FLOAT,chroma_stft_mean FLOAT,chroma_stft_std FLOAT,chroma_stft_var FLOAT,chroma_cq_mean FLOAT,chroma_cq_std FLOAT,chroma_cq_var FLOAT,chroma_cens_mean FLOAT,chroma_cens_std FLOAT,chroma_cens_var FLOAT,melspectrogram_mean FLOAT,melspectrogram_std FLOAT,melspectrogram_var FLOAT,mfcc_mean FLOAT,mfcc_std FLOAT,mfcc_var FLOAT,mfcc_delta_mean FLOAT,mfcc_delta_std FLOAT,mfcc_delta_var FLOAT,rmse_mean FLOAT,rmse_std FLOAT,rmse_var,cent_mean FLOAT,cent_std FLOAT,cent_var FLOAT,spec_bw_mean FLOAT,spec_bw_std FLOAT,spec_bw_var FLOAT,contrast_mean FLOAT,contrast_std FLOAT,contrast_var FLOAT,rolloff_mean FLOAT,rolloff_std FLOAT,rolloff_var FLOAT,poly_mean FLOAT,poly_std FLOAT,poly_var FLOAT,tonnetz_mean FLOAT,tonnetz_std FLOAT,tonnetz_var FLOAT,zcr_mean FLOAT,zcr_std FLOAT,zcr_var FLOAT,harmonic_mean FLOAT,harmonic_std FLOAT,harmonic_var FLOAT,perc_mean FLOAT,perc_std FLOAT,perc_var FLOAT,frame_mean FLOAT,frame_std FLOAT,frame_var FLOAT)")

cr.execute("DESCRIBE features")
