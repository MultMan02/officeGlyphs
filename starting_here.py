import pygame

pygame.init()

CHRCOLOR = (255, 160, 220)
WIDTH = 500
HEIGHT = 500

tela = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Office Glyphs")

x = 50
y = 50
altura = 60
largura = 40
velocidade = 5

rodando = True

while rodando:

    tela.fill("black")

    pygame.draw.rect(tela, CHRCOLOR, (x, y, largura, altura))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_RIGHT]:
        if x + largura >= WIDTH:
            x = WIDTH - largura
        else:
            x += velocidade
    if teclas[pygame.K_LEFT]:
        if x <= 0:
            x = 0
        else:
            x -= velocidade
    if teclas[pygame.K_UP]:
        if y <= 0:
            y = 0
        else:
            y -= velocidade
    if teclas[pygame.K_DOWN]:
        if y + altura >= HEIGHT:
            y = HEIGHT - altura
        else:
            y += velocidade
    
    pygame.display.update()

    clock.tick(60)

pygame.quit()