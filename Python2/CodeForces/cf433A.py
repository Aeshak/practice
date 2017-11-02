# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 15:26:22 2017

@author: aeshak
"""
s = raw_input().strip("{}")
if len(s) != 0:
   s = map (lambda x: x.strip(), s.strip().split(","))
   print len(set(s))
else:
   print 0
