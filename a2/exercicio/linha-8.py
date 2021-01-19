frase = input('Escreva uma frase: ').upper().replace(' ', '')
expInv = frase[::-1]
if frase == expInv:
    print('É palíndromo, pois {} --> {}.'.format(frase, expInv))
else:
    print('Essa frase nao é um polidromo.')