#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 00:39:18 2020

@author: ramon
"""
from scipy import signal
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

sys = signal.StateSpace(A,B,C,D)
t, y = signal.step(sys)

plt.plot(t, y)
plt.show()