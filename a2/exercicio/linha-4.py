nome = input("Digite seu nome:" )
tamanho_nome = len(nome)
contador = tamanho_nome
while(contador > -1):
  print(nome[contador:])
  contador = contador -1