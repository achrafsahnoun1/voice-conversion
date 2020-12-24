import numpy as np
from scipy .io import wavfile
import pyworld
import IPython
from IPython.display import Audio
import matplotlib.pyplot as plt
fs = 16000 
fftlen = pyworld.get_cheaptrick_fft_size(fs)
frame_period = 5 
hop_length = int(fs * (frame_period * 0.001))
### Extraction du pitch

fs, x = wavfile.read('File Path')  
x = x.astype(np.float64)
f0, timeaxis = pyworld.dio(x, fs, frame_period=frame_period)
f0 = pyworld.stonemask(x, f0, timeaxis, fs)          
plt.plot(timeaxis,f0,"g")
'''
voici la procedure de modification du pitch dans la phase de conversion
plt.plot(timeaxis,f0,"g")
'''
plt.title("fundamental frequency [Hz]")
plt.show()

### Extraction du spectrogram
spectrogram = pyworld.cheaptrick(x, f0, timeaxis, fs)
plt.figure()
plt.plot(timeaxis,spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s] ')
plt.title('Spectrogram with scipy.signal',size=16)

### Extraction du aperiodicity 

aperiodicity = pyworld.d4c(x, f0, timeaxis, fs) 
plt.figure()
plt.plot(timeaxis,aperiodicity)
plt.title('Aperiodicity',size=16);
plt.xlabel('Time [s] ')
print("shape=",aperiodicity.shape)

a = np.asarray(aperiodicity)
np.savetxt("val.csv", a, delimiter=",") #pour enregistrer le vecteur d'aperiodicity dans un csv file
"""
voici les procedures de modifications du vecteur de l'aperiodicity dans la phase de conversion
#aperiodicity=np.ones((2576, 513))/2
#aperiodicity=np.zeros((2576, 513))
#aperiodicity=np.ones((2576, 513))
#aperiodicity=np.random.rand(2576,513)
#aperiodicity=np.random.randint(2,size=(2576,513))
"""
aperiodicity=aperiodicity.astype(float)
print("aperiodi",aperiodicity)

### Fonction de synthese   
waveform = pyworld.synthesize(f0, spectrogram, aperiodicity, fs, frame_period)

### Play audio 
IPython.display.display(Audio(waveform, rate=fs))

