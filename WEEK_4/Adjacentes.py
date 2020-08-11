"""
Exercício 2 - Desafio do vídeo "Repetição com while"

Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito com um dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir, imprima "não".

Exemplos:

Digite um número inteiro: 12345
não

Digite um número inteiro: 1011
sim
"""

valor = int(input("Digite um número inteiro: "))
adjacentes = False
anterior = valor % 10
valor = valor // 10

while valor > 0 and not adjacentes:
    atual = valor % 10
    valor = valor // 10
    if atual == anterior:
        adjacentes = True
    anterior = atual

if adjacentes:
    print("sim")
else:
    print("não")