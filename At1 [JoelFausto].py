# Fundamentos de Criptografia
# At1: Crie uma função em Python que limpe textos sujos, ou seja, uma função que dada uma frase retorne apenas letras.

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

  print(textoLimpo)

limpaTexto("Áçai_12345$%!@RuaJoão")