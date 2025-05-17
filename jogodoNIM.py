# %%

def computador_escolhe_jogada(n, m):
    if n % (m + 1) != 0:
        return n % (m + 1)
    elif n <= m:
        return n
    else:
        return m

def usuario_escolhe_jogada(n, m):
    retirar = int(input("Quantas peças deseja retirar? "))
    
    while retirar < 1 or retirar > m:
        print("Oops! Jogada inválida! Tente de novo.")
        retirar = int(input("Quantas peças deseja retirar? "))
        
    return retirar

def partida(n, m):
    print(f"\nComeçando a partida com {n} peças e limite de {m} por jogada.")

    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_usuario = True
        
    else:
        print("Computador começa!")
        vez_do_usuario = False

    while n > 0:
        print(f"\nRestam {n} peça(s) na pilha.")

        if vez_do_usuario:
            retirar = usuario_escolhe_jogada(n, m)
            print(f"Você retirou {retirar} peça(s).")
        else:
            retirar = computador_escolhe_jogada(n, m)
            print(f"O computador retirou {retirar} peça(s).")

        n = n - retirar
        vez_do_usuario = not vez_do_usuario

    if vez_do_usuario:
        print("\nO computador ganhou!")
        return "computador"
    else:
        print("\nVocê ganhou!")
        return "usuario"

def campeonato():
    usuario_pontos = 0
    computador_pontos = 0

    print("\nVocê escolheu um campeonato! Serão 3 partidas.")

    for rodada in range(1, 4):
        print(f"\n**** Rodada {rodada} ****")

        n = int(input("Quantas peças? "))
        while n <= 0:
            print("Escolha um número válido.")
            n = int(input("Quantas peças? "))

        m = int(input("Limite de peças por jogada? "))
        while m <= 0 or m > n:
            print("Escolha um número válido.")
            m = int(input("Limite de peças por jogada? "))

        vencedor = partida(n, m)

        if vencedor == "usuario":
            usuario_pontos += 1
        else:
            computador_pontos += 1

        print(f"\nPlacar: Você {usuario_pontos} x {computador_pontos} Computador")

    print("\n**** Final do campeonato! ****")
    print(f"Placar final: Você {usuario_pontos} x {computador_pontos} Computador")

# Principal ↓

print("""
Bem-vindo ao jogo do NIM! Escolha:
1 - para jogar uma partida isolada
2 - para jogar um campeonato
""")

tipo = input()

if tipo == "1":
    print("Você escolheu uma partida isolada!")

    n = int(input("Quantas peças? "))
    while n <= 0:
        print("Escolha um número válido.")
        n = int(input("Quantas peças? "))

    m = int(input("Limite de peças por jogada? "))
    while m <= 0 or m > n:
        print("Escolha um número válido.")
        m = int(input("Limite de peças por jogada? "))

    partida(n, m)

elif tipo == "2":
    campeonato()

else:
    print("Digite uma opção válida!")
