"""
Exercício 2

Este é o desafio do vídeo "Entrada de Dados".

Reescreva o programa contaSegundos para imprimir também a quantidade de dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, "quebre" esse valor em dias, horas, minutos e segundos. A saída deve estar no formato: a dias, b horas, c minutos e d segundos. Seja cuidadoso com o formato! Espaços a mais, vírgulas faltando ou outras diferenças são considerados erro

Abaixo um exemplo de como deve ser a entrada e saída de dados do programa:

Exemplo:

    Entrada de Dados:

Por favor, entre com o número de segundos que deseja converter: 178615

    Saída de Dados:

2 dias, 1 horas, 36 minutos e 55 segundos.

"""
segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segundos = int(segundos)

dias = total_segundos // 86400
dias_restantes = total_segundos % 86400

horas = dias_restantes // 3600
horas_restantes = dias_restantes % 3600

minutos= horas_restantes // 60
segundos_restantes = horas_restantes % 60


print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")