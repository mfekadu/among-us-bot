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
    MIRAHQ_IMAGE_FILENAME,
    ORANGE_PLAYER_MARKER_FILENAME,
    PINK_PLAYER_MARKER_FILENAME,
    POLUS_FILENAME,
    POLUS_IMAGE_FILENAME,
    PURPLE_PLAYER_MARKER_FILENAME,
    RED_PLAYER_MARKER_FILENAME,
    SKELD_FILENAME,
    SKELD_IMAGE_FILENAME,
    WHITE_PLAYER_MARKER_FILENAME,
    YELLOW_PLAYER_MARKER_FILENAME,
)


def read_map_data(filename=SKELD_FILENAME):
    print("read_map_data", filename)
    with open(get_map_data_path(filename), "r") as f:
        return json.load(f)


def read_image_as_numpy(filepath):
    print(f"read_image_as_numpy: {filepath}")
    # https://stackoverflow.com/questions/7762948/how-to-convert-an-rgb-image-to-numpy-array
    return cv2.imread(filepath, cv2.IMREAD_COLOR)


def read_player_marker_image(filename=RED_PLAYER_MARKER_FILENAME):
    print(f"read_player_marker_image {filename}")
    path = get_player_marker_path(filename)
    return read_image_as_numpy(path)
