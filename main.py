import pygame
from background import Background
from player import Player
from enemy import Enemy
from bullet import Bullet

# Définir les dimensions de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Créer une fenêtre pygame
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Définir le titre de la fenêtre
pygame.display.set_caption("LeTangu Swat Simulator")

# Créer un groupe pour stocker tous les sprites
all_sprites = pygame.sprite.Group()

# Créer le fond d'écran
background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(background)

# Créer le joueur
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(player)

# Créer les ennemis
enemies = pygame.sprite.Group()
for _ in range(10):
    enemy = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT)
    all_sprites.add(enemy)
    enemies.add(enemy)

# Créer les balles
bullets = pygame.sprite.Group()

# Définir la boucle de jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Mettre à jour les positions des sprites
    all_sprites.update()

    # Vérifier les collisions entre le joueur et les ennemis
    if pygame.sprite.spritecollide(player, enemies, True):
        running = False

    # Vérifier les collisions entre les balles et les ennemis
    for bullet in bullets:
        if pygame.sprite.spritecollide(bullet, enemies, True):
            bullets.remove(bullet)
            all_sprites.remove(bullet)

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Dessiner tous les sprites
    all_sprites.draw(screen)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()