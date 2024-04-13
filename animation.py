import pygame


# definir une classe pour l'animation
class AnimateSprite(pygame.sprite.Sprite):

    # Chose à faire
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  # commencer l'anim à l'im 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une méthode pour demarrer l'animation
    def start_animation(self):
        self.animation = True

    # definir une méthode pour animer le sprite
    def animate(self, loop=False):

        # verifier si l'animation est active
        if self.animation:

            # passe à l'image suivante
            self.current_image += 1

            # si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

                # verifier si l'animation n'est pa en mode boucle
                if loop is False:

                    # desactivation de l'animation
                    self.animation = False

            # modifier l'image précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# definir une fonction pour charger les images d'unsprite
def load_animation_images(sprite_name):
    # charger les 24 img de ce sprite dans le dossier correspondant
    images = []
    # recuperer le chemin du dossier
    path = f"assets/{sprite_name}/{sprite_name}"

    # boucler sur chaque image
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        pygame.image.load(image_path)
        images.append(pygame.image.load(image_path))

    # renvoyer le contenu de la liste d'image
    return images


# definir un dictionnaire qui va contenir les images chargé de chaque sprite
# mummy -> [...mummy1.png,...mummy2.png,....]
# mummy -> [...player1.png,...player2.png,....]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}
