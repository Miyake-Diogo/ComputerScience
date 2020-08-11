"""
Exercício 2

Receba um número inteiro positivo na entrada e imprima os n n n primeiros números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.

Exemplo:
Digite o valor de n: 5
1
3
5
7
9
"""
numero = int(input("Digite o valor de n: "))
i = 1
while(numero >= 1):
    print(i)
    i = i + 2
    numero = numero -1