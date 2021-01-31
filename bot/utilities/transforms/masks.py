import cv2
import numpy as np


def rgb_to_hsv(focus_window):
    hsv = cv2.cvtColor(focus_window, cv2.COLOR_RGB2HSV)
    print(hsv)
    return hsv


def bgr_to_hsv(focus_window):
    hsv = cv2.cvtColor(focus_window, cv2.COLOR_BGR2HSV)
    print(hsv)
    return hsv


def hsv_map_masked(game_window):
    #                 H  S  V
    lower = np.array([0, 0, 0])
    upper = np.array([150, 150, 255])
    hsv = rgb_to_hsv(game_window)
    mask = cv2.inRange(hsv, lower, upper)
    return mask


#                            H    S    V
RED_PLAYER_MARKER_MASK_LOWER = np.array([100, 200, 140])
RED_PLAYER_MARKER_MASK_UPPER = np.array([130, 255, 200])


def rgb_player_map_masked(game_window, lower=RED_PLAYER_MARKER_MASK_LOWER, upper=RED_PLAYER_MARKER_MASK_UPPER):
    game_window = cv2.cvtColor(game_window, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(game_window, lower, upper)
    # print("min", game_window.min(), "max", game_window.max())
    return mask