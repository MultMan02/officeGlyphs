import pygame

pygame.init()

JonasImg = pygame.image.load('game/assets/Jonas.png')
background = pygame.image.load('game/assets/Background.png')
jumpSound = pygame.mixer.Sound('game/assets/Jump.wav')
Song = pygame.mixer.music.load('game/assets/Song.mp3')
pygame.mixer.music.play(-1)

CHRCOLOR = (255, 160, 220)
WIDTH = 1280
HEIGHT = 720
GRAVITY = 15
ACELERATION = 5
DESACELERATION = 1
jumpheight = 15
highJump = False
onAir = False
cooldown = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Office Glyphs")

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hSpeed = 0
        self.vSpeed = GRAVITY
        self.hitbox = (self.x + 16, self.y + 4, 32, 54)

def redrawWindow():
    screen.blit(background, (0, 0))
    screen.blit(JonasImg, (Jonas.x, Jonas.y))
    if highJump:
        pygame.draw.rect(screen, "green", (0, 0, 20, 20))
    else:
        pygame.draw.rect(screen, "red", (0, 0, 20, 20))
    pygame.display.update()
    clock.tick(60)

Jonas = player(WIDTH // 2, HEIGHT // 2, 64, 64)
rodando = True
while rodando:

    if Jonas.hSpeed > 0:
        Jonas.hSpeed -= DESACELERATION
    elif Jonas.hSpeed < 0:
        Jonas.hSpeed += DESACELERATION
    
    if Jonas.vSpeed > GRAVITY:
        Jonas.vSpeed -= DESACELERATION
    elif Jonas.vSpeed < GRAVITY:
        Jonas.vSpeed += DESACELERATION

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:#Movement
        Jonas.hSpeed = ACELERATION
    if keys[pygame.K_LEFT]:
        Jonas.hSpeed = -ACELERATION
    if keys[pygame.K_UP] and Jonas.y == HEIGHT - Jonas.height and onAir == False:
        Jonas.vSpeed = -jumpheight
        jumpSound.play()
        onAir = True
    if keys[pygame.K_DOWN]:
        Jonas.vSpeed += ACELERATION
    if keys[pygame.K_j] and cooldown == 0:
        if highJump:
            highJump = False
        else:
            highJump = True
        cooldown = 1
    
    if onAir and Jonas.y <= HEIGHT - Jonas.height - 1:
        onAir = False


    if cooldown >= 1:
        cooldown += 1
    if cooldown >= 30:
        cooldown = 0
    
    if highJump:
        jumpheight = 30
    else:
        jumpheight = 15
    
    if Jonas.hSpeed > 0:#Gravidade
        if Jonas.x + Jonas.hSpeed + Jonas.width >= WIDTH:
            Jonas.x = WIDTH - Jonas.width
        else:
            Jonas.x += Jonas.hSpeed
    if Jonas.hSpeed < 0:
        if Jonas.x + Jonas.hSpeed <= 0:
            Jonas.x = 0
        else:
            Jonas.x += Jonas.hSpeed
    if Jonas.vSpeed > 0:
        if Jonas.y + Jonas.vSpeed + Jonas.height >= HEIGHT:
            Jonas.y = HEIGHT - Jonas.height
        else:
            Jonas.y += Jonas.vSpeed
    if Jonas.vSpeed < 0:
        if Jonas.y + Jonas.vSpeed <= 0:
            Jonas.y = 0
        else:
            Jonas.y += Jonas.vSpeed

    redrawWindow()

pygame.quit()