def calcular_derivada(f, x, h=1e-6):
    """
    Calcula a derivada de uma função f em um ponto x usando o método das diferenças finitas.

    Argumentos:
    f: Função para a qual deseja-se calcular a derivada.
    x: Ponto no qual a derivada será calculada.
    h: Tamanho do incremento utilizado para calcular as diferenças finitas (opcional, padrão: 1e-6).

    Retorna:
    O valor aproximado da derivada de f em x.
    """
    df = (f(x + h) - f(x)) / h
    return df

if __name__=='__main__':
    
    def f(x):
        return x**2

    x = 2  # Ponto onde queremos calcular a derivada

    derivada = calcular_derivada(f, x)
    print(f"A derivada de f em x = {x} é: {derivada}")
