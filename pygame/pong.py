import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

barra_y = 250
velocidade = 5

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP]:
        barra_y -= velocidade

    if teclas[pygame.K_DOWN]:
        barra_y += velocidade

    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (255, 255, 255), (50, barra_y, 20, 100))

    pygame.display.flip()

pygame.quit()
