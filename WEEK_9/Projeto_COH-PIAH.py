import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    ''' Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    compara = (sum([abs(x - y) for x, y in zip(as_a, as_b)]) / len(as_b))
    return compara


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)

    frases = []
    palavras = []

    soma_sentenca = 0
    soma_palavra = 0
    soma_caracteres_frase = 0

    for sentenca in sentencas:
        soma_sentenca = soma_sentenca + len(sentenca)
        comprimento_frase = separa_frases(sentenca)

        for f in comprimento_frase:
            frases.append(f)

    for frase in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(frase)
        comprimento_palavra = separa_palavras(frase)

        for palavra in comprimento_palavra:
            palavras.append(palavra)

    for palavra in palavras:
        soma_palavra = soma_palavra + len(palavra)

    palavras = separa_palavras(texto)

    media_palavras = soma_palavra/len(palavras)
    rel_type_token = n_palavras_diferentes(palavras)/len(palavras)
    hapax = n_palavras_unicas(palavras)/len(palavras)
    medio_sentencas = soma_sentenca / len(sentencas)
    compara_sentenca = len(frases) / len(sentencas)
    tamanho_medio_frase = soma_caracteres_frase / len(frases)

    lista_final = [media_palavras, rel_type_token, hapax, medio_sentencas, compara_sentenca, tamanho_medio_frase]

    return lista_final



def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        assinaturas.append(ass_texto)

    coh_piah = []
    for assinatura in assinaturas:
        coh_piah.append(compara_assinatura(assinatura, ass_cp))

    return coh_piah.index(min(coh_piah)) + 1


# Iniciar o programa
def main():
    assinatura = le_assinatura()
    textos = le_textos()
    compara = avalia_textos(textos, assinatura)
    print(f"O autor do texto {compara} está infectado com COH-PIAH")