import time
import sys
import keyboard
from Xlib import display, X
from Xlib.ext import xtest
from PIL import ImageGrab


disp = display.Display()
root = disp.screen().root

def main():
    time.sleep(1)
    game_loop()

def game_loop():
    while not keyboard.is_pressed('q'):
        scan_for_black_tiles()
    sys.exit()

def scan_for_black_tiles():
    start = time.time()

    left = 251
    top = 579
    right = 589
    bottom = 619

    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    tile_x_positions = [251, 360, 480, 588]
    y_position = 600

    for x in tile_x_positions:
        pixel = screenshot.getpixel((x - left, y_position - top))
        if pixel == (0, 0, 0):
            click_coordinate(x, y_position + 40)

    end = time.time()
    print(end - start)

def click_coordinate(x, y):
    root.warp_pointer(x, y)
    disp.sync()
    time.sleep(0.005)

    xtest.fake_input(disp, X.ButtonPress, 1)
    disp.sync()
    time.sleep(0.03)
    xtest.fake_input(disp, X.ButtonRelease, 1)
    disp.sync()

if __name__ == '__main__':
    main()