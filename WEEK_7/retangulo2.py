"""
Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
de forma que os caracteres que não estiverem na borda do retângulo sejam espaços.

Por exemplo:
digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##

"""

l = int(input("digite a largura: "))
a = int(input("digite a altura: "))

i=1
while(i <= a):
    j = 1
    while(j <= l):
        if(i == 1) or (i == a):
            print('#',end='')
        else:
            if(j == 1) or (j == l):
                print('#', end='')
            else:
                print(' ',end='')
        j = j + 1
    print('')
    i = i + 1