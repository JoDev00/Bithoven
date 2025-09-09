import pyautogui
import time

TILE_SEGMENTS = 4

def main():
    initialize_grid()
    #pyautogui.moveTo(center)

def initialize_grid():
    grid = []

    print("Place your cursor at the bottom left corner")
    time.sleep(2)
    x_start = pyautogui.position().x
    y_start = pyautogui.position().y

    print("\nPlace your cursor at the top right corner")
    time.sleep(2)
    x_end = pyautogui.position().x
    y_end = pyautogui.position().y

    print(f"x_start = {x_start}, y_start = {y_start}")
    print(f"x_end = {x_end}, y_end = {y_end}")

    middle = ((x_start + x_end) / 2, (y_start + y_end) / 2)
    pyautogui.moveTo(middle)
    print(f"moved to {middle}")

if __name__ == '__main__':
    main()