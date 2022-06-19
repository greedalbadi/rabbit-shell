import cv2





class stream_webcam:

    def __init__(self, title="", camera=0):

            self.camera = camera
            self.title = title

    def get_frame(self, cv2_camera):

        ret, frame = cv2_camera

        return frame

    def colorframe(self, frame):

        # color frame
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
