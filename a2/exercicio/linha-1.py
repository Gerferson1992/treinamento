string_1 = input( "informe quantas letras tem:" )
string_2 = input( "Informe quantas letras tem:" )
tamanho_str_1 = len(string_1)
tamanho_str_2 = len(string_2)
print(string_1 + ":"  + str(tamanho_str_1))
print(string_2 + ":"  + str(tamanho_str_2))
stringiguais = string_1 == string_2
print("string 1 é " + ('igual a string 2' if stringiguais else "diferente string 2"))