from screen.grabwindow import grab_window_rgb
from screen.constants import FPS_UNLIMITED
import cv2
from transforms.crops import (
    player_focus_crop,
    report_button_focus_crop,
    use_button_focus_crop,
    cafe_player_calibrate_focus_crop
)
from transforms.masks import rgb_player_map_masked
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
    BLACK_PLAYER_MARKER_FILENAME
)
from cartography.reader import read_map_data, read_player_marker_image
from cartography.writer import write_map_data, write_player_marker_image
from cartography.common import get_data_path


CONFIG = {
    "map_filename": SKELD_FILENAME,
    "marker_filename": RED_PLAYER_MARKER_FILENAME,
    "fps": FPS_UNLIMITED,
    "do_write_marker": False
}

data = read_map_data(CONFIG["map_filename"])
print("completed reading the data")



for i in range(100):
    game_window = grab_window_rgb("Among Us", CONFIG["fps"])
    player = player_focus_crop(game_window)
    calibrate_spot = cafe_player_calibrate_focus_crop(game_window)
    cv2.imshow("game_window", rgb_player_map_masked(game_window))
    cv2.imshow("player", player)
    cv2.imshow("calibrate_spot", calibrate_spot)
    if CONFIG["do_write_marker"]:
        print("make sure you navigate to the bottom wall of the hallway from Cafe to Upper Engine")
        print("then walk down until you hit the bottom wall")
        print("then run right until you hit the cafe table")
        print("then run this script")
        write_player_marker_image(calibrate_spot, CONFIG["marker_filename"])
        break
    # allow for keyboard input into the game
    cv2.waitKey(10)

cv2.destroyAllWindows()
