import pyautogui
import time
import sys
import keyboard
import mouse
from PIL import ImageGrab

def main():
    grid_matrix = initialize_grid_matrix()
    scan_for_black_tiles(grid_matrix)
    game_loop(grid_matrix)

def game_loop(grid_matrix):
    while not keyboard.is_pressed('q'):
        scan_for_black_tiles(grid_matrix)
    sys.exit()

def scan_for_black_tiles(grid_matrix):
    # bottom to top (priority)
    screenshot = ImageGrab.grab()
    for row in reversed(grid_matrix):
        for x, y in row:
            pixel = screenshot.getpixel((x, y))
            if pixel == (0, 0, 0):
                click_coordinate(x, y)

def click_coordinate(x, y, hold_duration = 0.01):
    print(f"detected black tile coordinate: {(x, y)}")
    pyautogui.mouseDown(x=x, y=y + 40, button="left")
    pyautogui.mouseUp(button="left")

# for now, i'll manually put in the tile positions, but it will be configurable later
def initialize_grid_matrix():
    # these get initialized to tuples later, but for readability this works for my purposes

    # this represents the tile coordinates to check
    grid_matrix = [
        [(250, 600), (360, 600), (480, 600), (590, 600)],
        [(250, 800), (360, 800), (480, 800), (590, 800)]
    ]
    return grid_matrix


if __name__ == '__main__':
    main()