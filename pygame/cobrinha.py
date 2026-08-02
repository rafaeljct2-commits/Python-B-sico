  import pygame

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cobrinha")

x = 400
y = 300

velocidade = 5

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        x -= velocidade

    if teclas[pygame.K_RIGHT]:
        x += velocidade

    if teclas[pygame.K_UP]:
        y -= velocidade

    if teclas[pygame.K_DOWN]:
        y += velocidade

    tela.fill((0, 0, 0))

    pygame.draw.rect(tela, (0, 255, 0), (x, y, 20, 20))

    pygame.display.flip()

pygame.quit()  
