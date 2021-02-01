import json

import cv2

from .common import get_map_data_path, get_player_marker_path
from .constants import (
    BLACK_PLAYER_MARKER_FILENAME,
    BLUE_PLAYER_MARKER_FILENAME,
    BROWN_PLAYER_MARKER_FILENAME,
    CYAN_PLAYER_MARKER_FILENAME,
    GREEN_PLAYER_MARKER_FILENAME,
    LIME_PLAYER_MARKER_FILENAME,
    MIRAHQ_FILENAME,
    ORANGE_PLAYER_MARKER_FILENAME,
    PINK_PLAYER_MARKER_FILENAME,
    POLUS_FILENAME,
    PURPLE_PLAYER_MARKER_FILENAME,
    RED_PLAYER_MARKER_FILENAME,
    SKELD_FILENAME,
    WHITE_PLAYER_MARKER_FILENAME,
    YELLOW_PLAYER_MARKER_FILENAME,
)


def write_map_data(data, filename=SKELD_FILENAME):
    print("write_map_data", filename)
    with open(get_map_data_path(filename), "w") as f:
        return json.dump(data, f)


def write_player_marker_image(image, filename=RED_PLAYER_MARKER_FILENAME):
    path = get_player_marker_path(filename)
    return cv2.imwrite(path, image)
