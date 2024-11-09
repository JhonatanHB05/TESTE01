#VERIFICANDO SE UM NUMERO PERTENCE OU NÃO A SEQUÊNCIA DE FIBONACCI
#INDICAÇAO DE UM NUMERO PELO USUARIO
NUMERO = int(input("Insira um numero, para verificar se está na sequência de Fibonacci: "))
#CONFERINDO SE O NUMERO ESTA NA SEQUÊNCIA DE FIBONACCI
a, b = 0, 1
fibonacci_encontrado = False
#CRIANDO UMA REPETIÇAO DE VERIFICAÇÃO
while a <= NUMERO:
    if a == NUMERO:
        fibonacci_encontrado = True
        break
    a,b = b, a + b
#IMPRIMINDO O RESULTADO
if fibonacci_encontrado:
    print(f"O número {NUMERO}, pertence a sequencia de Fibonacci.")
else:    
    print(f"O número {NUMERO}, nao pertence a sequencia de Fibonacci")
#FIM DO PROGRAMA
