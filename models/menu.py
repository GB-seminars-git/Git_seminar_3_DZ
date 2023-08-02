from models.text import *


def main_menu() -> int:
    print(menu_main_msg)
    while True:
        choice = input(choice_menu_msg)
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')
