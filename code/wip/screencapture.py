import dxcam
import numpy as np


class ScreenCapture:
    camera = None
    target_fps = 60

    # constructor
    def __init__(self, monitor):
        self.camera = dxcam.create(output_color="BGR", output_idx=monitor, max_buffer_len=512)

    def startCapture(self):

        # Start Camera
        self.camera.start(target_fps=self.target_fps,video_mode=True)


    def getCapture(self):

        # Take in frame
        frame = self.camera.get_latest_frame()
        frame = frame[..., :3]
        frame = np.ascontiguousarray(frame)

        return frame

    def stopCapture(self):
        # Stop Camera and delete resources
        self.camera.stop()
        del self.camera
