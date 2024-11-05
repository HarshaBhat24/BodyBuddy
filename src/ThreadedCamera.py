from threading import Thread
import cv2, time


class ThreadedCamera(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        if not self.capture.isOpened():
            raise Exception("Could not open video device")
        self.total_frames = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps= int(self.capture.get(cv2.CAP_PROP_FPS))
        self.duration = self.total_frames / self.fps
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        print(f"Total frames: {self.total_frames}")
        print(f"FPS: {self.fps}")
        print(f"Duration: {self.duration}")

        self.FPS = 1/self.fps
        self.FPS_MS = int(self.FPS * 1000)

        # Start frame retrieval thread
        self.thread = Thread(target=self.update, args=())
        self.frame = None
        self.frame_number=self.total_frames
        self.thread.daemon = True
        self.thread.start()

    def update(self):
        while True:
            if self.total_frames>=0:
                if self.capture.isOpened():
                    (self.status, self.frame) = self.capture.read()
                    self.total_frames-=1
                time.sleep(self.FPS)
            else:
                return

    def show_frame(self):
        return self.FPS_MS, self.frame