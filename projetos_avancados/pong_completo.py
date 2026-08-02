import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong Completo")

barra_y = 250
velocidade_barra = 6

bola_x = 400
bola_y = 300

velocidade_bola_x = 4
velocidade_bola_y = 4

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        barra_y -= velocidade_barra

    if teclas[pygame.K_DOWN]:
        barra_y += velocidade_barra

    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    if bola_y <= 0 or bola_y >= altura:
        velocidade_bola_y *= -1

    if bola_x <= 70 and barra_y <= bola_y <= barra_y + 100:
        velocidade_bola_x *= -1

    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (255, 255, 255), (50, barra_y, 20, 100))
    pygame.draw.circle(tela, (255, 255, 255), (bola_x, bola_y), 10)

    pygame.display.flip()

pygame.quit()
