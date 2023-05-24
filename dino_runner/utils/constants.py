import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioWalk1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioWalk2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarWalk1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarWalk2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarJump.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioDuck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioDuck.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarDuck.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/MarioStarDuck.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/Dragon.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/gumba.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/gumba.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/GreenTube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/GreenTube.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/GreenTube.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/Canon.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Mario/others/Canon.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Mario/others/Flower.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
