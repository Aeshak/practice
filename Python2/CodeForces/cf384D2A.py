# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 22:06:46 2017

@author: aeshak
"""
def coder(n):
   flagi = False
   out = ""
   count = 0
   for i in range(n):
      flagi = not flagi
      flag = flagi
      for i in range(n):
         if flag:
            out += "C"
            count += 1
         else:
            out += "."
         flag = not flag
      out += "\n"
   print count
   print out
n = int(raw_input())
coder(n)
