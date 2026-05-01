import pygame
import sys
import json
import random

WIDTH, HEIGHT = 800, 600
FPS = 60
TILE_SIZE = 32

class Entity(pygame.sprite.Sprite):
    def __init__(self, color, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((32, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()

class Player(Entity):
    def __init__(self, pos, groups, obstacles, enemy_group):
        super().__init__((0, 100, 255), pos, groups)
        self.obstacles = obstacles
        self.enemy_group = enemy_group  # ✅ Recebe como parâmetro
        self.lvl, self.xp, self.hp, self.max_hp = 1, 0, 100, 100
        self.attack_power = 10
        self.inventory = []
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = 0

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.attacking:
            if keys[pygame.K_UP]: self.direction.y = -1
            elif keys[pygame.K_DOWN]: self.direction.y = 1
            else: self.direction.y = 0

            if keys[pygame.K_LEFT]: self.direction.x = -1
            elif keys[pygame.K_RIGHT]: self.direction.x = 1
            else: self.direction.x = 0

            if keys[pygame.K_z]:
                self.attacking = True
                self.attack_

        self.pos.x += self.direction.x * speed
        self.rect.centerx = round(self.pos.x)
        self.collision('horizontal')
        self.pos.y += self.direction.y * speed
        self.rect.centery = round(self.pos.y)
        self.collision('vertical')

    def collision(self, direction):
        for sprite in self.obstacles:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                    self.pos.x = self.rect.centerx
                if direction == 'vertical':
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.centery

    def attack_logic(self):
        hit_rect = self.rect.inflate(40, 40)
        for enemy in self.enemy_group:  # ✅ Usa self.enemy_group
            if hit_rect.colliderect(enemy.rect):
                enemy.get_damage(self.attack_power)

    def update(self):
        self.input()
        self.move(5)
        if self.attacking:
            if pygame.time.get_ticks() - self.attack_time > self.attack_cooldown:
                self.attacking = False

class Enemy(Entity):
    def __init__(self, pos, groups, player, item_group, all_sprites):
        super().__init__((255, 0, 0), pos, groups)
        self.player = player
        self.item_group = item_group  # ✅ Recebe como parâmetro
        self.all_sprites = all_sprites  # ✅ Recebe como parâmetro
        self.hp = 30

    def get_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.player.xp += 50
            if random.random() > 0.5:
                Item(self.rect.center, [self.all_sprites, self.item_group], "Moeda de Ouro")  # ✅ Usa self
            self.kill()

    def update(self):
        v_player = pygame.math.Vector2(self.player.rect.center)
        v_enemy = pygame.math.Vector2(self.rect.center)
        if (v_player - v_enemy).magnitude() < 200:
            dir = (v_player - v_enemy).normalize()
            self.rect.center += dir * 2

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups, name):
        super().__init__(groups)
        self.name = name
        self.image = pygame.Surface((15, 15))
        self.image.fill((255, 215, 0))
        self.rect = self.image.get_rect(center=pos)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20, bold=True)
        
        self.all_sprites = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()  # ✅ Atributo da classe
        self.item_group = pygame.sprite.Group()   # ✅ Atributo da classe
        
        self.player = Player((400, 300), self.all_sprites, self.obstacles, self.enemy_group)  # ✅ Passa enemy_group
        self.spawn_world()

    def spawn_world(self):
        for _ in range(5):
            Entity((50, 50, 50), (random.randint(0, 700), random.randint(0, 500)), [self.all_sprites, self.obstacles])
        for _ in range(3):
            Enemy((random.randint(0, 800), random.randint(0, 600)), [self.all_sprites, self.enemy_group], self.player, self.item_group, self.all_sprites)  # ✅ Passa item_group e all_sprites

    def save(self):
        data = {" f)

    def draw_ui(self):
        pygame.draw.rect(self.screen, (200,0,0), (20, 20, 150, 15))
        pygame.draw.rect(self.screen, (0,200,0), (20, 20, self.player.hp * 1.5, 15))
        info = f"LVL: {self.player.lvl} | XP: {self.player.xp} | [Z] Atacar [S] Save [I] Inventário"
        self.screen.blit(self.font.render(info, True, (255,255,255)), (20, 45))

    def run(self):
        while True:
            self.screen.fill((34, 139, 34))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s: 
                        self.save()
                    if event.key == pygame.K_i: 
                        print(f"Inventário: {self.player.inventory}")

            items_hit = pygame.sprite.spritecollide(self.player, self.item_group, True)
            for item in items_hit: 
                self.player.inventory.append(item.name)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            self.draw_ui()
            
            if self.player.attacking:
                pygame.draw.circle(self.screen, (255,255,0), self.player.rect.center, 40, 2)

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":  # ✅ Removido global desnecessário
    Game().run()