# Atividade - Cifra Clássica: Implementar algumas das chamadas "Cifras clássicas".

def railFenceCipher(m, num_rails):
    # Cria uma lista de trilhos vazios
    rails = [[] for _ in range(num_rails)]
    
    rail = 0
    direction = 1  # Direção: 1 para baixo, -1 para cima
    
    for char in m:
        rails[rail].append(char)
        rail += direction
        
        # Inverte a direção quando atingir as bordas dos trilhos
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    # Concatena os trilhos em uma única lista
    criptografado = sum(rails, [])
    
    return "".join(criptografado)

def railFenceDecipher(criptografado, num_rails):
    # Cria uma lista de trilhos vazios
    rails = [[] for _ in range(num_rails)]
    
    rail = 0
    direction = 1  # Direção: 1 para baixo, -1 para cima
    
    for _ in range(len(criptografado)):
        # Marca a posição atual com um asterisco para facilitar o preenchimento posterior
        rails[rail].append('*')
        rail += direction
        
        # Inverte a direção quando atingir as bordas dos trilhos
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    # Preenche os asteriscos com os caracteres do texto cifrado
    index = 0
    for rail in rails:
        for i in range(len(rail)):
            if rail[i] == '*':
                rail[i] = criptografado[index]
                index += 1
    
    # Reconstrói o texto original seguindo o padrão de leitura dos trilhos
    decriptado = ""
    rail = 0
    direction = 1
    
    for _ in range(len(criptografado)):
        decriptado += rails[rail].pop(0)
        rail += direction
        
        # Inverte a direção quando atingir as bordas dos trilhos
        if rail == 0 or rail == num_rails - 1:
            direction *= -1
    
    return decriptado

# Exemplo de uso
mensagem = "defendtheeastwallofthecastle"

cifra = railFenceCipher(mensagem, 3)
print(cifra)
decifrado = railFenceDecipher(cifra, 3)
print(decifrado)
