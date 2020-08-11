"""
Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.

Exemplos de execução no shell de Python

 vogal("a")
True
 vogal("b")
False
 vogal("E")
True

Os valores True e False devolvidos devem ser do tipo bool (booleanos), e não strings

Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.
"""
def vogal(input_string):
    input_string = input_string.lower()
    if((input_string == "a") or (input_string == "e") or (input_string == "i") or (input_string == "o") or (input_string == "u")):
        return True
    else:
        return False
