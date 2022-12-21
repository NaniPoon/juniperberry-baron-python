# print("test environment")
import os
import cv2 as cv
import numpy as np
import pyautogui
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

loop_time = time()
while (True):

    #take in screenshot
    windowinput = pyautogui.screenshot()

    #convert windowinput to numpy
    windowinput = np.array(windowinput)

    #convert from rgb tp bgr
    windowinput = cv.cvtColor(windowinput, cv.COLOR_RGB2BGR)

    cv.imshow('Juniper Berry Baron', windowinput)
    print(f'FPS {format(1 / (time() - loop_time))}')
    loop_time = time()

    if cv.waitKey(1) == ord("-"):
        cv.destroyAllWindows()
        break


print("Exited")