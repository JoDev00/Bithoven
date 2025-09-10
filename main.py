import pyautogui
import time
import pyscreeze
import sys
import keyboard
import mouse

def main():
    window_dimensions = (200, 951), (640, 165)
    grid_matrix = initialize_grid_matrix(window_dimensions)
    scan_for_black_tiles(grid_matrix)
    game_loop(grid_matrix)

def game_loop(grid_matrix):
    while not keyboard.is_pressed('q'):
        scan_for_black_tiles(grid_matrix)

    sys.exit()

def scan_for_black_tiles(grid_matrix):
    # bottom to top (priority)
    for row in reversed(grid_matrix):
        for coordinate in row:
            if pyautogui.pixelMatchesColor(x=coordinate[0], y=coordinate[1], expectedRGBColor=(0, 0, 0)):
                print(f"detected black tile coordinate: {coordinate}")
                pyautogui.mouseDown(x=coordinate[0], y=coordinate[1], button="left")
                time.sleep(0.01)
                pyautogui.mouseUp(x=coordinate[0], y=coordinate[1], button="left")

# for now, i'll manually put in the tile positions, but it will be configurable later
def initialize_grid_matrix(window_dimensions):
    # these get initialized to tuples later, but for readability this works for my purposes

    # this represents the tile coordinates to check
    grid_matrix = [
        [(250, 200), (360, 200), (480, 200), (590, 200)],
        [(250, 400), (360, 400), (480, 400), (590, 400)],
        [(250, 600), (360, 600), (480, 600), (590, 600)],
        [(250, 800), (360, 800), (480, 800), (590, 800)]
    ]
    return grid_matrix


if __name__ == '__main__':
    main()