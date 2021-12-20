#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:47:13 2021

@author: nidiana
"""

# program to read the outputs produced with python
# To analyse ALM information

import pandas as pd
import numpy 
import matplotlib.pyplot as plt
import math
import os


R=0.25
H=0.73
Nb=2
c=0.0375

fileDir = os.path.dirname(os.path.realpath('__file__'))
file_location = os.path.join(fileDir, 'MotionT03/postProcessing/turbines/0/turbine.csv')

V=0.5
TSR=4.71
w=TSR*V/R
T=2*math.pi/w
Aref=2*R*H


df = pd.read_csv(file_location);  # to read the wind turbine parameter analysis

#print(df)

#print(type(df['Frontal Area (ft^2)'][0])) To see the type of data in that column

#Assigning the parameter values corresponding to the case ejecuted

#print("x3 ndim: ", df.ndim)
#print("x3 shape:", df.shape)
titles=list(df)


df.head()
type(df.to_numpy()) # convert the  read data to array with numpy
x=df.to_numpy()[0] # to read the first line of data [0], the first assigned row with data
time=x[0]
azi=x[1]; # radious of reference, 
tsr=x[2]; # Aread of referencia, for straight blade 2R*H
cp=x[3]; # repolutions per minute
cd=x[4]; # Velocity in the free-stream
ct=x[5];  # density
cd1=x[6]; # temperature 
ct1=x[7]; # viscosity
cd2=x[8];
ct2=x[9]; # tip speed ratio


df.head()
array_t1=(df.to_numpy()) # convert the  read data to array with numpy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               

timeT1=array_t1[:,[0]] #tN=tUref/R  Normalized time
CoefT1=array_t1[:,[5]]
CoefP1=array_t1[:,[3]]
Thust=array_t1[:,[4]]
teta=array_t1[:,[1]]%360

#Defining number of cycles
NoCycles=timeT1[-1]//T
iLast_t=(NoCycles-1)*T
indexs = list(map(lambda i: i> iLast_t, timeT1)).index(True)
indexf = list(map(lambda i: i> iLast_t+T, timeT1)).index(True)


plt.figure(1)
plt.plot(array_t1[:,[1]], CoefP1,'bo') #
#plt.plot(timeT1[indexs:indexf], CoefP1[indexs:indexf],'bo') 
plt.xlabel('Time (s)')
plt.ylabel('Power Coefficient ($C_P$)')

#plt.savefig('CPAL01.png', dpi=300, bbox_inches='tight')
plt.show()

plt.rcParams.update({'font.size':16})

plt.figure(2)
plt.plot(teta[indexs:indexf], Thust[indexs:indexf],'bo') 
plt.xlabel('Azimuthal angle ($^\circ$)')
plt.ylabel('Thrust Coefficient ($C_T$)')
plt.legend(['ALM turbineFoam'])
#plt.savefig('CPAL01.png', dpi=300, bbox_inches='tight')
plt.show()



CThr_ave=numpy.mean(Thust[indexs:indexf])
CP_ave=numpy.mean(CoefP1[indexs:indexf])
Re_ave=TSR*V*c/0.000001

print('TSR =', TSR, 'CP_ave =', CP_ave, 'CThr_ave = ', CThr_ave, 'Re_ave',Re_ave)