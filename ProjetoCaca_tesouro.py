import numpy as np
import os

print('-------- Caça Ao Tesouro --------')

#----------------------------------------------------------------------- dicionários de movimento
dificuldade = {
    'facil': [np.random.randint(3,5), np.random.randint(3,5)],
    'medio': [np.random.randint(5,7), np.random.randint(5,7)],
    'dificil': [np.random.randint(8,10), np.random.randint(8,10)],
    'f': [np.random.randint(3,5), np.random.randint(3,5)],
    'm': [np.random.randint(5,7), np.random.randint(5,7)],
    'd': [np.random.randint(8,10), np.random.randint(8,10)],
}

movimentacao = {
    'cima': [-1, 0],
    'baixo': [1, 0],
    'esquerda': [0, -1],
    'direita': [0, 1],
    'c': [-1, 0],
    'b': [1, 0],
    'e': [0, -1],
    'd': [0, 1]
}

#----------------------------------------------------------------------- definicao de dificuldade
while True:
    valor_dificuldade = input('Pretende jogar no (F)acil, (M)edio ou (D)ificil? ').lower()
    if valor_dificuldade not in dificuldade:
        print('Valor inválido!')
    else:
        break

#----------------------------------------------------------------------- variáveis
mapa = np.random.randint(10, 99, tuple(dificuldade[valor_dificuldade]))
local_atual = (0, 0)
score = 1000
contador = 0
jogador = -1
nvl_dificuldade = mapa.size

linha = np.random.randint(0, mapa.shape[0])
coluna = np.random.randint(0, mapa.shape[1])
if linha == 0 and coluna == 0:
    coluna = np.random.randint(1, mapa.shape[1])
tesouro = (linha, coluna)

#----------------------------------------------------------------------- controle de area do mapa
def esta_no_mapa(local, movimento, mapa):
    proximo_local = tuple(np.add(local, movimento))
    return (0 <= proximo_local[0] < mapa.shape[0]) and (0 <= proximo_local[1] < mapa.shape[1])

#----------------------------------------------------------------------- execucao do jogo
while tesouro != local_atual:
    contador += 1
    os.system('cls' if os.name == 'nt' else 'clear')

    mapa_atual = mapa.copy()
    mapa_atual[local_atual] = jogador
    print(mapa_atual)
    print(f"\nScore: {score}")
    print('Movimentos inválidos diminuem seu Score!\n')

    movimento = input('Realize seu movimento: ((C)ima, (B)aixo), (D)ireita, (E)squerda) ').lower()

    if (movimento not in movimentacao) or not (esta_no_mapa(local_atual, movimentacao[movimento], mapa)):
        print('\nMovimento inválido!\n')
        score -= 20
        input('Pressione Enter para continuar...')
    else:
        local_atual = tuple(np.add(local_atual, movimentacao[movimento]))

        if nvl_dificuldade >= 40:
            score -= 33
        else:
            score -= 20

    if score <= 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Você perdeu! O tesouro estava em', tesouro)
        break

#----------------------------------------------------------------------- finalizacao do jogo
if score > 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Parabéns, você achou o tesouro!!')
    print(f'Pontuação final: {score}')
