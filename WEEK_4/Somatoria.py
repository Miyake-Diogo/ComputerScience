"""
Exercício 3

Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

Exemplo:
Digite um número inteiro: 123
6
"""
numero = int(input("Digite um número inteiro: "))
n = str(numero)
comprimento = len(n)
inicio = 1
soma = 0
while (comprimento >=1):
    a = numero // inicio % 10
    inicio = inicio * 10
    soma = a + soma
    comprimento = comprimento - 1

print(soma)