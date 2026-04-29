import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações de tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("RPG de Turno Básico")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
CINZA = (200, 200, 200)

# Fontes
fonte = pygame.font.SysFont("Arial", 30)

# Classe do Personagem
class Personagem:
    def __init__(self, nome, hp, ataque, x, y, cor):
        self.nome = nome
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.x = x
        self.y = y
        self.cor = cor

    def desenhar(self, surface):
        # Desenha "personagem" (um quadrado simples)
        pygame.draw.rect(surface, self.cor, (self.x, self.y, 100, 100))
        # Desenha HP
        texto_hp = fonte.render(f"{self.nome}: {self.hp}/{self.hp_max}", True, PRETO)
        surface.blit(texto_hp, (self.x, self.y - 40))

    def atacar(self, alvo):
        dano = random.randint(self.ataque - 5, self.ataque + 5)
        alvo.hp -= dano
        if alvo.hp < 0: alvo.hp = 0
        return dano

# Instâncias
player = Personagem("Heroi", 50, 20, 150, 300, AZUL)
inimigo = Personagem("Monstro", 80, 15, 550, 300, VERMELHO)

# Variáveis do jogo
turno_player = True
mensagem = "Seu turno! Pressione ESPAÇO para atacar."
rodando = True
relogio = pygame.time.Clock()

# Loop Principal
while rodando:
    tela.fill(PRETO)
    
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        if turno_player and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Turno do Jogador
                dano = player.atacar(inimigo)
                mensagem = f"Você causou {dano} de dano!"
                turno_player = False
                
                # Verifica se o inimigo morreu
                if inimigo.hp <= 0:
                    mensagem = "Você venceu!"
                    turno_player = None # Fim de jogo

    # Turno do Inimigo
    if turno_player == False and inimigo.hp > 0:
        pygame.display.update()
        pygame.time.wait(1000) # Pausa dramática
        dano = inimigo.atacar(player)
        mensagem = f"Monstro causou {dano} de dano!"
        turno_player = True
        
        # Verifica se o jogador morreu
        if player.hp <= 0:
            mensagem = "Game Over!"
            turno_player = None

    # Desenhar elementos
    player.desenhar(tela)
    inimigo.desenhar(tela)
    
    # Desenhar mensagens
    texto_msg = fonte.render(mensagem, True, PRETO)
    tela.blit(texto_msg, (LARGURA // 2 - texto_msg.get_width() // 2, 50))

    pygame.display.flip()
    relogio.tick(30)

pygame.quit()
