import pygame

# 1. Inicializar Pygame
pygame.init()
tela = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Classe da Sprite
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 2. Carregar imagem e rect
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0)) # Quadrado verde
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.velocidade = 5

    def update(self):
        # 3. Mover com base nas teclas
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade

# 4. Criar grupo e instanciar
todas_as_sprites = pygame.sprite.Group()
jogador = Jogador()
todas_as_sprites.add(jogador)

# Loop do Jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar e Desenhar
    todas_as_sprites.update()
    
    tela.fill((0, 0, 0)) # Limpar tela
    todas_as_sprites.draw(tela)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
