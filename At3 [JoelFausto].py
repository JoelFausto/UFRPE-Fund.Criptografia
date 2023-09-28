# 1° Questão
# Escreva uma função em Python que recebe um texto limpo, isto  ́e, sem acentos nem números e nem caracteres especiais e, em seguida, cifra esse texto utilizando a cifra de deslocamento.

# Entrada: Mensagem (texto limpo) m e uma chave k ∈ {1, 2, · · · , 25}.
# Saída: Texto cifrado apenas.

# Observação: Como a forma de cifrar e de decifrar para a Cifra de Deslocamento são idênticas, mudando apenas o sinal da chave, não ́e necessário implementar uma função de decriptação.

def limpaTexto(mensagem):

  alfabeto = ["a", "A", "b", "B", "c", "C", "d", "D", "e", "E", "f", "F", "g", "G", "h", "H", "i", "I", "j", "J", "k", "K", "l", "L", "m", "M", "n", "N", "o", "O", "p", "P", "q", "Q", "r", "R", "s", "S", "t", "T", "u", "U", "v", "V", "w", "W", "x", "X", "y", "Y", "z", "Z"]
  textoLimpo = ""

  for i in mensagem:
      if i in alfabeto:
          textoLimpo += i

      # Transformação das vogais com acento e "ç".
      elif i == "á" or i == "à" or i == "â" or i == "ã" or i == "ä":
          textoLimpo += "a"
      elif i == "Á" or i == "À" or i == "Â" or i == "Ã":
          textoLimpo += "A"
      elif i == "é" or i == "è" or i == "ê" or i == "ë":
          textoLimpo += "e"
      elif i == "É" or i == "È" or i == "Ê":
          textoLimpo += "E"
      elif i == "í" or i == "ì" or i == "î" or i == "ï":
          textoLimpo += "i"
      elif i == "Í" or i == "Ì" or i == "Î":
          textoLimpo += "I"
      elif i == "ó" or i == "ò" or i == "ô" or i == "õ" or i == "ö":
          textoLimpo += "o"
      elif i == "Ó" or i == "Ò" or i == "Ô" or i == "Õ":
          textoLimpo += "O"
      elif i == "ú" or i == "ù" or i == "û" or i == "ü":
          textoLimpo += "u"
      elif i == "Ú" or i == "Ù" or i == "Û":
          textoLimpo += "U"
      elif i == "ç":
          textoLimpo += "c"
      elif i == "Ç":
          textoLimpo += "C"

  return textoLimpo

def deslocamento(m, k):
    mensagem = limpaTexto(m)

    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
    criptografado = ""

    for l in mensagem:
        pos =  alfabeto.index(l.upper())
        c = (pos + k) % 26
        criptografado += alfabeto[c]

    return(criptografado)

# 2° Questão
# Escreva uma uma função em Python que recebe um texto cifrado utilizando uma cifra de deslocamento e, através do processo de quebra estudado nesse ḿodulo, 
# encontra a chave que foi utilizada.

# Entrada: Texto cifrado, com cifra de deslocamento, a partir de um texto original escrito em português do Brasil.
# Saída: Chave utilizada para cifrar o texto.

# Observação: Para que o processo de análise de frequência funcione adequadamente, ser ́a necessário utilizar um texto razoavelmente longo. Utilize um com pelo menos MIL letras.
# VocÊ pode copiar algum texto da internet mas fique atento aos acentos e cedilha. Você pode remover manualmente as letras acentuadas (eu não recomento) ou pode melhorar
# o código “Limpar texto” para trocar as letras acentuadas e cedilha pelas mesmas letras sem acentuação.

def analiseFrequencia(c, modo):
    frequencia = {}
    total_caracteres = len(c)

    for caracter in c:
        if caracter in frequencia:
            frequencia[caracter] += 1
        else:
            frequencia[caracter] = 1

    # Adiciona letras ausentes com frequência zero
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letra in alfabeto:
        if letra not in frequencia:
            frequencia[letra] = 0

    if modo == 'p':
        resultado = [round((frequencia[caracter] / total_caracteres), 3) for caracter in alfabeto]
    elif modo == 'c':
        resultado = [frequencia[caracter] for caracter in alfabeto]
    else:
        print("Valor inválido! Use 'p' para porcentagem ou 'c' para contagem.")

    return resultado

def deslocamentoDec(m):

    # Constante I da língua portuguesa
    constant_i_portuguese = 0.073
    # Frequências da língua portuguesa
    P = [0.146, 0.01, 0.039, 0.05, 0.126, 0.01, 0.013, 0.013, 0.062, 0.009, 0.0, 0.028, 0.047, 
         0.044, 0.097, 0.025, 0.012, 0.065, 0.068, 0.043, 0.036, 0.016, 0.0, 0.005, 0.0, 0.005]
    # Frequências do texto cifrado
    Q = analiseFrequencia(m, 'p')

    # Listas das constantes encontradas em cada iteração.
    constant_i_list = []

    for k in range(1, 26):
        sum = 0
        for i in range(1, 26):
            # Cálculo da soma ponderada entre as frequências esperadas. 
            # No final de cada laço de i temos o valor de (Índice) para chave k.
            sum += P[i] * Q[(i + k) % 26]
        constant_i_list.append(round(sum, 3))
    
    correct_constant = 0
    # Busca pela constante I mais próxima da língua portuguesa.
    for j, item in enumerate(constant_i_list):
        sub = abs(constant_i_portuguese - item)
        if j == 0:
            smaller = sub
            correct_constant = item
        if sub < smaller:
            smaller = sub
            correct_constant = item

    key = constant_i_list.index(correct_constant) + 1

    return key

# Exemplo de Uso
mensagem = """Bem, eles são bem legais comigo e essa conversa com certeza me tranquilizou muito, não queria ser um fardo para eles, mas confesso meu pai poderia ser filósofo ele fala 
umas coisas que me deixam quebrando a cabeça por dias para entender seu significado, mas esse não é o ponto aqui, como eu ia dizendo passei esses meses em busca de algo que completasse 
esse vazio que havia na minha vida, eu precisava de um propósito, então eu tentei alguns estágios/trabalhos como: carteiro (trabalho legal eu andava muito de bicicleta, mas acho que não 
sou bom com cachorros), entregador de pizzas (também legal, mas não é nada fácil trabalhar com pizzas sem poder come-las), eletricista (bem, nesse eu nem tenho muito a conversar sobre, 
simplesmente não é pra mim), pedreiro (interessante, mas descobri que não tenho físico pra isso) e até mesmo bombeiro (acho que foi a melhor experiência que tive, o sentimento que tive 
ao salvar um gatinho de uma árvore ou ajudar uma meninha perdida dos pais no parque a encontra-los me fez sentir útil e deu até um quentinho no coração, porém existem certos trabalhos 
para pessoas com “coração forte” e acho que não sou qualificado para essas “missões” e se eu quisesse ser um bombeiro eu deveria enfrentar esses tipos de situações e não decepcionar as 
pessoas ao meu redor, mas não era qualificado para isso, se eu vejo sangue na minha frente eu tenho uma crise de ansiedade de imediato, meus pais dizem que tenho isso desde de pequeno, 
não sei o motivo, mas desde então eu evito), e esse foi meu itinerário nesses últimos tempos. Fora a procura incessável por um objetivo para minha vida eu passava algumas manhãs no 
parque da cidade, amava caminhadas ao ar livre, sentir o ar, respirar fundo, olhar o céu, os pássaros livres voando, isso me fazia bem, podia passar uma vida apenas admirando essas 
pequenas coisas e acho que foi por esse motivo que no dia em questão aconteceu o que aconteceu. Eu estava tão fascinado com a paisagem que nem percebi quando o clima de repente mudou, 
estava um sol brilhante e um céu do mais azul, mas pareceu que em um piscar de olhos o céu ficou nublado e no lugar das brisas tranquilas e revigorantes, começaram ventos bravios 
não sei se você enquanto viajava de carro colocou o rosto para fora e parecia que o ar podia lhe transpassar e lhe deixar em pedaços, bem era esse o nível dos ares naquele momento 
quando me dei conta de imediato tentei voltar para casa, mas pra situação ficar melhor ainda NEVOA! Sim nevoa, serio não sei qual fenômeno aconteceu naquela manhã só sei que o clima
parecia conspirar pra me deixar preso naquele parque. Como teimoso que era eu não me aquietei a ficar “preso” naquela mesma posição e tentei a todo custo sair dali, e por mais difícil 
que fosse eu consegui me mover alguns metros, porém ao olhar para o céu eu via algo brilhante e parecia vir em minha direção, a princípio parecia apenas um brilho pequeno, mas foi 
chegando mais e mais perto e quando consigo finalmente perceber o que era...PUFT! Foi um almoço tranquilo, meus pais e eu conversamos sobre qualquer coisa como era habitual, senão me engano o tópico da vez foi como as mudanças climáticas estavam afetando a vivência 
na Terra é eu sei, conversar sobre coisas assim em pleno almoço!? Mas como eu disse são tópicos aleatórios e acabou que esse foi o do dia, eu e minha família sempre fomos bem 
comunicativos acho que é por isso que temos uma convivência tão legal, além de meus pais, posso dizer que são meus amigos e confidentes, e por isso que naquele almoço eles notaram que 
eu não estava bem, porém conseguir disfarçar puxando uma pergunta sobre o tópico da vez...por sorte não houve nenhuma reclamação ou sermão pelo meu atraso, o que me deixou bem pensativo. A voz estava certa e isso acontecer era mesmo bem raro, minha mãe é o que se pode chamar de “mãe coruja”, sério ela é super preocupada comigo, chegar alguns minutos atrasado da aula já era quase motivo de um “ataque do coração” para ela, então nenhuma reação foi bem inusitado, mas tomei aquilo como uma coincidência eu talvez tivesse imaginado tudo aquilo, isso não seria tão incomum para mim, sempre me dizem que sonho acordado, coisa ao qual eu chamo de imaginação, enfim coloquei na cabeça de esquecer toda aquela “loucura” de momentos atrás, era uma das poucas vezes que guardava algo dos meus pais, para mim não estava escondendo algo, apenas não comentei sobre algo que achei irrelevante, só iria preocupa-los. 
Depois do almoço ajudei minha mãe com alguns afazeres de casa, meio que estava devendo isso a ela pelo meu atraso do almoço e depois passei o resto da tarde maratonando uma série de uma 
garota que tinha uma banda de fantasmas, a noite o de sempre jantar, jogar e cama, mas como se aquele dia não pudesse ser ainda mais estranho eu tive um sonho, foi mais ou menos assim: 
Eu estava de volta no beco e de frente para a porta, os detalhes de ouro agora brilhavam muito e quando olhei para a maçaneta para ver o entalhe que tinha achado tão bonito ele não estava 
mais lá, quando olho para o lado a águia da maçaneta estava ao meu lado, ela não parecia predadora como as dos documentários, pelo contrário parecia doce, bem maior que as comuns, eu pude 
olhar em seus olhos e foi como se visse a projeção da voz em minha frente era o mesmo sentimento, o poder, a calmaria, e por fim o conforto, eu não me sentia assustado, quando me viro para 
a porta novamente me atento há uma luz que vinha por debaixo da porta a princípio era uma luz normal e até pude sentir um vento que vinha de detrás dela que chegava aos meus pés, estava 
tudo tão confortável que não me contenho e coloco mais uma vez a mão sobre a maçaneta para abrir e ver o que tinha por detrás dela, porém assim que estendo minha mão e tento girar a 
maçaneta eu ouço vozes, não era como a voz que havia escutado no beco ao meio-dia daquele dia, na verdade eram várias vozes, que se tornaram gritos de desespero, agonia era como se eu 
pudesse ouvir uma guerra acontecendo por detrás da porta, pude escutar espadas tinindo, arcos sendo empunhados, sons de flechas por todos os lados, mais e mais gritos, explosões, era 
horrível, eu parecia estar dentro de uma guerra mas não enxergava nada, quando não estava mais aguentando ouvir aquilo abaixei a cabeça e coloquei as mãos nos ouvidos, e lembra-se da luz 
e da brisa tranquila que tinha notado anteriormente, agora era um ar sujo, com mal odor e da porta em vez de luz agora estava saindo...sangue! Tentei me afastar a visão do sangue mas ao 
olhar de volta a porta vejo uma serpente na maçaneta da porta, corro a visão para o chão novamente e agora o sangue já estava nos meus pés, nesse momento que vi o sangue acordo de súbito 
com um grito..."""
mensagem_limpa = limpaTexto(mensagem).upper()
mensagem_cifrada = deslocamento(mensagem_limpa, 3)

print(deslocamentoDec(mensagem_cifrada))