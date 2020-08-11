"""
Exercício 5 - Verificando ordenação

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
"""
entrada = int(input())
entrada2 = int(input())
entrada3 = int(input())

if(entrada < entrada2 and entrada2 < entrada3):
    print("crescente")
else:
    print("não está em ordem crescente")