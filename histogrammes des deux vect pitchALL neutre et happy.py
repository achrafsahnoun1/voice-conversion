import numpy as np
from scipy .io import wavfile
import pyworld
import IPython
from IPython.display import Audio
import matplotlib.pyplot as plt
import os


#paramétres par defaut
fs = 16000 
fftlen = pyworld.get_cheaptrick_fft_size(fs)
frame_period = 5 
hop_length = int(fs * (frame_period * 0.001))
### Extraction du pitch totale pour le dossier qui contient 1200 fichiers audio d'une emotion neutre
Allneutre=[]
folder_path='/content/sample_data/neutre'
for path in os.walk(folder_path):
    for i in range (0,1200) :
          fs, x = wavfile.read('/content/sample_data/neutre/'+str(path[2][i]))  
          x = x.astype(np.float64)
          f0, timeaxis = pyworld.dio(x, fs, frame_period=frame_period)
          f0 = pyworld.stonemask(x, f0, timeaxis, fs)
          f0=f0[f0!=0]
          for j in f0 : 
             Allneutre.append(j)
x = np.asarray(Allneutre)
print(x)
np.savetxt("pitchneutrefin.txt",x,fmt='%s', delimiter=",")

### Extraction du pitch totale pour le dossier qui contient 1200 fichiers audio d'une emotion happy

Allhappy=[]
folder_path='/content/sample_data/happy'
for path in os.walk(folder_path):
    for i in range (0,1000) :
          fs, x = wavfile.read('/content/sample_data/happy/'+str(path[2][i]))  
          x = x.astype(np.float64)
          f0, timeaxis = pyworld.dio(x, fs, frame_period=frame_period)
          f0 = pyworld.stonemask(x, f0, timeaxis, fs)
          f0=f0[f0!=0]
          for j in f0 : 
             Allhappy.append(j)

y = np.asarray(Allhappy)
print(y)
np.savetxt("pitchhappyfin.txt",y,fmt='%s', delimiter=",")


### histogrammes des deux vecteurs 
def plotHistogram(p, o):
    bins=np.linspace(0,200,100)
    plt.hist([x, y], bins, label=['Neutre', 'Happy'])
    plt.legend(loc='upper right')
    plt.show()

plotHistogram(x, y)
