


clear all

close all

 

 

 

load('All_F0_Male.mat')

Male_F0=All_F0;

clear All_F0

 

[count,center_M]=hist(Male_F0,50);

JM=count/length(Male_F0);

 

load('All_F0_Female.mat')

Female_F0=All_F0;

clear All_F0

[count,center_F]=hist(Female_F0,50);

JF=count/length(Female_F0);

 

 

 

plot(center_M,JM)

hold on

plot(center_F,JF,'r')

legend('Male','Female')

title('Pitch')