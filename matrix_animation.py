import random
import os
import time
import shutil

def get_terminal_size():
    return shutil.get_terminal_size((80, 20))

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def matrix_rain(duration=10):
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    width, height = get_terminal_size()
    drops = [0] * width

    end_time = time.time() + duration
    sleep_time = 0.2
    while time.time() < end_time:
        print('\033[1;32m', end='')
        for i in range(width):
            if drops[i] == 0 or random.random() > 0.95:
                drops[i] = random.randint(1, height)
            print(f'\033[{drops[i]};{i}H{random.choice(chars)}', end='')
            drops[i] -= 1
            if drops[i] < 1:
                drops[i] = 0
        time.sleep(sleep_time)
        sleep_time = max(0.01, sleep_time * 0.9)  # Decrease sleep time
        print('\033[0m', end='')

def print_success():
    message = [
        "                                                                       ",
        "  ______ ____ ______     ________ __   ____  ____  ____   ______ ______",
        " /  ___// ___\\____ \   /  ___/  |  \_/ ___\/ ___\/ __ \ /  ___//  ___/",
        " \___ \\  \___|  |_> >  \___ \|  |  /\  \__\  \__\  ___/ \___ \ \___ \ ",
        "/____  >\___  >   __/  /____  >____/  \___  >___  >___  >____  >____  >",
        "     \/     \/|__|          \/            \/    \/    \/     \/     \/ ",
        "    "
    ]
    width, height = get_terminal_size()
    start_row = height // 2 - len(message) // 2
    start_col = (width - max(len(line) for line in message)) // 2

    print('\033[1;33m', end='')
    for i, line in enumerate(message):
        print(f'\033[{start_row + i};{start_col}H{line}')
    print('\033[0m', end='')

if __name__ == "__main__":
    try:
        clear_console()
        hide_cursor()
        matrix_rain(duration=10)
        clear_console()
        print_success()
        time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_console()
