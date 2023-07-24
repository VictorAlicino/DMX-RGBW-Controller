from queue import Queue
import numpy as np
import cv2


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb[::-1])


class ColorExtractor:
    def __init__(self):
        self._left_image = None
        self._right_image = None

        self._height: int = 0
        self._width: int = 0

        self._left_colour = [0, 0, 0]
        self._right_colour = [0, 0, 0]
        self._center_colour = [0, 0, 0]
        self._left_hex_colour = '#000000'
        self._right_hex_colour = '#000000'
        self._center_hex_colour = '#000000'

        self._prev_center_colour = (0, 0, 0)

        self._center_fade_speed: float = 1.2

    def get_left_colour(self) -> list:
        return self._left_colour

    def get_right_colour(self) -> list:
        return self._right_colour

    def get_center_colour(self) -> list:
        return self._center_colour

    def get_left_hex_colour(self) -> str:
        return self._left_hex_colour

    def get_right_hex_colour(self) -> str:
        return self._right_hex_colour

    def get_center_hex_colour(self) -> str:
        return self._center_hex_colour

    def update(self, img: np.ndarray):
        image = cv2.resize(img, (320, 480))

        self._height, self._width, _ = image.shape
        self._left_image = image[:, :self._width // 2]
        self._right_image = image[:, self._width // 2:]

        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
        _, img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        img_thresh = cv2.bitwise_not(img_thresh)
        contours, _ = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        max_contour = max(contours, key=cv2.contourArea)
        moment = cv2.moments(max_contour)
        cx = int(moment['m10'] / moment['m00'])
        cy = int(moment['m01'] / moment['m00'])
        center_pixel = image[cy, cx, :]

        self._center_colour = center_pixel[:3].tolist()
        self._center_hex_colour = '#%02x%02x%02x' % (center_pixel[2], center_pixel[1], center_pixel[0])

        left_avg_color = np.mean(self._left_image, axis=(0, 1)).astype(int)
        self._left_colour = left_avg_color[:3].tolist()
        self._left_hex_colour = '#%02x%02x%02x' % (left_avg_color[2], left_avg_color[1], left_avg_color[0])

        right_avg_color = np.mean(self._right_image, axis=(0, 1)).astype(int)
        self._right_colour = right_avg_color[:3].tolist()
        self._right_hex_colour = '#%02x%02x%02x' % (right_avg_color[2], right_avg_color[1], right_avg_color[0])