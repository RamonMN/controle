# Script para visualização do Princípio do Argumento de Cauchy
# Autor: Ramon Machado Ribeiro de Assumpção Nunes
# Curso: Engenharia de Controle e Automação - IFF

import matplotlib.pyplot as plt
import control as ctl 
import numpy as np 
import matplotlib.animation as animation

# Contorno no dominio (plano s)
theta = np.linspace(0, 2*np.pi, 100)
radius = 1
a = radius*np.cos(theta) - 3.5   # Eq. parametricas do circulo
b = radius*np.sin(theta)
s = a + b*1j


# Contorno resultante na imagem (plano F(S))
num = [1, -2, 1.25]
den = [1, 7, 12]
F = ctl.tf(num, den)
w = [ctl.evalfr(F,s[i]) for i in range(len(s))]


# Desenho do mapeamento (domínio, imagem)
def animate(i):
    axs[0].scatter(s[i].real, s[i].imag, color = 'blue')
    axs[1].scatter(w[i].real, w[i].imag, color='red')


fig, axs = plt.subplots(1, 2, figsize = (16, 8))

# Polos e zeros de F(s)
for pole in np.roots(den):
    axs[0].scatter(pole.real, pole.imag, marker='x', color='red', s=150)
for zero in np.roots(num):
    axs[0].scatter(zero.real, zero.imag, facecolors='none', edgecolors='r', s=150)


# Configurações do gráfico
for ax in axs:
    ax.grid(True)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginário')

axs[0].set_xlim([-5, 3])
axs[0].set_ylim([-4, 4])
axs[0].set_title('Domínio')

axs[1].set_ylim([-35, 35])
axs[1].set_xlim([-25, 45])
axs[1].set_title('Imagem')
axs[1].scatter(0, 0, color='black', s=100)
plt.tight_layout()


# Função animação
ani = animation.FuncAnimation(fig, animate, len(s), interval=100)

# Gerar o gif da animação
#writergif = animation.PillowWriter(fps=10)
#ani.save('animation8.gif', writer=writergif)


plt.show()
