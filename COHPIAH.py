# %%

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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    soma = 0
    for i in range(6):
        x = abs(as_a[i] - as_b[i])
        soma += x
    
    return soma / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []

    for sentenca in sentencas:
        fs = separa_frases(sentenca)
        frases.extend(fs)
        for frase in fs:
            palavras.extend(separa_palavras(frase))

    # Tamanho médio de palavra (WAL)
    soma_tam_palavras = sum(len(p) for p in palavras)
    wal = soma_tam_palavras / len(palavras)

    # Relação Type-Token (TTR)
    ttr = n_palavras_diferentes(palavras) / len(palavras)

    # Hapax Legomana (HLR)
    hlr = n_palavras_unicas(palavras) / len(palavras)

    # Tamanho médio de sentença (SAL)
    soma_tam_sentencas = sum(len(s) for s in sentencas)
    sal = soma_tam_sentencas / len(sentencas)

    # Complexidade média da sentença (SAC)
    sac = len(frases) / len(sentencas)

    # Tamanho médio de frase (PAL)
    soma_tam_frases = sum(len(f) for f in frases)
    pal = soma_tam_frases / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_similaridade = float('inf')
    texto_mais_proximo = 0

    for i, texto in enumerate(textos):
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)

        if similaridade < menor_similaridade:
            menor_similaridade = similaridade
            texto_mais_proximo = i + 1  # +1 pois queremos do texto 1 até n

    return texto_mais_proximo
