import subprocess
import sys

# check exists package
try:
    import pygame
    import pygame_menu
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame==2.0.2"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-menu==4.1.4"])
    import pygame
    import pygame_menu

# init pygame
pygame.init()
surface = pygame.display.set_mode((600, 400))

# make your menu
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Hello pygame', 400, 300,
                       theme=pygame_menu.themes.THEME_ORANGE)

menu.add.text_input('Name :', default='PTMTP')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

# run game menu
menu.mainloop(surface)
