import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
import time
import cv2
import numpy as np

# frames per second
ONE_SECOND = 1
FPS_1 = ONE_SECOND
FPS_2 = ONE_SECOND / 2
FPS_4 = ONE_SECOND / 4
FPS_8 = ONE_SECOND / 8
FPS_16 = ONE_SECOND / 16
FPS_24 = ONE_SECOND / 24
FPS_30 = ONE_SECOND / 30
FPS_32 = ONE_SECOND / 32
FPS_60 = ONE_SECOND / 60
FPS_120 = ONE_SECOND / 120


def __grab_window_handle(name="Among Us", fps=FPS_30):
    # https://stackoverflow.com/questions/3260559/how-to-get-a-window-or-fullscreen-screenshot-in-python-3k-without-pil
    toplist, winlist = [], []
    win32gui.EnumWindows(
        lambda hwnd, res: winlist.append((hwnd, win32gui.GetWindowText(hwnd))), toplist
    )
    handles = [(hwnd, title) for hwnd, title in winlist if name in title]
    assert len(handles) >= 1, f"failed to find window by name: {name}"
    assert len(handles[0]) >= 1, f"weird length for first handle: {len(handles[0])}"
    # just grab the hwnd for first window matching {name}
    hwnd = handles[0][0]
    return hwnd


def __grab_window_bbox_and_hwnd(name="Among Us", fps=FPS_30):
    hwnd = __grab_window_handle(name, fps)
    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    return bbox, hwnd


def __grab_window_bbox_and_setup_nicely_on_screen(name="Among Us", fps=FPS_30):
    bbox, hwnd = __grab_window_bbox_and_hwnd(name, fps)
    x_pos_1, y_pos_1, x_pos_2, y_pos_2 = bbox
    width = x_pos_2 - x_pos_1
    height = y_pos_2 - y_pos_1
    _, _, desktop_width, desktop_height = win32gui.GetWindowRect(
        win32gui.GetDesktopWindow()
    )
    # print(bbox, (width, height), (desktop_width, desktop_height))
    if x_pos_2 > desktop_width:
        difference = desktop_width - x_pos_2
        x_pos_1 = x_pos_1 + difference
    if y_pos_2 > desktop_height:
        difference = desktop_height - y_pos_2
        y_pos_1 = y_pos_1 + difference
    # keep window on screen for good screenshot
    win32gui.MoveWindow(
        hwnd,
        x_pos_1,
        y_pos_1,
        width,
        height,
        True,
    )
    return bbox


def __grab_window_image(name="Among Us", fps=FPS_30):
    bbox = __grab_window_bbox_and_setup_nicely_on_screen(name, fps)
    time.sleep(fps)
    img = ImageGrab.grab(bbox)
    # img.show() # for debugging
    return img


def grab_window_rgb(name="Among Us", fps=FPS_30):
    img = __grab_window_image(name, fps)
    cv2_img = np.array(img.convert("RGB"))
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    # cv2.imshow("amongus", cv2_img) # for debugging
    return cv2_img
