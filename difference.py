# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:40:57 2018

@author: Chintan Maniyar
"""

import pandas as pd
import os

path = 'Utah_Lake_Utah/'
dirs = os.listdir(path)
print(dirs[1:])
df = pd.read_csv(path + 'corrected_utah__OL_1_EFR_measurements.csv')
rayleigh = 'rBRR_'
toa = 'rtoa_'
count = 1
diff = []

for d in dirs[1:]:
    if(count < 10):
        diff = df[toa + '0' + str(count)] - df[rayleigh + '0' + str(count)]
    else:
        diff = df[toa + str(count)] - df[rayleigh + str(count)]
    print(path + d)
    diff.to_csv(path + d + '/diff.csv')
    count += 1
