from screen.grabwindow import grab_window_rgb
import pyautogui
from screen.constants import FPS_UNLIMITED
import cv2
import numpy as np
from transforms.crops import (
    player_focus_crop,
    report_button_focus_crop,
    use_button_focus_crop,
    cafe_player_calibrate_focus_crop,
)
from transforms.masks import (
    rgb_player_map_masked,
    RED_PLAYER_MARKER_MASK_LOWER,
    RED_PLAYER_MARKER_MASK_UPPER,
)
from cartography.constants import (
    SKELD_FILENAME,
    MIRAHQ_FILENAME,
    POLUS_FILENAME,
    RED_PLAYER_MARKER_FILENAME,
    BROWN_PLAYER_MARKER_FILENAME,
    ORANGE_PLAYER_MARKER_FILENAME,
    YELLOW_PLAYER_MARKER_FILENAME,
    LIME_PLAYER_MARKER_FILENAME,
    GREEN_PLAYER_MARKER_FILENAME,
    CYAN_PLAYER_MARKER_FILENAME,
    BLUE_PLAYER_MARKER_FILENAME,
    PURPLE_PLAYER_MARKER_FILENAME,
    PINK_PLAYER_MARKER_FILENAME,
    WHITE_PLAYER_MARKER_FILENAME,
    BLACK_PLAYER_MARKER_FILENAME,
    RED_PLAYER_MARKER_MASKED_FILENAME,
    BROWN_PLAYER_MARKER_MASKED_FILENAME,
    ORANGE_PLAYER_MARKER_MASKED_FILENAME,
    YELLOW_PLAYER_MARKER_MASKED_FILENAME,
    LIME_PLAYER_MARKER_MASKED_FILENAME,
    GREEN_PLAYER_MARKER_MASKED_FILENAME,
    CYAN_PLAYER_MARKER_MASKED_FILENAME,
    BLUE_PLAYER_MARKER_MASKED_FILENAME,
    PURPLE_PLAYER_MARKER_MASKED_FILENAME,
    PINK_PLAYER_MARKER_MASKED_FILENAME,
    WHITE_PLAYER_MARKER_MASKED_FILENAME,
    BLACK_PLAYER_MARKER_MASKED_FILENAME,
)
from cartography.reader import read_map_data, read_player_marker_image
from cartography.writer import write_map_data, write_player_marker_image
from cartography.common import get_data_path, get_player_marker_path


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


for i in range(10000):
    game_window = grab_window_rgb("Among Us", CONFIG["fps"])
    game_window_masked = rgb_player_map_masked(game_window)
    # img_gray = cv2.cvtColor(game_window_masked, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(CONFIG["marker_masked_path"],0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(game_window_masked,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.5
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(game_window, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    cv2.imshow("game_window", game_window)
    cv2.imshow("game_window_masked", game_window_masked)
    # allow for keyboard input into the game
    cv2.waitKey(10)

cv2.destroyAllWindows()
