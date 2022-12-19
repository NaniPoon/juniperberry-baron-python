# print("test environment")
import os
import cv2 as cv
import numpy as np
import pyautogui

os.chdir(os.path.dirname(os.path.abspath(__file__)))

while (True):

    #take in screenshot
    windowinput = pyautogui.screenshot()

    #convert windowinput to numpy
    windowinput = np.array(windowinput)

    #convert from rgb tp bgr
    windowinput = cv.cvtColor(windowinput, cv.COLOR_RGB2BGR)

    cv.imshow('Juniper Berry Baron', windowinput)

    if cv.waitKey(1) == ord("-"):
        cv.destroyAllWindows()
        break


print("Exited")