# Atividade - Cifra Clássica: Implementar algumas das chamadas "Cifras clássicas".

def baconianCipher(mensagem):

    tabela_cifra = {
        'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
        'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaaa',
        'K': 'abaab', 'L': 'ababa', 'M': 'ababb ', 'N': 'abbaa', 'O': 'abbab',
        'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
        'U': 'baabb', 'V': 'baabb', 'W': 'babaa', 'X': 'babab', 'Y': 'babba',
        'Z': 'babbb'
    }

    cifra = ""
    for l in mensagem:
        if l.isalpha():
            cifra += tabela_cifra.get(l.upper(), '')
        else:
            cifra += l

    return cifra

def baconianDecipher(cifra):

    tabela_decifra = {
        'aaaaa': 'A', 'aaaab': 'B', 'aaaba': 'C', 'aaabb': 'D', 'aabaa': 'E',
        'aabab': 'F', 'aabba': 'G', 'aabbb': 'H', 'abaaa': 'I', 'abaaa': 'J',
        'abaab': 'K', 'ababa': 'L', 'ababb': 'M', 'abbaa': 'N', 'abbab': 'O',
        'abbba': 'P', 'abbbb': 'Q', 'baaaa': 'R', 'baaab': 'S', 'baaba': 'T',
        'baabb': 'U', 'baabb': 'V', 'babaa': 'W', 'babab': 'X', 'babba': 'Y',
        'babbb': 'Z'
    }

    descriptado = ""

    for l in range(0, len(cifra), 5):
        descriptado += tabela_decifra[cifra[l:l+5]]

    return descriptado

print((baconianCipher("Joel")))
