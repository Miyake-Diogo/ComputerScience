"""
Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como
parâmetro e devolve o maior número primo menor ou igual ao número passado à função

Exemplos de execução no shell do Python:

maior_primo(100)
97
maior_primo(7)
7

DICA:
escreva uma função é Primo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não;
se for, guarde numa variável. Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.
"""

def e_primo(valor):
    divisores = 0
    for divisor in range(1, valor):
        if valor % divisor == 0:
            divisores = divisores + 1
        if divisores > 1:
            break
    if divisores > 1:
        return False
    else:
        return True


def maior_primo(n):
    primo = n
    i = 0
    while i <= n:
        if e_primo(i):
            primo = i
        i = i + 1
    return print(primo)

# print(maior_primo(100))