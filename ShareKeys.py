'''
Algotirmo 1 (Compartilhar a senha): Crie um algoritmo que:

- Recebe o número de algarismos dos números que ser são gerados (vou chamar de n);
- O número de pessoas que vão compartilhar essa senha (vou chamar de p);
- Gerar uma senha S com n algarismos (mas não mostra essa senha);
- Gera o número a1 com n algarismos;
- Depois gera um número a2 que tem n algarismos e verifica se mdc(a1, a2) = 1;
- Depois gera um número a3 que tem n algarismos e verifica se ele tem mdc igual a 1 com cada um dos anteriores;
- Depois gera um número a4 que tem n algarismos e verifica se ele tem mdc igual a 1 com cada um dos anteriores;
- Repete esse processo até gerar a1, a2, . . . , ap;
- Calcula a parte da senha que corresponde a cada pessoa.
- Pessoa k: (ak, sk), sendo sk = S%ak
- O algoritmo retorna todos os pares (ak, sk).
'''

import random
import math

def gerar_numero_algarismos(n):
    return random.randint(10 ** (n - 1), 10 ** n - 1)

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

n = int(input("Quantos algorismos deve ter o número gerado? ")) # número de algarismos
p = int(input("Será dividos em quantas pessoas? ")) # número de pessoas

senha = gerar_numero_algarismos(n)

a = [gerar_numero_algarismos(n)]
s = []

while len(a) < p:
        x = gerar_numero_algarismos(n)
        coprimo = True
        for c in a:
            if mdc(c, x) != 1:
                coprimo = False
                break
        if coprimo:
            a.append(x)

for i in range(p):
  s.append(senha % a[i])

for c in range(p):
  print('Pessoa',c,': ',a[c], ',', s[c])

'''
Algotirmo 2 (Recuperar a senha): Crie um algoritmo que:
- Recebe os pares (ak, sk) gerados pelo algoritmo anterior e, utilizando o método descrito anteriormente, calcula a senha original S. Esse algoritmo deve retornar a senha S.
'''

def euclidiano_extendido(a, b):
    # Algoritmo euclidiano extendido para encontrar o inverso multiplicativo de 'a' módulo 'b'
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = euclidiano_extendido(b % a, a)
        return (g, x - (b // a) * y, y)

def shareKeys(p, r):
    pessoas = p
    restos = r
    M = 1

    for m in range(len(p)):
        M = M * pessoas[m]

    partes = []
    for x in range(len(p)):
        _, inv, _ = euclidiano_extendido(M // pessoas[x], pessoas[x])
        n = (restos[x] * inv) % pessoas[x]
        partes.append(n)

    key = 0
    for i in range(len(p)):
        key += ((M * partes[i]) // pessoas[i])
    key = key % M

    return key

print('')
print(f"A senha era: {shareKeys(a, s)}")