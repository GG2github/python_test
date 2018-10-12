# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:13:18 2018

@author: Sales
"""
# import pandas as pd
# import numpy as np

import re

input = open('C:/Users/mac/Downloads/debug-chen0724%2Fspm.log', 'r')
# input = open('C:/Users/mac/Downloads/spm.2018-10-01.log', 'r')
# input = open('d:/log_20180911.log', 'r')
i=0
udid=[]

#print input[0][0]

for line in input:
    i=i+1
print i


set_data = set()

with open('C:/Users/mac/Downloads/spm.2018-09-28.log','r') as f:
# with open('C:/Users/mac/Downloads/spm.2018-09-18.log','r') as f:
# with open('d:/log_20180911.log', 'r') as f:
    m = f.read()

    data1 = re.findall(r'udid',m)
    print(len(data1))

    data2 = re.findall(r'"logTime":"2018-09-28 20:',m)
    print(len(data2))

    #data = re.findall(r'"udid":"*",',m)
    data = re.findall(r'"udid":"(.*?)",',m)
    # print(data)

    print(len(data))
    print(len(set(data)))










