import cv2 # OpenCV para computer vision
import numpy as np # Para cálculo de matrices
import matplotlib.pyplot as plt #Para graficar
import os
import glob
 
files_names = sorted(glob.glob(dir+'*.jpg'))
 
for idx, name in enumerate(files_names):
    print('Reading '+name)
    img = cv2.imread(files_names[idx])