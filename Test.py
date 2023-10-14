#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 23:37:31 2023

@author: shelbygolden
"""

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


'''Randomly produce 100 Bernoilli trials 20 times'''

sns.distplot(random.binomial(n = 100, p = 0.5, size = 20)/100, 
             hist = False, label = 'p=0.5')

sns.distplot(random.binomial(n = 100, p = 0.56, size = 20)/100,
             hist = False, label = 'p=0.56')

sns.distplot(random.binomial(n = 100, p = 0.7, size = 20)/100,
             hist = False, label = 'p=0.7')

sns.distplot(random.binomial(n = 100, p = 0.4, size = 20)/100,
             hist = False, label = 'p=0.4')

plt.title('Resulting Histograms')
plt.ylabel('Density')
plt.xlabel('p')
plt.legend()
plt.show()