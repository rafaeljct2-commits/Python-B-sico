import pygame
import random

pygame.init()

# Tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cobrinha Completa")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Relógio
clock = pygame.time.Clock()

# Fonte
fonte = pygame.font.SysFont(None, 35)

# Cobrinha
tamanho = 20

x = 400
y = 300

velocidade_x = 0
velocidade_y = 0

corpo = []
comprimento = 1

# Comida
comida_x = random.randrange(0, LARGURA, tamanho)
comida_y = random.randrange(0, ALTURA, tamanho)

# Pontos
pontos = 0

rodando = True

while rodando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_LEFT:
                velocidade_x = -tamanho
                velocidade_y = 0

            elif evento.key == pygame.K_RIGHT:
                velocidade_x = tamanho
                velocidade_y = 0

            elif evento.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = -tamanho

            elif evento.key == pygame.K_DOWN:
                velocidade
