import pygame
import pygame.image

from pygame import Surface, Rect
from pygame.font import Font

C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)

WIN_WIDTH = 800

MENU_OPTION = ("START", "EXIT")


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/fundo menu.png').convert()
        self.boar = pygame.image.load('./asset/javali.png').convert_alpha()
        self.boar = pygame.transform.scale(self.boar, (100, 100))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0


        while True:
            self.window.blit(self.surf, self.rect)
            self.window.blit(self.boar, (97, 200))

            self.menu_text(50, "CITY SCAPE", C_WHITE, (WIN_WIDTH / 2, 100))
            self.menu_text(20, "ENTER - START", (255, 255, 255), (WIN_WIDTH / 2, 330))
            self.menu_text(20, "ESPAÇO - PULAR", (255, 255, 255), (WIN_WIDTH / 2, 300))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(30, MENU_OPTION[i], C_YELLOW, (WIN_WIDTH / 2, 200 + 40 * i))
                else:
                    self.menu_text(30, MENU_OPTION[i], C_WHITE, (WIN_WIDTH / 2, 200 + 40 * i))

            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont("comicsansms", text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)