import pygame
import os
import random
from code.Const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self, window):
        self.window = window
        self.ground = 450

        # JAVALI
        self.boar = pygame.image.load('./asset/javali.png').convert_alpha()
        self.boar = pygame.transform.scale(self.boar, (50, 50))

        self.boar_x = 80
        self.boar_y = 400

        # pulo
        self.jump = False
        self.vel_y = 0
        self.gravity = 0.1
        self.clock = pygame.time.Clock()

        # CÉU (imagem 1)
        self.bg = pygame.image.load('./asset/city 7/1.png').convert()
        self.bg = pygame.transform.scale(self.bg, (WIN_WIDTH, WIN_HEIGHT))

        # PRÉDIOS (2 até o que você tiver)
        # cada camada separada
        self.layer1 = pygame.image.load('./asset/city 7/2.png').convert_alpha()
        self.layer1 = pygame.transform.scale(self.layer1, (WIN_WIDTH, WIN_HEIGHT))

        self.layer2 = pygame.image.load('./asset/city 7/3.png').convert_alpha()
        self.layer2 = pygame.transform.scale(self.layer2, (WIN_WIDTH, WIN_HEIGHT))

        self.layer3 = pygame.image.load('./asset/city 7/4.png').convert_alpha()
        self.layer3 = pygame.transform.scale(self.layer3, (WIN_WIDTH, WIN_HEIGHT))

        # posições
        self.x1 = 0.5
        self.x2 = 1
        self.x3 = 1.5

        # pedra pequena
        self.rock_small = pygame.image.load('./asset/pedra.png').convert_alpha()
        self.rock_small = pygame.transform.scale(self.rock_small, (40, 40))

        # pedra grande
        self.rock_big = pygame.image.load('./asset/pedra.png').convert_alpha()
        self.rock_big = pygame.transform.scale(self.rock_big, (70, 70))

        # começa com uma aleatória
        self.rock = random.choice([self.rock_small, self.rock_big])

        self.rock_x = WIN_WIDTH


    def run(self):
        while True:

            # EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.jump:
                            self.jump = True
                            self.vel_y = -5

            # GRAVIDADE (PULO)
            if self.jump:
                self.boar_y += self.vel_y
                self.vel_y += self.gravity

                if self.boar_y >= 400:
                    self.boar_y = 400
                    self.jump = False

            # fundo
            self.window.fill((0, 0, 0))
            self.window.blit(self.bg, (0, 0))

            # movimento camadas
            self.x1 -= 0.2
            self.x2 -= 0.4
            self.x3 -= 0.6

            if self.x1 <= -WIN_WIDTH:
                self.x1 = 0
            if self.x2 <= -WIN_WIDTH:
                self.x2 = 0
            if self.x3 <= -WIN_WIDTH:
                self.x3 = 0

                # mover pedra
            self.rock_x -= 1.7

            self.rock_y = self.ground - self.rock.get_height()

            # desenhar camadas
            self.window.blit(self.layer1, (self.x1, 0))
            self.window.blit(self.layer1, (self.x1 + WIN_WIDTH, 0))

            self.window.blit(self.layer2, (self.x2, 0))
            self.window.blit(self.layer2, (self.x2 + WIN_WIDTH, 0))

            self.window.blit(self.layer3, (self.x3, 0))
            self.window.blit(self.layer3, (self.x3 + WIN_WIDTH, 0))

            # desenhar javali
            self.window.blit(self.boar, (self.boar_x, self.boar_y))
            self.clock.tick(150)
            self.window.blit(self.rock, (self.rock_x, self.rock_y))
            # colisão
            boar_rect = pygame.Rect(self.boar_x + 5, self.boar_y + 5, 40, 40)
            rock_rect = self.rock.get_rect(topleft=(self.rock_x, self.rock_y))

            if boar_rect.colliderect(rock_rect):
                print("GAME OVER")
                pygame.quit()
                quit()


            pygame.display.flip()
