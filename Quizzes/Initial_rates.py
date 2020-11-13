# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 10:37:50 2020

@author: matthewrowley1
"""

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,50,3000)

def Simulate(A0, B0, k):
        A = np.zeros_like(t)
        B = np.zeros_like(t)
        C = np.zeros_like(t)
        A[0] = A0
        B[0] = B0
        for i in range(len(t)-1):
                C[i+1] = C[i]+3* k*A[i]*A[i]*B[i]
                A[i+1] = A[i]-k*A[i]*A[i]*B[i]
                B[i+1] = B[i]-2*k*A[i]*A[i]*B[i]
                
        return A, B, C
        
A, B, C = Simulate(0.01, 0.01, 0.11)

plt.subplot(1,3,1)
plt.plot(t,C)
plt.xlabel("Time (s)")
plt.ylabel("[C] (M)")
plt.title("Trial 1: [A]$_0$ = 0.0100 M, [B]$_0$ = 0.0100 M")
plt.grid(color='k', linestyle='-', linewidth=.2)

A, B, C = Simulate(0.02, 0.01, 0.11)

plt.subplot(1,3,2)
plt.plot(t,C)
plt.xlabel("Time (s)")
plt.ylabel("[C] (M)")
plt.title("Trial 2: [A]$_0$ = 0.0200 M, [B]$_0$ = 0.0100 M")
plt.grid(color='k', linestyle='-', linewidth=.2)

A, B, C = Simulate(0.02, 0.02, 0.11)

plt.subplot(1,3,3)
plt.plot(t,C)
plt.xlabel("Time (s)")
plt.ylabel("[C] (M)")
plt.title("Trial 3: [A]$_0$ = 0.0200 M, [B]$_0$ = 0.0200 M")
plt.grid(color='k', linestyle='-', linewidth=.2)

plt.show()


'''
top=0.88,
bottom=0.11,
left=0.06,
right=0.965,
hspace=0.17,
wspace=0.205
'''
