
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        print("Não é permitido dividir por zero!")
        return None
    else:
        return a / b
    