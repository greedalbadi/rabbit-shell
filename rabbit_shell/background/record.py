import numpy
import cv2
import pyautogui
import pickle

class cam_Record:

    def __init__(self, camera: int=0):
        self.cam = cv2.VideoCapture(camera)

    def cam_frame(self):

        ret, frame = self.cam.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def pickle_frame(self, frame):

        return pickle.dumps(frame)

