import json

def salvar_dicionarios(dicionario, nome_do_arquivo):
    """
    Função que salva os dicionarios principais do código em arquivos '.json'.
    """
    with open(f'{nome_do_arquivo}.json', 'w') as file:
        json.dump(dicionario, file)
        
def pegar_dicionario(nome_do_arquivo):
    """
    Função que carrega os dicionarios principais do codigo que estão salvos em arquivos '.json'.
    """
    with open(f'{nome_do_arquivo}.json', 'r') as file:
        return json.load(file)

placar = pegar_dicionario('placar')

tabuleiro = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
]

jogador = 'O'

jogo = True

def adicionar_tabuleiro(tabuleiro, indice, jogador):
    tabuleiro[indice] = jogador

def mudar_jogador():
    global jogador
    if jogador == 'O':
        jogador = 'X'
    else:
        jogador = 'O'

def mostrar_tabuleiro():
    print(f'\n{tabuleiro[:3]}')
    print(tabuleiro[3:6])
    print(f'{tabuleiro[6:9]}\n')

def mostrar_placar(dicionario):
    return (f'---- Jogador X: {dicionario["Jogador X"]} - Jogador O: {dicionario["Jogador O"]} ----')


def valor_valido(valor):
    if valor.isnumeric():
        if valor in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return True
    
    return False

def checar_casa(tabuleiro, casa):
    if tabuleiro[casa] in 'OX':
        return False

    return True

def ver_quem_ganhou(tabuleiro):
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
        return True
    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
        return True
    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
        return True
    
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        return True
    
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        return True

    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        return True
    
def reiniciar_tabuleiro():
    global tabuleiro
    tabuleiro = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9'
]
    
def continuar_jogo():

    while True:
        continuar = input('>>> Deseja continuar a partida [s]im ou [n]ão: ')
        if continuar in 'sS':
            return True
        elif continuar in 'nN':
            return False
        else:
            print('\n--- Valor invalido ----')
def menu():
    jogo = True

    while jogo:
        print(f'\n{mostrar_placar(placar)}')
        reiniciar_tabuleiro()

        mostrar_tabuleiro()

        contador = 0

        while True:

            if contador == 9:
                print('\n===== O Jogo deu velha! =====\n')
                if continuar_jogo():
                    break
                else:
                    print(f'\n{mostrar_placar(placar)}')
                    jogo = False
                    break

            print(f'\n------ Vez do jogador {jogador} ------\n')

            casa = input('>>> Digite em qual casa deseja jogar: ')

            if valor_valido(casa):
                indice = int(casa) - 1

                if checar_casa(tabuleiro, indice):
                    adicionar_tabuleiro(tabuleiro, indice, jogador)
                    mostrar_tabuleiro()
                    if ver_quem_ganhou(tabuleiro):
                        print(f'==== JOGADOR {jogador} GANHOU! =====')
                        valor = placar[f'Jogador {jogador}']
                        placar[f'Jogador {jogador}'] = valor + 1
                        salvar_dicionarios(placar, 'placar')
                        if continuar_jogo():
                            break
                        else:
                            print(f'\n{mostrar_placar(placar)}')
                            jogo = False
                            break
                    mudar_jogador()
                    contador += 1
                else:
                    print('\n---- Essa casa já foi jogada! -----')
                    continue
            
            else:
                print('\n--- Valor Invalido! ---')

menu()