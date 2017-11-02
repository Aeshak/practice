# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:28:50 2017

@author: aeshak
"""

P = ["1/6", "1/3", "1/2", "2/3", "5/6", "1/1"]
Y,W = map(int,raw_input().split())
print P[6-max(Y,W)]

