import time
from time import sleep
import random
from random import randint

itens =  ('',' Pedra', 'Papel', 'Tesoura')
pc = randint(1, 3)

print('''\033[33m-=-=-=-=-=-=-=-=-=Opções-=-=-=-=-=-=-=-=-=-\033[m
[ 1 ] ⚫
[ 2 ] 🧻
[ 3 ] ✂️
\033[33m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m''')
jogador = int(input('Faça uma jogada:'))

print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
sleep(2)


print('-='*15)
print('O computador jogou {}'.format(itens[pc]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='* 15)

if pc == 1:             #pc jogou pedra
    if jogador == 1:
        print('''⬜ EMPATE ⬜
        ''')
    elif jogador == 2:
        print('''✔️ JOGADOR VENCE ✔️
        ''')
    elif jogador == 3:
        print('''❌ COMPUTADOR VENCE ❌
        ''')
    else:
        print('''\033[31mJogada Inválida!\033[m
        ''')


elif pc == 2:           #pc jogou papel
    if jogador == 1:
        print('''❌ COMPUTADOR VENCE ❌
        ''')
    elif jogador == 2:   
        print('''⬜ EMPATE ⬜
        ''')
    elif jogador == 3:
        print('''✔️ JOGADOR VENCE ✔️
        ''')
    else:    
        print('''\033[31mJogada Inválida!\033[m
        ''')


elif pc == 3:           #pc jogou tesoura
    if jogador == 1:
        print('''✔️ JOGADOR VENCE ✔️
        ''')
    elif jogador == 2:   
        print('''❌ COMPUTADOR VENCE ❌
        ''')
    elif jogador == 3:
        print('''⬜ EMPATE ⬜
        ''')
    else:    
        print('''\033[31mJogada Inválida!\033[m
        ''')
