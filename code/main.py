import os
import cv2 as cv
from screencapture import ScreenCapture
from time import time


os.chdir(os.path.dirname(os.path.abspath(__file__)))
screenCap = ScreenCapture('Maple')
loopTime = time()
screenCap.startCapture()

while True:

    frame = screenCap.getCapture()
    cv.imshow('Juniper Berry Baron', frame)
    print(f'FPS {format(1 / (time() - loopTime))}')
    loopTime = time()

    if cv.waitKey(1) == ord("-"):
        cv.destroyAllWindows()
        screenCap.stopCapture()
        break


print("Exited")



