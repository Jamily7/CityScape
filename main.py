from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

import pygame

print("Setup start")
pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
print("Setup end")

print("Loop start")

from code.Game import Game

menu = Menu(window)
option = menu.run()

if option == "START":
    game = Game(window)
    game.run()

print(option)
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #end pygame

