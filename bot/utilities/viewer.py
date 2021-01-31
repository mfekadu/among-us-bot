from screen.grabwindow import grab_window_rgb
from screen.constants import FPS_UNLIMITED
import cv2
from transforms.crops import (
    player_focus_crop,
    report_button_focus_crop,
    use_button_focus_crop,
)
from transforms.masks import rgb_to_hsv, bgr_to_hsv, hsv_map_masked

for i in range(1000):
    game_window = grab_window_rgb("Among Us", FPS_UNLIMITED)
    # game_window = hsv_map_masked(game_window)
    player = player_focus_crop(game_window)
    report = report_button_focus_crop(game_window)
    use = use_button_focus_crop(game_window)
    cv2.imshow("game_window", game_window)
    cv2.imshow("player", player)
    cv2.imshow("report", report)
    cv2.imshow("use", use)
    # allow for keyboard input into the game
    cv2.waitKey(10)

cv2.destroyAllWindows()
