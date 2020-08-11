"""
Exercício 1

Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
Se o número for primo, imprima "primo". Caso contrário, imprima "não primo".

Exemplos:

Digite um número inteiro: 13
primo

Digite um número inteiro: 12
não primo

"""
valor = int(input("Digite um número inteiro: "))
count = 0
i = 0

while i <= valor or count < 2 :
    i = i+ 1
    x = valor% i
    if x == 0:
        count = count + 1
    if count <= 2:
        numero = "primo"
    else:
        numero = "não primo"

print(numero)