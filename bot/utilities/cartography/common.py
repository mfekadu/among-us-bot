import os

def get_data_path():
    return os.path.join("..", "..", "data")

def get_map_data_path(filename):
    return os.path.join(get_data_path(), filename)

def get_player_marker_path(filename):
    return os.path.join(get_data_path(), filename)
