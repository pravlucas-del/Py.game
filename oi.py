import pygame
import sys

# Inicializa o Pygame
pygame.init()

# 1. CONFIGURAÇÕES DO JOGO
TILE_SIZE = 32  # Altere para o tamanho dos seus tiles (ex: 16, 32 ou 64)
COLUNAS = 10
LINHAS = 10

LARGURA_TELA = COLUNAS * TILE_SIZE
ALTURA_TELA = LINHAS * TILE_SIZE

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Meu Mapa de Masmorra")
clock = pygame.time.Clock()

# 2. CARREGAR AS IMAGENS DO SEU TILESET
# Remova os comentários '#' abaixo quando tiver as imagens salvas na pasta
texturas = {
    # 0: pygame.transform.scale(pygame.image.load("chao.png"), (TILE_SIZE, TILE_SIZE)),
    # 1: pygame.transform.scale(pygame.image.load("parede.png"), (TILE_SIZE, TILE_SIZE)),
    # 2: pygame.transform.scale(pygame.image.load("porta.png"), (TILE_SIZE, TILE_SIZE)),
    
    # Cores temporárias para teste caso não tenha as imagens prontas:
    0: (50, 50, 50),       # Chão = Cinza Escuro
    1: (120, 120, 120),   # Parede = Cinza Claro
    2: (150, 75, 0)       # Porta = Marrom
}

# 3. MATRIZ DO MAPA
mapa_masmorra = [
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 4. FUNÇÃO DE RENDERIZAÇÃO
def desenhar_mapa():
    for linha_index, linha in enumerate(mapa_masmorra):
        for coluna_index, tile_id in enumerate(linha):
            pos_x = coluna_index * TILE_SIZE
            pos_y = linha_index * TILE_SIZE
            
            recurso = texturas[tile_id]
            
            # Se for uma imagem (Surface do Pygame) desenha a textura, senão desenha um bloco colorido
            if isinstance(recurso, pygame.Surface):
                tela.blit(recurso, (pos_x, pos_y))
            else:
                pygame.draw.rect(tela, recurso, (pos_x, pos_y, TILE_SIZE, TILE_SIZE))

# 5. LOOP PRINCIPAL DO JOGO
while True:
    # Gerencia eventos do sistema
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Limpa a tela com uma cor de fundo (Preto)
    tela.fill((0, 0, 0))
    
    # Desenha os blocos na tela
    desenhar_mapa()
    
    # Atualiza a exibição da janela
    pygame.display.flip()
    
    # Controla a taxa de quadros (60 FPS)
    clock.tick(60)
