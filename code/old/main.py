import os
import cv2 as cv
# from screencapture import ScreenCapture
from screencapture import WindowCapture

from time import time
from vision import Vision
os.chdir(os.path.dirname(os.path.abspath(__file__)))

vision_flower = Vision('flower.png')

# initialize capture object and passing monitor 1
screenCap = ScreenCapture(0)
screenCap = ScreenCapture(0)
WindowCapture
loopTime = time()
screenCap.startCapture()


# export_folder =r"n"

# while True:
#
#     frame = screenCap.getCapture()
#
#
#     print(f'FPS {format(1 / (time() - loopTime))}')
#     loopTime = time()
#     points = vision_flower.find(frame, 0.5, 'rectangles')
#
#
#     if cv.waitKey(1) == ord("-"):
#         cv.destroyAllWindows()
#         screenCap.stopCapture()
#         break
#
#


