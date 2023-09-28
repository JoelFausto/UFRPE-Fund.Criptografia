# Atividade: Crie uma função que realize o cálculo de uma exponenciação modular.

def exponeciacao_modular(base, expoente, n):
    result = 1
    
    while expoente > 0:
        if expoente % 2 == 1:
            result = (result * base) % n
        expoente //= 2
        base = (base * base) % n
    
    resultado = result % n

    return resultado