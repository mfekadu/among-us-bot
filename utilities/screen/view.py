from grabwindow import grab_window_rgb
import cv2
import numpy as np


PLAYER_BUFFER_X = 75
PLAYER_BUFFER_Y = 100

GAME_MIN_WIDTH = 800
GAME_MIN_HEIGHT = 600

REPORT_BUTTON_BUFFER_X_800x600 = 75
REPORT_BUTTON_BUFFER_Y_800x600 = 75
USE_BUTTON_BUFFER_X_800x600 = 75
USE_BUTTON_BUFFER_Y_800x600 = 60

FIND_USE_BUTTON_CENTER_X_800x600 = lambda n: n - n // 9
FIND_USE_BUTTON_CENTER_Y_800x600 = lambda n: n - n // 9
FIND_REPORT_BUTTON_CENTER_X_800x600 = lambda n: n - n // 9
FIND_REPORT_BUTTON_CENTER_Y_800x600 = lambda n: n - n // 3
FIND_PLAYER_CENTER = lambda n: n // 2


def to_hsv(focus_window):
    hsv = cv2.cvtColor(focus_window, cv2.COLOR_RGB2HSV)
    print(hsv)
    return hsv


def masked(game_window):
    lower = np.array([0, 0, 0])
    upper = np.array([150, 150, 255])
    hsv = cv2.cvtColor(game_window, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    return mask


def focus_crop(game_window, top, bot, left, right):
    return game_window[top:bot, left:right]


def center_buffer_focus_crop(
    game_window,
    center_y_finder=FIND_PLAYER_CENTER,
    center_x_finder=FIND_PLAYER_CENTER,
    buffer_y=PLAYER_BUFFER_Y,
    buffer_x=PLAYER_BUFFER_X,
):
    print("game_window.shape", game_window.shape)
    height, width, ncolors = game_window.shape
    assert (
        height >= GAME_MIN_HEIGHT and width >= GAME_MIN_WIDTH
    ), f"unexpected game_window.shape: {game_window.shape}"
    mid_y = center_y_finder(height)
    mid_x = center_x_finder(width)
    top = mid_y - buffer_y
    bot = mid_y + buffer_y
    left = mid_x - buffer_x
    right = mid_x + buffer_x
    return focus_crop(game_window, top, bot, left, right)


def use_button_focus_crop(
    game_window,
    center_y_finder=FIND_USE_BUTTON_CENTER_Y_800x600,
    center_x_finder=FIND_USE_BUTTON_CENTER_X_800x600,
    buffer_y=USE_BUTTON_BUFFER_Y_800x600,
    buffer_x=USE_BUTTON_BUFFER_X_800x600,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )


def player_focus_crop(
    game_window,
    center_y_finder=FIND_PLAYER_CENTER,
    center_x_finder=FIND_PLAYER_CENTER,
    buffer_y=PLAYER_BUFFER_Y,
    buffer_x=PLAYER_BUFFER_X,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )


def report_button_focus_crop(
    game_window,
    center_y_finder=FIND_REPORT_BUTTON_CENTER_Y_800x600,
    center_x_finder=FIND_REPORT_BUTTON_CENTER_X_800x600,
    buffer_y=REPORT_BUTTON_BUFFER_Y_800x600,
    buffer_x=REPORT_BUTTON_BUFFER_X_800x600,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )


for i in range(1000):
    game_window = grab_window_rgb("Among Us")
    # game_window = masked(game_window)
    player = player_focus_crop(game_window)
    report = report_button_focus_crop(game_window)
    use = use_button_focus_crop(game_window)
    cv2.imshow("game_window", game_window)
    cv2.imshow("player", to_hsv(player))
    cv2.imshow("report", to_hsv(report))
    cv2.imshow("use", to_hsv(use))
    # allow for keyboard input into the game
    cv2.waitKey(10)

cv2.destroyAllWindows()
