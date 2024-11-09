#SOLICITAR UMA STRING
string = input("Digite uma string para ser invertida: ")

#iNICIALIZA A STRING INVERTIDA
string_invertida = ""

#INVERSAO DA STRING
for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print("String invertida:", string_invertida)
#FIM DO PROGRAMA