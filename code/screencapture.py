import dxcam


class ScreenCapture:
    camera = None

    # constructor
    def __init__(self, window_name):
        self.camera = dxcam.create(output_color="BGR")

    def startCapture(self):

        # Start Camera
        self.camera.start(target_fps=60)

    def getCapture(self):

        #Take in frame
        frame = self.camera.get_latest_frame()

        return frame

    def stopCapture(self):

        # Stop Camera and delete it's resources
        self.camera.stop()
        del self.camera
