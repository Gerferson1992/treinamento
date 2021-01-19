nome = input("DIGITE SEU NOME:")
tamanho_nome = len(nome)
contador = tamanho_nome
while(contador > 0):
	print(nome[0:contador])
	contador = contador -1