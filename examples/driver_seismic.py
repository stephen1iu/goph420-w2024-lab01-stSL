from goph420_lab01.integration import integrate_gauss

import numpy as np
import matplotlib as plt

s_wave_data=np.loadtxt(fname="s_wave_data.txt")
print(s_wave_data.shape) #(1001,2)
for i in range (0,len(s_wave_data)):
    x=np.array([s_wave_data[i][0]])
    y=np.array([s_wave_data[0][i]])