import json

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


def read_map_data(filename=SKELD_FILENAME):
    with open(get_map_data_path(filename), "r") as f:
        return json.load(f)


def read_player_marker_image(filename=RED_PLAYER_MARKER_FILENAME):
    path = get_player_marker_path(filename)
    return cv2.imread(path, cv2.IMREAD_COLOR)
