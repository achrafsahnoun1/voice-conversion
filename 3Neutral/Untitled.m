clear all

clc

 

addpath ('C:\Users\Ghofran ouertani\Desktop\MATLAB R2017a\voicebox')

 

%She had your dark suit and greasy wash water all year

 

All_F0=[];

 

   

seq=dir('D:\p2m\Zippé\AllNeutral\3Neutral');

   

 

 

length(seq)

for k=3:length(seq);

    Nom_seq=seq(k).name

    Nbre=k

    

    cd 'D:\p2m\Zippé\AllNeutral\3Neutral'

     

     [s,fs]=readsph(Nom_seq);

     s=s/max(abs(s));

     

     

    if fs~=16000

        s=resample(s,16000,fs);

        fs=16000;

    end

  

    sound(s,fs)

    pause

    %[fx,tx,pv,fv]=fxpefac(s,fs);

     [fx,vuv]=fxrapt(s,fs);

    

 

  

     

    All_F0=[All_F0; mean(fx)];

 

     

    

end

 

cd 'D:\p2m\Zippé\AllNeutral'

save Mean_F0_Male All_F0


