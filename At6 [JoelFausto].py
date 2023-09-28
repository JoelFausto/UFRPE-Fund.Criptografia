# Aprendendo sobre o compartilhamento de senhas.

import random as rd

# MDC - Recursivo
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

# Exponencial Modular
def expMod(base, expoente, n):
    result = 1
    
    while expoente > 0:
        if expoente % 2 == 1:
            result = (result * base) % n
        expoente //= 2
        base = (base * base) % n
    
    resultado = result % n

    return resultado

# Pequeno Teorema de Fernant
def primo(num, t, modo):
    prob = 1/2
    for _ in range(t):
        a = rd.randint(2, num-1)
        while mdc(a, num) != 1:
            a = rd.randint(2, num-1)
        if expMod(a, num - 1, num) != 1:
            if modo == "N":
                return "Não é primo"
            else:
                return False
        prob /= 2

    if modo == "N":
        return f"É primo com probabilidade {prob}!"
    else:
        return True
    
def shareKeys(s, p1, p2, p3, p4):
    primos = [p1, p2, p3, p4]
    restos = [(s % p) for p in primos]
    
    M = p1 * p2 * p3 * p4

    a = (restos[0] * expMod(M/p1, p1 - 2, p1)) % p1
    b = (restos[1] * expMod(M/p2, p2 - 2, p2)) % p2
    c = (restos[2] * expMod(M/p3, p3 - 2, p3)) % p3
    d = (restos[3] * expMod(M/p4, p4 - 2, p4)) % p4

    senha = (((M * a) / p1) + ((M * b) / p2) + ((M * c) / p3) + ((M * d) / p4)) % M

    return f"Senha dada: {s}, senha encontrada: {senha}"

print(shareKeys(100, 23, 17, 59, 73))