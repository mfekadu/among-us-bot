import cv2
import numpy as np

from .constants import SKELD_FILENAME, SKELD_IMAGE_FILENAME
from .reader import read_map_data
from .writer import write_map_data_image


def visualize_map_data(filename=SKELD_FILENAME):
    arr = np.full((1000, 1000, 3), 0)
    data = read_map_data(filename)
    print("read_map_data complete")
    for k, v in data.items():
        x, y = eval(k)
        arr[y][x] = (255, 255, 255) if v else (0, 0, 0)
    write_map_data_image(arr, SKELD_IMAGE_FILENAME)
    cv2.imshow(SKELD_IMAGE_FILENAME, arr)
