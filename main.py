import pyautogui
import time

TILE_SEGMENTS = 4

def main():
    initialize_grid()

def initialize_grid():
    grid_x = []
    grid_y = []
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
    tile_width = (grid_dimensions[0] / TILE_SEGMENTS, grid_dimensions[1] / TILE_SEGMENTS)

    print(f"grid_dimensions: {grid_dimensions}, tile_width: {tile_width}")
    for x in range(TILE_SEGMENTS):
        x_coordinate = (x_start + tile_width[0] * (x + 0.5))
        grid_x.append(x_coordinate)
        for y in range(TILE_SEGMENTS):
            y_coordinate = (y_end + tile_width[1] * (y + 0.5))
            grid_y.append(y_coordinate)
            grid.append((x_coordinate, y_coordinate))

    print(len(grid))
    for i in grid:
        print(i)

    for coordinate in grid:
        pyautogui.moveTo(coordinate, duration=0)
        time.sleep(0)

if __name__ == '__main__':
    main()