import pygame
import random

pygame.init()

# Tamanho da tela
largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cobrinha Completa")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Relógio
clock = pygame.time.Clock()

# Cobrinha
x = 400
y = 300

velocidade_x = 0
velocidade_y = 0

tamanho = 20

# Comida
comida_x = random.randrange(0, largura - tamanho, tamanho)
comida_y = random.randrange(0, altura - tamanho, tamanho)

# Pontos
pontos = 0

# Fonte
fonte = pygame.font.SysFont(None, 35)

rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                velocidade_x = -20
                velocidade_y = 0

            if evento.key == pygame.K_RIGHT:
                velocidade_x = 20
                velocidade_y = 0

            if evento.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -20

            if evento.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = 20

    x += velocidade_x
    y += velocidade_y

    # Game Over ao sair da tela
    if x < 0 or x >= largura or y < 0 or y >= altura:
        rodando = False

    # Comer comida
    if x == comida_x and y == comida_y:
        pontos += 1

        comida_x = random.randrange(0, largura - tamanho, tamanho)
        comida_y = random.randrange(0, altura - tamanho, tamanho)

    tela.fill(PRETO)

    # Comida
    pygame.draw.rect(
        tela,
        VERMELHO,
        [comida_x, comida_y, tamanho, tamanho]
    )

    # Cobrinha
    pygame.draw.rect(
        tela,
        VERDE,
        [x, y, tamanho, tamanho]
    )

    # Pontuação
    texto = fonte.render(
        f"Pontos: {pontos}",
        True,
        BRANCO
    )

    tela.blit(texto, (10, 10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
