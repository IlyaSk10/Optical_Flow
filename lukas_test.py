# -*- coding: utf-8 -*-
"""lukas_test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19OyF8dCAedmA2bgcLzdFfVnbPKt0eLrS
"""

#!wget 'https://raw.githubusercontent.com/IlyaSk10/Optical_Flow/master/test.gif'

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2

im = Image.open('/content/test.gif')
print("Number of frames: "+str(im.n_frames))

for i in range(im.n_frames):
  im.seek(i)
  im.save('frame{}.png'.format(i))

fig,ax=plt.subplots(1,3,figsize=(15,15))
for i in range(im.n_frames):
  ax[i].imshow(cv2.imread('/content/frame{}.png'.format(i)))

#!git clone 'https://github.com/khushboo-agarwal/Optical-Flow'

import math
from scipy import signal
from PIL import Image
import numpy as np
from numpy import *
from matplotlib import pyplot as plt
from pylab import *
import cv2
import random


def LK_OpticalFlow(Image1,Image2,):
  
  I1 = np.array(Image1)
  I2 = np.array(Image2)
  S = np.shape(I1)

	
  I1_smooth = cv2.GaussianBlur(I1 #input image
								,(3,3)	#shape of the kernel
								,0      #lambda
								)
  I2_smooth = cv2.GaussianBlur(I2, (3,3), 0)

  
		

  Ix = signal.convolve2d(I1_smooth,[[-0.25,0.25],[-0.25,0.25]],'same') + signal.convolve2d(I2_smooth,[[-0.25,0.25],[-0.25,0.25]],'same')
  Iy = signal.convolve2d(I1_smooth,[[-0.25,-0.25],[0.25,0.25]],'same') + signal.convolve2d(I2_smooth,[[-0.25,-0.25],[0.25,0.25]],'same')
  It = signal.convolve2d(I1_smooth,[[0.25,0.25],[0.25,0.25]],'same') + signal.convolve2d(I2_smooth,[[-0.25,-0.25],[-0.25,-0.25]],'same')
	

  features = cv2.goodFeaturesToTrack(I1_smooth # Input image
	,10000 
	,0.01 
	,10 
	)	

  feature = np.int0(features)
  plt.figure(figsize=(20,20))
  plt.subplot(1,3,1)
  plt.title('Frame 1')
  plt.imshow(I1_smooth, cmap = cm.gray)
  plt.subplot(1,3,2)
  plt.title('Frame 2')
  plt.imshow(I2_smooth, cmap = cm.gray)
  for i in feature:
    x,y = i.ravel()
    cv2.circle(I1_smooth 
      ,(x,y) 			 
      ,3 				 
      ,0 			 
      ,-1 			 
      )
	
  
  u = v = np.nan*np.ones(S)

  
  for l in feature:
    j,i = l.ravel()
    
    
    IX = ([Ix[i-1,j-1],Ix[i,j-1],Ix[i-1,j-1],Ix[i-1,j],Ix[i,j],Ix[i+1,j],Ix[i-1,j+1],Ix[i,j+1],Ix[i+1,j-1]]) 
    IY = ([Iy[i-1,j-1],Iy[i,j-1],Iy[i-1,j-1],Iy[i-1,j],Iy[i,j],Iy[i+1,j],Iy[i-1,j+1],Iy[i,j+1],Iy[i+1,j-1]]) 
    IT = ([It[i-1,j-1],It[i,j-1],It[i-1,j-1],It[i-1,j],It[i,j],It[i+1,j],It[i-1,j+1],It[i,j+1],It[i+1,j-1]]) 
    
  
    LK = (IX, IY)
    LK = np.matrix(LK)
    LK_T = np.array(np.matrix(LK)) 
    LK = np.array(np.matrix.transpose(LK)) 
    
    A1 = np.dot(LK_T,LK) 
    A2 = np.linalg.pinv(A1)
    A3 = np.dot(A2,LK_T)
    
    (u[i,j],v[i,j]) = np.dot(A3,IT) 

  
  colors = "bgrcmykw"
  color_index = random.randrange(0,8)
  c=colors[color_index]

  plt.subplot(1,3,3)
  plt.title('Vector plot of Optical Flow')
  plt.imshow(I1,cmap = cm.gray)
  for i in range(S[0]):
    for j in range(S[1]):
      if abs(u[i,j])>t or abs(v[i,j])>t: 
        plt.arrow(j,i,v[i,j],u[i,j],head_width = 5, head_length = 5, color = 'r')
        
  plt.show()

t = 0.3 

Image1 = Image.open('frame0.png').convert('L')
Image2 = Image.open('frame1.png').convert('L')
LK_OpticalFlow(Image1, Image2)