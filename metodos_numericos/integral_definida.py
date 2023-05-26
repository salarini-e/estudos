def calcular_integral_definida(f, a, b, n=1000):
    """
    Calcula a integral definida de uma função f no intervalo [a, b] usando o método do trapézio.

    Argumentos:
    f: Função que será integrada.
    a: Limite inferior do intervalo de integração.
    b: Limite superior do intervalo de integração.
    n: Número de subintervalos (opcional, padrão: 1000).

    Retorna:
    O valor aproximado da integral definida de f no intervalo [a, b].
    """
    h = (b - a) / n  # Tamanho de cada subintervalo
    soma = 0.5 * (f(a) + f(b))  # Primeiro e último termo da soma

    for i in range(1, n):
        x = a + i * h
        soma += f(x)

    integral = h * soma
    return integral

if __name__=='__main__':
    def f(x):
        return x**2

    a = 0  # Limite inferior do intervalo de integração
    b = 1  # Limite superior do intervalo de integração

    integral = calcular_integral_definida(f, a, b)
    print(f"A integral definida de f no intervalo [{a}, {b}] é: {integral}")
