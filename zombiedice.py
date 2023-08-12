'''
ALUNO: SUELEN MARIN MACHADO
PROFESSOR: GALBAS MILLEO FILHO
CURSO: TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
'''
'''
IMPORTS
'''
import random
import os

'''
FACES DOS DADOS DE ACORDO COM A SUA COR
'''
dado_verde = ("Cerebro", "Passos", "Cerebro", "Tiro", "Passos", "Cerebro", "Verde")
dado_amarelo = ("Tiro", "Passos", "Cerebro", "Tiro", "Passos", "Cerebro", "Amarelo")
dado_vermelho = ("Tiro", "Passos", "Tiro", "Cerebro", "Passos", "Tiro", "Vermelho")
tubo_dados = []
'''
VARIÁVEIS QUE SERÃO UTILIZADAS NO DESENVOLVIMENTO DO JOGO
'''
opcao_inicio = 0
em_jogo = False
numero_jogadores = 0
nome_jogadores = []
cerebro_jogadores = []
tiros_rodada = 0
cerebros_rodada = 0
passos_rodada = 0
indice_jogador = 0
dado_cerebros = []
'''
FUNÇÕES UTILIZADAS PARA A MANIPULAÇÃO DOS DADOS
'''


# LIMPA O TERMINAL
def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# TITUO DO JOGO TERMINAL
def Titulo():
    print('''
    Zombie Dice
    ''')


# MENU DE OPÇÕES INICIO DO JOGO
def Menu():
    print('1 - Iniciar Jogo\n2 - Sair\n')


# MENU DE OPÇÕES DURANTE O JOGO
def MenuJogador():
    print('\nDeseja jogar novamente?\n')
    print("1 - Jogar\n2 - Parar\n")


# ESPAÇO ENTRE AS LINHAS
def Espaco():
    print("")


# MOSTRA NO TERMINAL TURNO DO JOGADOR E QUANTIDADE DE CEREBROS
def TurnoJogador(jogador):
    print('Turno de: ', nome_jogadores[jogador])
    print('Total de cérebros: ', cerebro_jogadores[jogador])


# INICIA O JOGO E RETORNA A QUANTIDADE DE JOGADORES
def IniciarJogo(numero_jogadores):
    ClearScreen()
    Titulo()
    while numero_jogadores < 2:

        if numero_jogadores < 2:
            try:
                numero_jogadores = int(input("Por favor, digite o número de jogadores (mínimo 2): "))
            except:
                ClearScreen()
                Titulo()
                print("Por favor, digite um número válido!")

    ClearScreen()
    Titulo()
    for i in range(numero_jogadores):
        nome_jogadores.append(input("Digite o nome do jogador " + str(i + 1) + ": "))

        # DEFINE NOME PADRÃO AOS JOGADORES CASO NÃO SEJA DIGITADO NENHUM
        if nome_jogadores[i] == "":
            nome_jogadores[i] = "Jogador " + str(i + 1)

        cerebro_jogadores.append(0)

    ClearScreen()
    Titulo()
    print("Jogadores: ", nome_jogadores)
    print("Cérebros: ", cerebro_jogadores)
    Espaco()
    input("Pressione enter para continuar...")
    ClearScreen()
    Titulo()

    return numero_jogadores


# RODA O TURNO DO JOGADOR E RETORNA A QUANTIDADE DE CEREBROS, TIROS E PASSOS
def Turno(jogador, tiros_rodada, cerebros_rodada, passos_rodada):
    ClearScreen()
    Titulo()
    TurnoJogador(jogador)
    Espaco()
    print('Pressione Enter para jogar os dados')
    input()
    ClearScreen()
    Titulo()
    TurnoJogador(jogador)
    Espaco()

    # VERIFICA QUANTIDADE DE DADOS NO TUBO E SE NÃO HÁ DADOS, PREENCHE O TUBO COM OS CEREBROS DO JOGADOR JÁ GANHOS
    if (len(tubo_dados) <= 2):
        tubo_dados.append(dado_cerebros)

    if (len(tubo_dados) >= 3):

        # SORTEIA DADO E FACE E SOMA OS RESULTADOS PARCIAIS
        for i in range(3):
            resultado, cor = SorteiaDados()
            if resultado == "Cerebro":
                dado_cerebros.append(cor)
                cerebros_rodada += 1
                cerebro_jogadores[jogador] += 1
            elif resultado == "Tiro":
                tiros_rodada += 1
            else:
                passos_rodada += 1

        if resultado == "Cerebro":
            cerebros_rodada += 1
            cerebro_jogadores[jogador] += 1
        elif resultado == "Tiro":
            tiros_rodada += 1
        else:
            passos_rodada += 1

    # CASO NÃO TENHA DADOS NO TUBO
    else:
        print("Você não tem mais jogadas disponíveis")
        print("Tubo vazio")
        input()

    # MOSTRA OS RESULTADOS DA RODADA
    print("\nDados no tubo: ", len(tubo_dados))
    Espaco()
    print('Tiros do turno: ', tiros_rodada)
    print('Cérebros do turno: ', cerebros_rodada)
    print('Passos do turno: ', passos_rodada)

    # VERIFICA SE O JOGADOR PERDEU A RODADA
    if tiros_rodada >= 3:
        print("\nVocê perdeu o turno por levar 3 tiros ou mais!")
        print("\nPressione enter para continuar...")
        input()
        ClearScreen()
        cerebro_jogadores[jogador] -= cerebros_rodada
        cerebros_rodada = 0
        passos_rodada = 0
        tiros_rodada = -1

    return tiros_rodada, cerebros_rodada, passos_rodada


# PREENCHE O TUBO DE DADOS COM OS DADOS E EMBARALHA
def preencher_tubo_dados():
    for i in range(0, 6):
        tubo_dados.append(dado_verde)
    for i in range(0, 4):
        tubo_dados.append(dado_amarelo)
    for i in range(0, 3):
        tubo_dados.append(dado_vermelho)

    random.shuffle(tubo_dados)


# SORTEIA FACE DO DADO
def SorteiaFace():
    dado = random.randint(0, 5)
    return dado


# SORTEIA DADO DO TUBO E REMOVE ELE
def SorteiaCor():
    dado_aleatorio = random.randint(0, len(tubo_dados) - 1)
    dado_selecionado = tubo_dados.pop(dado_aleatorio)
    return dado_selecionado


# SORTEIA O DADO E RETORNA O RESULTADO, COR DO DADO E A FACE DO DADO
def SorteiaDados():
    face = SorteiaFace()
    cor = SorteiaCor()
    print("Dado: ", cor[6], "-", cor[face])

    # DEVOLVE DADOS COM PASSOS SORTEADOS AO TUBO
    if (cor[face] == "Passos"):
        tubo_dados.append(cor)
        random.shuffle(tubo_dados)

    return cor[face], cor


# VERIFICA SE USURARIO QUER INICIAR JOGO
while numero_jogadores == 0:
    ClearScreen()
    Titulo()
    Menu()

    while opcao_inicio != 1 and opcao_inicio != 2:
        try:
            opcao_inicio = int(input('Digite a opção desejada: '))
        except:
            ClearScreen()
            Titulo()
            Menu()
            print("Por favor, digite um número válido!")

    if opcao_inicio == 1:
        numero_jogadores = IniciarJogo(numero_jogadores)
        ClearScreen()
        Titulo()
        print('Jogo iniciado!')
        Espaco()
        print('Pressione Enter para iniciar o jogo')
        input()
        em_jogo = True
    elif opcao_inicio == 2:
        ClearScreen()
        Titulo()
        print('Jogo encerrado!\n')
        break

# PREENCHE DADOS NO TUBO
preencher_tubo_dados()

# INICIA O JOGO
while em_jogo == True:
    ClearScreen()
    Titulo()
    indice_jogador = 0

    while indice_jogador <= numero_jogadores:

        # VERIFICA SE HÁ VENCEDOR
        for i in range(numero_jogadores):
            if cerebro_jogadores[i] >= 13:
                ClearScreen()
                Titulo()
                print("O vencedor é: ", nome_jogadores[i])
                print("Cérebros: ", cerebro_jogadores[i])
                Espaco()
                print("!!! PARABÉNS !!!\n")
                print("Pressione enter para continuar...")
                input()
                em_jogo = False
                break

        if (em_jogo == False):
            break

        if (tiros_rodada == -1):
            tiros_rodada = 0

        if (indice_jogador == int(numero_jogadores)):
            indice_jogador = 0

        # EXECUTA TURNO
        tiros_rodada, cerebros_rodada, passos_rodada = Turno(indice_jogador, tiros_rodada, cerebros_rodada,
                                                             passos_rodada)

        # VERIFICA SE JOGADOR ESTÁ COM 3 TIROS
        if (tiros_rodada == -1):
            tubo_dados = []
            dado_cerebros = []
            preencher_tubo_dados()
            if (indice_jogador == int(numero_jogadores)):
                indice_jogador = 0
            else:
                indice_jogador += 1

        if (tiros_rodada != -1):
            MenuJogador()
            opcao_incio = 0

            while opcao_incio != 1 and opcao_incio != 2:
                try:
                    opcao_incio = int(input('Digite a opção desejada: '))
                except:
                    print("Por favor, digite um número válido!")

            # JOGADOR REPETE JOGADA
            if opcao_incio == 1:
                ClearScreen()
                Titulo()
                print('Rodada iniciada!')
                Espaco()
                print('Pressione Enter para continuar')
                input()

            # RESETA E PASSA A VEZ PARA PROXIMO JOGADOR
            elif opcao_incio == 2:
                ClearScreen()
                Titulo()
                print('Rodada encerrada!\n')
                print('Resultado final da rodada:\n')
                print("Jogador", nome_jogadores[indice_jogador])
                print("Cérebros: ", cerebro_jogadores[indice_jogador])
                Espaco()
                print('Pressione Enter para continuar')
                input()
                tubo_dados = []
                dado_cerebros = []
                preencher_tubo_dados()
                if (indice_jogador == numero_jogadores):
                    indice_jogador = 0
                else:
                    indice_jogador += 1
                tiros_rodada = 0
                cerebros_rodada = 0
                passos_rodada = 0

print("Fim de jogo\n")