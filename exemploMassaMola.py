from scipy import signal
import matplotlib.pyplot as plt

# Seja um sistema massa mola que a posição de saída, medida a partir
# da posição de equilibrio, chamemos de y e que a ele seja aplicada uma força 
# externa u. Constante da mola = K, constante de amortecimento = B

# Variaveis
k = 0.03
b = 0.5
m = 10

# eq. do sistema: my'' + by' + ky = u
# var. de estado: x1 = y e x2 = y'
# logo, x1' = x2   ;   x2' = -k/m x1 -b/m x2 + 1/m u   ;   y = x1
# sendo, x' = Ax + Bu   ;   y = Cx + Du

A = [[0.0, 1.0], [-k/m, -b/m]]
B = [[0], [1/m]]
C = [1.0, 0.0] 
D = [0.0]

sys = signal.StateSpace(A,B,C,D)
t, y = signal.step(sys)
plt.plot(t,y)
plt.show()

# Observando os gráficos para a entrada em degrau, vemos que aumentando a 
# constante de amortecimento b, estamos diminuindo o overshoot do gráfico.
# Quando aumentamos a massa do sistema, estamos aumentando a frequência de
# oscilação do sistema antes de parar