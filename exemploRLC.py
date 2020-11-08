#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:54:10 2020

@author: ramon
"""
from scipy import signal
import matplotlib.pyplot as plt

# Seja um circuito RLC em série, a entrada do sistema será o sinal de tensão da fonte e a
# saída será a corrente que circula na malha.
# A EDO que define o sistema é: L.i'' + R.i' + 1/C.i = v'
# Modelando no espaço de estados, x1 = i; x2 = i'; u=v'; y=i=x1
# Dessa forma, teremos as matrizes A, B, C, D como estão abaixo.

R = 1.
L = 10.
C = 0.1

A = [[0., 1.], [-1./L*C, -R/L]]
B = [[0.], [1./L]]
C = [1., 0.]
D = [0.]

sys = signal.StateSpace(A,B,C,D)
t, y = signal.step(sys)

plt.plot(t,y)
plt.show()