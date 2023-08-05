# Funçao que encripta a palavra informada
def encrypt(word):
  # Elemento base (palavra vazia)
  length = len(word)
  if length == 0:
    return ""

  # Determina o index para a letra encriptada
  index = (ord(word[0])-97+5)%26
  
  #Encripta a letra  
  encryptedLetter = chr(index + 97)
  #Realiza a chamada do caso base eliminando a primeira letra 
  return encryptedLetter + encrypt(word[1:])


# Funçao que decripta a palavra informada 
def decrypt(word):
  # Elemento base (palavra vazia)
  length = len(word)
  if length == 0:
    return ""

  # Determina o index para a letra encriptada
  index = (ord(word[0])-97-5)

  # Realiza o mapeamento para quando o index é maior que o alfabeto ou menor
  if index > 26:
    index = index-26
  elif index < 0:
    index = 26-abs(index)

  # Encripta a letra
  encryptedLetter = chr(index + 97)
  # Realiza a chamada do caso base eliminando a primeira letra
  return encryptedLetter + decrypt(word[1:])

palavra = encrypt('tavalendonotadez')
print("Palavra criptografada: ",palavra)

print("Palavra criptografada: ",decrypt(palavra))

# Projeto realizado por Elvis Claudino, Gabriel Fasolim e Murilo Analiel
# Apresentação: https://www.youtube.com/watch?v=PlssPtJKa24