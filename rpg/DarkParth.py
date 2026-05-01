# Jogo da minha autoria
# No pygame
from pygame import *
import sys

init()

largura,altura = 1280,720
window = display.set_mode((largura,altura))
display.set_caption("Dark Parth")

relogio = time.Clock()

# Sprites/artes/mapas/imagens
#sprite_player = image.load("player.png")
#sprite_inimigo = image.load("inimigo.png")
#mapa_fundo = image.load("mapa_tutorail.png")

# Cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)

# Joogador
player_pos = [400,300]
velocidade = 5

# Loop Principal
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
    
    # Movimentação
    keys = key.get_pressed()
    if keys[K_A]:
        player_pos[0] -= velocidade
    if keys[K_D]:
        player_pos[0] += velocidade
    if keys[K_W]:
        player_pos[1] -= velocidade
    if keys[K_S]:
        player_pos[1] += velocidade

    # Botoes de ação
    if keys[K_J]:
        print("Ataque")
    if keys[K_K]:
        print("Defesa")
    if keys[K_L]:
        print("Esquiva")

    # Botoes de interação
    if keys[K_E]:
        print("Interagir")
    if keys[K_I]:
        print("Inventário")
    if keys[K_ESCAPE]:
        print("Menu")
    
    # Botoes de habilidades
    if keys[K_1]:
        print("Habilidade 1: Maldição do Ligamento ")
        for i in range(5):
            print("Dano de alma: 5")
    
    if keys[K_2]:
        print("Habilidade 2: Maldição do Sangue")
        for i in range(5):
            print("Dano de sangue: 15")
    if keys[K_3]:
        print("Habilidade 3: Maldição das Emoções")
        for i in range(5):
            print("Dano mental: 20")
    if keys[K_4]:
        print("Habilidade 4: Maldição da Medo")
        for i in range(5):
            print("Debuff em área : 10")
            
    if keys[K_5]:
        print("Habilidade 5: Maldição do Dano")
        for i in range(5):
            print("Dano em dobro: 30*2")
    if keys[K_6]:
        print("Habilidade 6: Maldição da Doença")
        for i in range(5):
            print("Dano mortal venenoso: 50")
            print("Dano em área: 20")
    if keys[K_7]:
        print("Habilidade 7: Maldição da Ruína")
        for i in range(5):
            print("Dano fisico: 100")
            print("Dano em área: 80")   
    if keys[K_8]:
        print("Habilidade 8: Maldição da Corrupção")
        for i in range(5):
            print("Dano fisco: 200")
            print("Dano em área: 150")
            print("Dano de alma: 135")
        if keys[K_9]:
            print("Habilidade 9: Maldição da Poeira")
            for i in range(5):
                print("Dano mortal: 500")
                print("Dano em área: 300")
                print("Dano de alma: 250")
    # Desenho do mapa
    window.fill(preto)
    #window.blit(mapa_fundo,(0,0))
    # Desenho do jogador   
    # window.blit(sprite_player,(player_pos[0],player_pos[1]))
    # Desenho do inimigo
    # window.blit(sprite_inimigo,(inimigo_pos[0],inimigo
    
    # Desenho geométrico Heroi
    draw.rect(window,azul,(player_pos[0],player_pos[1],50,50))
    
    # Desenho geométrico Inimigo
    draw.rect(window,vermelho,(200,200,50,50))
    
    # Logica de colisão
    player_rect = Rect(player_pos[0],player_pos[1],50,50)
    inimigo_rect = Rect(200,200,50,50)
    if player_rect.colliderect(inimigo_rect):
        print("Colisão detectada! Iniciando batalha...")
        if keys[K_J]:
            print("Player ataca o inimigo!")
            print("Dano causado: 20")
        if keys[K_K]:
            print("Player se defende!")
            
        if keys[K_L]:
            print("Player tenta esquivar!")
        elif keys[K_E]:
                print("Player interage com o inimigo!")
        elif keys[K_I]:
                print("Player abre o inventário durante a batalha!")
        elif keys[K_ESCAPE]:
                print("Player tenta fugir da batalha!")
        

    
    
    
    
    display.update()      
