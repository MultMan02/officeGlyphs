import pygame

pygame.init()

CHRCOLOR = (255, 160, 220)
WIDTH = 1280
HEIGHT = 720
GRAVITY = 15
ACELETION = 5
DESACELERATION = 1
JUMPHEIGHT = 15

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

def redrawWindow():
    screen.fill("white")
    pygame.draw.rect(screen, CHRCOLOR, (Jonas.x, Jonas.y, Jonas.width, Jonas.height))
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
        Jonas.hSpeed = ACELETION
    if keys[pygame.K_LEFT]:
        Jonas.hSpeed = -ACELETION
    if keys[pygame.K_UP] and Jonas.y == HEIGHT - Jonas.height:
        Jonas.vSpeed = -JUMPHEIGHT
    if keys[pygame.K_DOWN]:
        Jonas.vSpeed += ACELETION
    
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