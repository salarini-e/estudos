import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Função que define a EDO
def myODE(t, y):
    return 2 * t  # Exemplo de EDO: dy/dt = 2t

# Condição inicial
y0 = [0]  # Valor inicial de y

# Intervalo de tempo para a solução
t_span = [0, 5]  # Intervalo de tempo de 0 a 5

# Resolvendo a EDO
sol = solve_ivp(myODE, t_span, y0)

# Extração dos resultados
t = sol.t  # Valores de tempo
y = sol.y[0]  # Valores de y

# Plotando o resultado
plt.plot(t, y)
plt.xlabel('Tempo')
plt.ylabel('y')
plt.title('Solução da EDO dy/dt = 2t')
plt.grid(True)
plt.show()
