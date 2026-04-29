from pygame import *
import sys

init()

largura,altura = 800,600

window = display.set_mode((largura,altura))
display.set_caption("RPG Simples")

relogio = time.Clock()

# Cores
preto = (0,0,0)
azul = (0,0,255)
# Jogador
player_pos = [400,300]
velocidade = 5

# Loop principal
rodando = True
while rodando:
    # Eventos
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    # Movimentação
    keys = key.get_pressed()
    if keys[K_LEFT]: player_pos[0] -= velocidade
    if keys[K_RIGHT]: player_pos[0] += velocidade
    if keys[K_UP]: player_pos[1] -= velocidade
    if keys[K_DOWN]: player_pos[1] += velocidade

    # Desenho
    window.fill(preto)
    draw.rect(window,azul,(player_pos[0],player_pos[1],50,50))
    display.update()

    # FPS
    relogio.tick(60)
QUIT()


    
    
    
    
    
    
    
   

