# Jogo Nim tarefa semana 6
# Infos no arquivo objetivo week 6


def usuario_escolhe_jogada(n, m):

    print()
    while True:
        num = int(input("Quantas peças você vai tirar? "))

        if num > m or (n - num) < 0:
            print()
            print("Ooperacaos! Jogada inválida! Tente de novo.")
            print()

        else:
            if num < 2:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou", num, "peças.")
            return num

def e_multiplo(n, m):

    achou = False

    if(n % (m+1)) == 0:
        achou = True
    return achou

def computador_escolhe_jogada(n, m):

    print()

    quantidade = 0
    if n <= m:
        quantidade =  n
    else:
        if e_multiplo(n, m):
            quantidade = m
        else:
            computador = 0
            while computador % (m + 1) != n % (m + 1):
                computador = computador + 1
                if computador % (m + 1) == n % (m + 1):
                    quantidade = computador
                    break

    if quantidade < 2:
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou",quantidade,"peças.")
    return quantidade

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if e_multiplo(n, m):
        print()
        print("Voce começa!")
        jogador = 1
    else:
        print()
        print("Computador começa!")
        jogador = 0

    while n > 0:

        if jogador == 0:
            n = n - computador_escolhe_jogada(n, m)
            jogador = 1
        else:
            n = n - usuario_escolhe_jogada(n, m)
            jogador = 0
        if n == 0 and jogador == 0:
            print("Fim do jogo! Você ganhou!")
            break
        elif n == 0 and jogador == 1:
            print("Fim do jogo! O computador ganhou!")
            break

        if n < 2:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam",n,"peças no tabuleiro.")


def campeonato():
    print("\nVoce escolheu um campeonato!\n")
    rodada = 1
    while rodada <= 3:
        print("**** Rodada",rodada," ****")

        print()

        partida()

        print()

        rodada = rodada + 1
    print("**** Final do campeonato! ****\n")
    print("Placar: Você 0 X",(rodada-1),"Computador")



print("Bem-vindo ao jogo do NIM! Escolha:\n")
operacao = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

if operacao == 1:
    print("\nVoce escolheu uma partida isolada\n")
    partida()
elif operacao == 2:
    campeonato()