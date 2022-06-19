import numpy as np
import pyautogui
import cv2
from PIL import ImageGrab


class stream_screen:

    def screen_size(self):
        width, height = pyautogui.size()

        size = (0, 0, int(width), int(height))

        return size

    def screen_frame(self, size):

        frame = ImageGrab.grab(size)
        frame = np.array(frame)

        return frame

    def resize_frame(self, frame):

        h, w, L = frame.shape
        h = int(h / 2)
        w = int(w / 2)
        return cv2.resize(frame, (w, h))




