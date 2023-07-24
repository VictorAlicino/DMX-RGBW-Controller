import sys
import tkinter as tk
import time
import pyautogui
import numpy as np
import mss
import cv2
from color_extractor import ColorExtractor

debug_ver: bool = False


def _main() -> int:
    CE = ColorExtractor()
    while True:
        with mss.mss() as sct:
            # Define the region of the screen to capture
            monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
            # Capture the screen region and convert it to a numpy array
            img = np.array(sct.grab(monitor))

            CE.update(img)
            print(f'Left: {CE.get_left_hex_colour()} '
                  f'Center: {CE.get_center_hex_colour()} '
                  f'Right: {CE.get_right_hex_colour()}')
    return 0


def _debug_main() -> int:
    print('Debug mode on')
    CE = ColorExtractor()

    iterations = 10  # Number of iterations to run before measuring frequency
    start_time = time.monotonic()
    frequency = 0

    root = tk.Tk()

    left_color_box = tk.Canvas(root, width=350, height=350)
    left_color_box.pack(side="left", padx=5, pady=5)

    center_color_box = tk.Canvas(root, width=350, height=350)
    center_color_box.pack(side="left", padx=5, pady=5)

    right_color_box = tk.Canvas(root, width=350, height=350)
    right_color_box.pack(side="right", padx=5, pady=5)

    while True:
        for i in range(iterations):
            with mss.mss() as sct:
                # Define the region of the screen to capture
                monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
                # Capture the screen region and convert it to a numpy array
                img = np.array(sct.grab(monitor))

                CE.update(img)
                print(f'Left: {CE.get_left_hex_colour()} | '
                      f'Center: {CE.get_center_hex_colour()} | '
                      f'Right: {CE.get_right_hex_colour()} | '
                      f'@{frequency:.2f}Hz')
                left_color_box.delete("all")
                left_color_box.create_rectangle(0, 0, 350, 350,
                                                fill=f"#{CE.get_left_colour()[2]:02x}"
                                                     f"{CE.get_left_colour()[1]:02x}"
                                                     f"{CE.get_left_colour()[0]:02x}")

                center_color_box.delete("all")
                center_color_box.create_rectangle(0, 0, 350, 350,
                                                  fill=f"#{CE.get_center_colour()[2]:02x}"
                                                       f"{CE.get_center_colour()[1]:02x}"
                                                       f"{CE.get_center_colour()[0]:02x}")

                right_color_box.delete("all")
                right_color_box.create_rectangle(0, 0, 350, 350,
                                                 fill=f"#{CE.get_right_colour()[2]:02x}"
                                                      f"{CE.get_right_colour()[1]:02x}"
                                                      f"{CE.get_right_colour()[0]:02x}")
                root.update()

        elapsed_time = time.monotonic() - start_time
        frequency = iterations / elapsed_time
        start_time = time.monotonic()
    root.mainloop()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '--debug':
            debug_ver = True
            sys.exit(_debug_main())
        else:
            print('Unknown argument')
            sys.exit(1)
    else:
        sys.exit(_main())
