import matplotlib.pyplot as plt
import numpy as np

def bissection_sqrt(target, epsilon=0.001):    
    """
    Encontra a raiz quadrada de um número usando o método da bissecção.

    Parâmetros:
    - target: O número cuja raiz quadrada queremos encontrar.
    - epsilon: A precisão desejada para a resposta.

    Retorna:
    - A raiz quadrada aproximada do número target.
    """

    # Definir os limites iniciais do intervalo
    low = 0.0
    high = max(1.0, target)

    # Enquanto o intervalo não for suficientemente pequeno
    while high - low > epsilon:
        # Escolher o ponto médio do intervalo
        mid = (low + high) / 2.0

        # Calcular o valor da função no ponto médio
        square = mid * mid

        # Atualizar os limites do intervalo
        if square > target:
            high = mid
        else:
            low = mid

    # Retornar o valor aproximado da raiz quadrada
    return (low + high) / 2.0

if __name__=='__main__':
    # Intervalo de valores para o eixo x
    x = np.linspace(0, 10, 100)

    # Lista para armazenar os valores da função no eixo y
    y = []

    # Calcular os valores da função para cada ponto do eixo x
    for num in x:
        value=bissection_sqrt(num)
        if num==9:
            print(num, value)
        y.append(value)

    # Plotar o gráfico
    plt.scatter(1, 1, color='black')
    plt.scatter(4, 2, color='black')
    plt.scatter(9, 3, color='black')
    plt.plot(x, y)
    plt.xlabel('Número')
    plt.ylabel('Raiz Quadrada Aproximada')
    plt.title('Método da Bissecção - Raiz Quadrada Aproximada')
    plt.grid(True)
    plt.show()

# Código comentado é muito bom para não se esquecer nada quando se estuda
# Devo fazer isso mais vezes quando não estudo também