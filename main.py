import pyautogui
import time
import pyscreeze
import sys
import keyboard
import mouse

TILE_SEGMENTS = 4

def main():
    window_positions = initialize_window_positions()
    grid = initialize_grid(window_positions[0], window_positions[1], window_positions[2], window_positions[3])

    print("Press a to commence, or q to exit")
    while True:
        print(pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1]))

        if keyboard.is_pressed("q"):
            print("Exiting program")
            sys.exit()

        if keyboard.is_pressed("a"):
            game_loop(grid)

def game_loop(grid):
    # The tiles we want to keep the closest attention on
    top_row_of_tiles = []
    for i in range(len(grid)):
        if i == 0 or i % 4 == 0:
            top_row_of_tiles.append(grid[i])

    while True:
        for coordinate in top_row_of_tiles:
            if pyscreeze.pixelMatchesColor(coordinate[0], coordinate[1], (0, 0, 0)):
                pyautogui.mouseDown(x=coordinate[0], y=coordinate[1] + 50, button="left")
                time.sleep(0.01)
                pyautogui.mouseUp(x=coordinate[0], y=coordinate[1] + 50, button="left")
                continue

        if keyboard.is_pressed("q"):
            print("Exiting program")
            sys.exit()

def initialize_grid(x_start, x_end, y_start, y_end):
    grid_x = []
    grid_y = []
    grid = []

    grid_dimensions = (x_end - x_start, y_start - y_end)
    tile_width = (grid_dimensions[0] / TILE_SEGMENTS, grid_dimensions[1] / TILE_SEGMENTS)

    print(f"grid_dimensions: {grid_dimensions}, tile_width: {tile_width}")
    for x in range(TILE_SEGMENTS):
        x_coordinate = (x_start + tile_width[0] * (x + 0.5))
        grid_x.append(x_coordinate)
        for y in range(TILE_SEGMENTS):
            y_coordinate = (y_end + tile_width[1] * (y + 0.5))
            grid_y.append(y_coordinate)
            grid.append((x_coordinate, y_coordinate))

    return grid

def initialize_window_positions():
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

    return x_start, x_end, y_start, y_end


if __name__ == '__main__':
    main()