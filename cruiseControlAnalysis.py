#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 00:39:18 2020

@author: ramon
"""

import control
import numpy as np
import matplotlib.pyplot as plt


# Modelaremos a velocidade de um veículo que se 
# move com velocidade v e, portanto, aceleraçao v'.
# Considerando a resistência do ar proporcional a velocidade,
# com constaante de proporcionalidade igual à b, e a massa do carro
# igual à m, se a força responsável por controlar a velocidade (entrada)
# for igual à u, teremos: mv' = u - bv => v' = -b/m v + 1/m u
# Como queremos saber a respeito da velocidade, teremos y = 1v + 0u


m = 1000.0
b = 50.


A = [-b/m]
B = [1./m]
C = [1.]
D = [0.]

sys = control.ss(A,B,C,D)


"""
# Conversion from State Space to Transfer Function
sysTF = control.ss2tf(sys)

# Eigenvalues and eigenvectors of a matrix K
K = [[1., 2.], [3., 4.]]
eigValues = np.linalg.eig(K)[0]
eigVectors = np.linalg.eig(K)[1]

#Observability Matrix
O = control.obsv(A,C)

# Controllability Matrix
C = control.ctrb(A,B)

# Rank of the matrix C
rank = np.linalg.matrix_rank(C)

# Gramian of the system
Wt = control.gram(sys, 'c')

# Poles
poles = control.pole(sys)

# Pole/zero map
control.pzmap(sys)

# Root Locus plot
plt.figure()
control.root_locus(sys)

# Bode plot
plt.figure()
mag, phase, omega = control.bode(sys)

# Nyquist plot
plt.figure()
real, imag, freq = control.nyquist_plot(sys)

# Step Response
t, y = control.step_response(sys)
plt.figure()
plt.plot(t,y)
"""