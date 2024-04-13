import pygame
import math
from game import Game

pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

# fenetre
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))

# chargement de l'arriere plan
background = pygame.image.load('assets/bg.jpg')

# importer ou charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer ou charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()

running = True

# game loop // boucle du jeu

while running:

    # appliquer l'arriere plan au jeu
    screen.blit(background, (0, -200))

    # vérifier si le jeu a commencé ou non
    if game.is_playing:
        # déclencher les instructions de la partie
        game.update(screen)

    # verifier si le jeu n'a pa commencé
    else:
        # ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # print(game.player.rect.x)

    # MISE A JOUR FENETRE
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si touche esc active
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancer
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification pour savoir si la souris est en collision avec le button jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancer
                game.start()
                # jouer le son
                game.sound_manager.play('click')
    # fixer le nombre de FPS SUR ma clock
    clock.tick(FPS)
