"""
Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve

'Fizz' se o número for divisível por 3 e não for divisível por 5;

'Buzz' se o número for divisível por 5 e não for divisível por 3;

'FizzBuzz' se o número for divisível por 3 e por 5;

Caso o número não seja divisível 3 e também não seja divisível por 5, ela deve devolver o número recebido como parâmetro.

Exemplos de execução no Python Shell

fizzbuzz(3)
"Fizz"
fizzbuzz(5)
"Buzz"
fizzbuzz(15)
"FizzBuzz"
fizzbuzz(4)
4
"""
def fizzbuzz(entrada):
    if (entrada % 3 == 0 and entrada % 5 == 0):
        resultado = "FizzBuzz"
    elif (entrada % 3 == 0):
        resultado = "Fizz"
    elif(entrada%5 == 0):
        resultado = "Buzz"

    else:
        resultado = entrada
    return resultado