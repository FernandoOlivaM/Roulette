import os, random, colorama
from colorama import Fore, Style
file = open("options.txt", "r")
options = file.readlines()
file.close()
while True:
    spin = input(Fore.WHITE + 'Press any key to spin')
    print('And the winner is... ' + Fore.MAGENTA + options[random.randrange(1000, 0, -2) % len(options)])