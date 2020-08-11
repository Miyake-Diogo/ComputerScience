"""
Escreva um programa que recebe como entradas (utilize a função input) dois números inteiros correspondentes à
largura e à altura de um retângulo, respectivamente.
O programa deve imprimir uma cadeia de caracteres que represente
o retângulo informado com caracteres '#' na saída.

Por exemplo:

digite a largura: 10
digite a altura: 3
##########
##########
##########

Dica: lembre-se que a função print pode receber um parametro 'end', que altera o último caractere da cadeia,
tornando possível a remoção da quebra de linha (reveja as vídeo-aulas)
"""
l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

i=j=0
while i < a:
    while j <= l-1:
        print("#", end="")
        j = j+1
    i = i + 1
    print("", end="\n")
    j=0


