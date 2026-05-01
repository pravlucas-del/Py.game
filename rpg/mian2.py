# Jogo do Bicalho rpg 
# No pygame

from pygame import *
import sys

init()

largura,altura = 800,600
window = display.set_mode((largura,altura))
display.set_caption("RPG Simples")
relogio = time.Clock()
# Cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
# Jogadores
player1_pos = [400,300]
player2_pos = [500,300]
player3_pos = [600,300]
velocidade = 5
# Loop principal
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
            keys = key.get_pressed()
        
        # Movimentação Player 1
        if keys[K_A]: player1_pos[0] -= velocidade
        if keys[K_D]: player1_pos[0] += velocidade
        if keys[K_W]: player1_pos[1] -= velocidade
        if keys[K_S]: player1_pos[1] += velocidade
        
        # Movimentação Player 2
        if keys[K_LEFT]: player2_pos[0] -= velocidade
        if keys[K_RIGHT]: player2_pos[0] += velocidade
        if keys[K_UP]: player2_pos[1] -= velocidade
        if keys[K_DOWN]: player2_pos[1] += velocidade
        
        # Movimentação Player 3
        if keys[K_J]: player3_pos[0] -= velocidade
        if keys[K_L]: player3_pos[0] += velocidade
        if keys[K_I]: player3_pos[1] -= velocidade
        if keys[K_K]: player3_pos[1] += velocidade
    
    # Desenho
    window.fill(preto)
    draw.rect(window,vermelho,(player1_pos[0],player1_pos[1],50,50))
    draw.rect(window,verde,(player2_pos[0],player2_pos[1],50,50))
    draw.rect(window,azul,(player3_pos[0],player3_pos[1],50,50))
    display.flip()
    relogio.tick(60)
    
    # Desenho inimigos
    draw.rect(window,branco,(100,100,50,50))
    draw.rect(window,branco,(200,100,50,50))
    # Desenho mapa
    draw.rect(window,branco,(0,0,800,600),5)


    # Logica de batalha de turnos
    # Aqui você pode implementar a lógica de batalha de turnos, onde cada jogador tem uma vez para atacar ou usar habilidades. 
    # Você pode criar um sistema de HP, ataques e habilidades para cada jogador, e implementar a lógica de batalha de turnos com base nisso.
    if keys[K_C]:
        print("Player 1 ataca Player 2!")
        if keys[K_1] or keys[K_2]:
            print("Player 1 usa habilidade especial!")
            if keys[K_3]:
                print("Player 1 usa ultimate!")
    if keys[K_B]:
        print("Player 2 ataca Player 1!")
        if keys[K_4] or keys[K_5]:
            print("Player 2 usa habilidade especial!")
            if keys[K_6]:
                print("Player 2 usa ultimate!")
    if keys[K_N]:
        print("Player 3 ataca Player 1!")
        if keys[K_7] or keys[K_8]:
            print("Player 3 usa habilidade especial!")
            if keys[K_9]:
                print("Player 3 usa ultimate!")
    hp_player1 = 100
    hp_player2 = 80
    hp_player3 = 60
    velocidade_ataque = 10
    # Aqui você pode implementar a lógica de redução de HP quando um jogador é atacado, e verificar se algum jogador foi derrotado (HP <= 0).
    if keys[K_c]:
        hp_player2 -= velocidade_ataque
        print(f"Player 2 HP: {hp_player2}")
        if hp_player2 <= 0:
            print("Player 2 foi derrotado!")
    if keys[K_B]:
        hp_player1 -= velocidade_ataque
        print(f"Player 1 HP: {hp_player1}")
        if hp_player1 <= 0:
            print("Player 1 foi derrotado!")
    if keys[K_n]:
        hp_player1 -= velocidade_ataque
        print(f"Player 3 HP: {hp_player3}")
        if hp_player3 <= 0:
            print("Player 3 foi derrotado!")
    # Aqui você pode implementar a lógica de vitória, onde o jogo termina quando um jogador é derrotado e os outros jogadores são declarados vencedores.
    if hp_player1 <= 0:
        print("Player 2 e Player 3 são os vencedores!")
    elif hp_player2 <= 0:
        print("Player 1 e Player 3 são os vencedores!")
    elif hp_player3 <= 0:
        print("Player 1 e Player 2 são os vencedores!")
    else:
        print("A batalha continua")
    if keys[K_ESCAPE]:
        print("Jogo encerrado!")
        quit()
        sys.exit()
