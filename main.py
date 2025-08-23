import pyautogui
import time

def main():
    initialize_grid()
    #pyautogui.moveTo(center)

def initialize_grid():
    print("Place your cursor at the bottom left corner")
    time.sleep(3)
    x1 = pyautogui.position().x
    y1 = pyautogui.position().x
    print(f"x1 = {x1}, y1 = {y1}")

    print("\nPlace your cursor at the top right corner")
    time.sleep(3)
    x2 = pyautogui.position().x
    y2 = pyautogui.position().x
    print(f"x2 = {x2}, y2 = {y2}")

    time.sleep(2)

    # bask in the glory of my fantastic segmenting algorithm
    for i in range(4):
        time.sleep(0.5)
        pyautogui.moveTo(x1 + ((x1 / 4) * i), 500)

if __name__ == '__main__':
    main()