import time
from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import pytesseract
import navigate
import tasks
from pytesseract import Output
from utilities.screen.grabwindow import grab_window

# debugging
import inspect


class Bot:
    def __init__(self):
        print("frame", inspect.currentframe().f_code.co_name)
        self.name = "disco"
        self.tasks = None
        print("self", self)

    def menu(self):
        print("What would you like to do?")
        print("[1] Run Bot")
        print("[2] Solve Tasks")
        print("[3] Navigate to Tasks")
        print("[4] Find me")

        option = int(input('options:'))

        if(option == 1):
            self.startup()
        if(option == 2):
            tasks.menu()
        if(option == 3):
            navigate.pathfinding()
        if(option == 4):
            self.find_me()

    def find_me(self):
        print("frame", inspect.currentframe().f_code.co_name)

        # c = pyautogui.locateOnScreen('map_character.png', grayscale=True, confidence=.65)
        # pyautogui.moveTo(c)

    def startup(self):
        print("frame", inspect.currentframe().f_code.co_name)
        time.sleep(2)
        self.width = 1920
        self.height = 1080
        self.dim = (self.width, self.height)
        img = grab_window("Among Us")
        self.read_map(img)

    def read_map(self, img):
        print("frame", inspect.currentframe().f_code.co_name)
        # while True:
        #     pyautogui.press("tab")
        #     pix = img.load()
        #     task = None
        #     for t in tasks_loc:
        #         if pix[t[1]] > (190, 190, 0) and pix[t[1]] < (255, 255, 80) and pix[t[1]][2] < 200 and pix[t[1]][1] != 17:
        #             print(t[0])
        #             print(pix[t[1]])
        #             task = t
        #     if task is not None:
        #         result = navigate.pathfinding(tasks_loc.index(task))
        #         pyautogui.press("tab")
        #         if result is 1:
        #             self.perform_task(task)

    def perform_task(self, task):
        # if task[0] != "Unlock Manifolds":
        #     tasks.start_task()
        # task[2]()
    
bot = Bot()
bot.menu()