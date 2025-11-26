import pygame

pygame.init()

CHRCOLOR = (255, 160, 220)
WIDTH = 1280
HEIGHT = 720
GRAVITY = 15
ACELETION = 5
DESACELERATION = 1
JUMPHEIGHT = 25

tela = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Office Glyphs")

x = 100
y = 100
altura = 60
largura = 40
velocidade_hor = 0
velocidade_ver = GRAVITY

def redrawWindow():
    tela.fill("black")
    pygame.draw.rect(tela, CHRCOLOR, (x, y, largura, altura))
    pygame.display.update()
    clock.tick(60)

rodando = True
while rodando:

    if velocidade_hor > 0:
        velocidade_hor -= DESACELERATION
    elif velocidade_hor < 0:
        velocidade_hor += DESACELERATION
    
    if velocidade_ver > GRAVITY:
        velocidade_ver -= DESACELERATION
    elif velocidade_ver < GRAVITY:
        velocidade_ver += DESACELERATION

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:#Movement
        velocidade_hor = ACELETION
    if teclas[pygame.K_LEFT]:
        velocidade_hor = -ACELETION
    if teclas[pygame.K_UP] and y == HEIGHT - altura:
        velocidade_ver = -JUMPHEIGHT
    if teclas[pygame.K_DOWN]:
        velocidade_ver += ACELETION
    
    if velocidade_hor > 0:#Gravidade
        if x + velocidade_hor + largura >= WIDTH:
            x = WIDTH - largura
        else:
            x += velocidade_hor
    if velocidade_hor < 0:
        if x + velocidade_hor <= 0:
            x = 0
        else:
            x += velocidade_hor
    if velocidade_ver > 0:
        if y + velocidade_ver + altura >= HEIGHT:
            y = HEIGHT - altura
        else:
            y += velocidade_ver
    if velocidade_ver < 0:
        if y + velocidade_ver <= 0:
            y = 0
        else:
            y += velocidade_ver

    redrawWindow()

pygame.quit()