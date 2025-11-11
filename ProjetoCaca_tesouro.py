import numpy as np

mapa = np.random.randint(10,99,(5,5))

local_inicio = (0,0)
local_atual = (0,0)
local_test = ()
linha = 0
coluna = 0
pontuacao = 0

jogador=-1
mapa_atual = mapa.copy()


linha= np.random.randint(0,mapa.shape[0]) 
coluna = np.random.randint(0,mapa.shape[1])

if (linha==0 and coluna ==0):
    coluna = np.random.randint(1,mapa.shape[1])

def esta_no_mapa(local,movimento, mapa):
    localDetest = tuple(np.add(local, movimento))
    if(0 <=localDetest[0] < mapa.shape[0]) and (0<=localDetest[1] < mapa.shape[1]):
        return True
    else:
        return False


tesouro = (linha, coluna)



movimentacao = {
    'cima' : [-1, 0],
    'baixo' : [1 , 0],
    'esquerda' : [0 , -1],
    'direita' : [0 , 1],
    'c' : [-1 , 0],
    'b' : [1 , 0],
    'e' : [0 , -1],
    'd' : [0 , 1]
}

while tesouro != local_atual:
    mapa_atual = mapa.copy()
    mapa_atual[local_atual] = jogador 
    print(mapa_atual)


    movimento = input('Realize seu movimento ')

    if (movimento not in movimentacao) or not (esta_no_mapa(local_atual,movimentacao[movimento],mapa)):
        print('\n Movimento invalido \n')

    else:
        local_atual = tuple(np.add(local_atual, movimentacao[movimento]))

    pontuacao += 100


print('Parabens voce achou o tesouro!!')
print(f'Pontuacao : {pontuacao}')


