import os
import shutil

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text):
    print(text.center(shutil.get_terminal_size().columns))