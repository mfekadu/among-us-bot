import win32gui, win32ui, win32con, win32api
from PIL import ImageGrab
import time


def grab_window(name="Among Us"):
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
    win32gui.SetForegroundWindow(hwnd)
    bbox = win32gui.GetWindowRect(hwnd)
    time.sleep(1)
    img = ImageGrab.grab(bbox)
    # img.show() # for debugging
    return img