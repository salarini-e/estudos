import numpy as np
import matplotlib.pyplot as plt

# Parâmetros da simulação
dt = 0.01  # Passo de tempo
t_max = 10.0  # Tempo máximo da simulação

# Vetores para armazenar os valores de tempo, posição e velocidade
t = np.arange(0.0, t_max, dt)
x = np.zeros_like(t)
v = np.zeros_like(t)

# Condições iniciais
x[0] = 0.0  # Posição inicial
v[0] = 1.0  # Velocidade inicial

# Simulação do movimento
for i in range(1, len(t)):
    x[i] = x[i-1] + v[i-1] * dt
    v[i] = v[i-1] - x[i-1] * dt

# Plotando o resultado
plt.plot(t, x, label='Posição')
plt.plot(t, v, label='Velocidade')
plt.xlabel('Tempo')
plt.ylabel('Valor')
plt.title('Simulação de Movimento')
plt.legend()
plt.grid(True)
plt.show()
