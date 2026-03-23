from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Game import Game
import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
print("Setup end")

print("Loop start")

while True:
    menu = Menu(window)
    option = menu.run()

    print(option)

    if option == "START":
        game = Game(window)
        game.run()

    elif option == "EXIT":
        pygame.quit()
        quit()