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

    grid_dimensions = (x_end - x_start, y_start - y_end)
    # Then I need to half this to get the center of each tile, but do that *after* multiplying by 1-4
    tile_width = (grid_dimensions[0] / TILE_SEGMENTS, grid_dimensions[1] / TILE_SEGMENTS)

    print(f"grid_dimensions: {grid_dimensions}, tile_width: {tile_width}")
    for i in range(4):
        x_coordinate = (x_start + tile_width[0] * (i + 0.5))

        print(x_coordinate)
        pyautogui.moveTo(x_coordinate, pyautogui.position().y)
        time.sleep(1)

if __name__ == '__main__':
    main()