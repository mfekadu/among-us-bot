import cv2
import numpy as np
import pyautogui

from cartography.common import get_data_path, get_player_marker_path
from cartography.constants import (
    BLACK_PLAYER_MARKER_FILENAME,
    BLACK_PLAYER_MARKER_MASKED_FILENAME,
    BLUE_PLAYER_MARKER_FILENAME,
    BLUE_PLAYER_MARKER_MASKED_FILENAME,
    BROWN_PLAYER_MARKER_FILENAME,
    BROWN_PLAYER_MARKER_MASKED_FILENAME,
    CYAN_PLAYER_MARKER_FILENAME,
    CYAN_PLAYER_MARKER_MASKED_FILENAME,
    GREEN_PLAYER_MARKER_FILENAME,
    GREEN_PLAYER_MARKER_MASKED_FILENAME,
    LIME_PLAYER_MARKER_FILENAME,
    LIME_PLAYER_MARKER_MASKED_FILENAME,
    MIRAHQ_FILENAME,
    ORANGE_PLAYER_MARKER_FILENAME,
    ORANGE_PLAYER_MARKER_MASKED_FILENAME,
    PINK_PLAYER_MARKER_FILENAME,
    PINK_PLAYER_MARKER_MASKED_FILENAME,
    POLUS_FILENAME,
    PURPLE_PLAYER_MARKER_FILENAME,
    PURPLE_PLAYER_MARKER_MASKED_FILENAME,
    RED_PLAYER_MARKER_FILENAME,
    RED_PLAYER_MARKER_MASKED_FILENAME,
    SKELD_FILENAME,
    WHITE_PLAYER_MARKER_FILENAME,
    WHITE_PLAYER_MARKER_MASKED_FILENAME,
    YELLOW_PLAYER_MARKER_FILENAME,
    YELLOW_PLAYER_MARKER_MASKED_FILENAME,
)
from cartography.reader import read_map_data, read_player_marker_image
from cartography.writer import write_map_data, write_player_marker_image
from screen.constants import FPS_UNLIMITED
from screen.grabwindow import grab_window_rgb
from transforms.crops import (
    cafe_player_calibrate_focus_crop,
    player_focus_crop,
    report_button_focus_crop,
    use_button_focus_crop,
)
from transforms.masks import (
    RED_PLAYER_MARKER_MASK_LOWER,
    RED_PLAYER_MARKER_MASK_UPPER,
    rgb_player_map_masked,
)

CONFIG = {
    "map_filename": SKELD_FILENAME,
    "marker_filename": RED_PLAYER_MARKER_FILENAME,
    "marker_path": get_player_marker_path(RED_PLAYER_MARKER_FILENAME),
    "marker_masked_filename": RED_PLAYER_MARKER_MASKED_FILENAME,
    "marker_masked_path": get_player_marker_path(RED_PLAYER_MARKER_MASKED_FILENAME),
    "marker_mask_lower": RED_PLAYER_MARKER_MASK_LOWER,
    "marker_mask_upper": RED_PLAYER_MARKER_MASK_UPPER,
    "fps": FPS_UNLIMITED,
    "do_write_marker": False,  # flip to capture jpgs
}

data = read_map_data(CONFIG["map_filename"])
print("completed reading the data")


def draw_bounding_boxes(game_window, locations, width, height):
    # TODO: another func for just 1 bounding box rather than many locations
    for pt in zip(*locations[::-1]):
        cv2.rectangle(game_window, pt, (pt[0] + width, pt[1] + height), (0, 0, 255), 2)


def locateInGameWindow(game_window, game_window_masked, template, threshold=0.65):
    # TODO: another func for just 1 bounding box rather than many locations
    res = cv2.matchTemplate(game_window_masked, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(res >= threshold)
    return locations


for i in range(10000):
    game_window = grab_window_rgb("Among Us", CONFIG["fps"])
    game_window_masked = rgb_player_map_masked(game_window)
    # img_gray = cv2.cvtColor(game_window_masked, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(CONFIG["marker_masked_path"], 0)
    template_width, template_height = template.shape[::-1]
    locations = locateInGameWindow(game_window, game_window_masked, template)
    draw_bounding_boxes(game_window, locations, template_width, template_height)
    cv2.imshow("game_window", game_window)
    cv2.imshow("game_window_masked", game_window_masked)
    # allow for keyboard input into the game
    cv2.waitKey(10)

cv2.destroyAllWindows()
