PLAYER_BUFFER_X = 75
PLAYER_BUFFER_Y = 100

GAME_MIN_WIDTH = 800
GAME_MIN_HEIGHT = 600

REPORT_BUTTON_BUFFER_X_800x600 = 75
REPORT_BUTTON_BUFFER_Y_800x600 = 75
USE_BUTTON_BUFFER_X_800x600 = 75
USE_BUTTON_BUFFER_Y_800x600 = 60

FIND_USE_BUTTON_CENTER_X_800x600 = lambda n: n - n // 9
FIND_USE_BUTTON_CENTER_Y_800x600 = lambda n: n - n // 9
FIND_REPORT_BUTTON_CENTER_X_800x600 = lambda n: n - n // 9
FIND_REPORT_BUTTON_CENTER_Y_800x600 = lambda n: n - n // 3
FIND_PLAYER_CENTER = lambda n: n // 2


def focus_crop(game_window, top, bot, left, right):
    return game_window[top:bot, left:right]


def center_buffer_focus_crop(
    game_window,
    center_y_finder=FIND_PLAYER_CENTER,
    center_x_finder=FIND_PLAYER_CENTER,
    buffer_y=PLAYER_BUFFER_Y,
    buffer_x=PLAYER_BUFFER_X,
):
    print("game_window.shape", game_window.shape)
    height, width, ncolors = game_window.shape
    assert (
        height >= GAME_MIN_HEIGHT and width >= GAME_MIN_WIDTH
    ), f"unexpected game_window.shape: {game_window.shape}"
    mid_y = center_y_finder(height)
    mid_x = center_x_finder(width)
    top = mid_y - buffer_y
    bot = mid_y + buffer_y
    left = mid_x - buffer_x
    right = mid_x + buffer_x
    return focus_crop(game_window, top, bot, left, right)


def use_button_focus_crop(
    game_window,
    center_y_finder=FIND_USE_BUTTON_CENTER_Y_800x600,
    center_x_finder=FIND_USE_BUTTON_CENTER_X_800x600,
    buffer_y=USE_BUTTON_BUFFER_Y_800x600,
    buffer_x=USE_BUTTON_BUFFER_X_800x600,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )


def player_focus_crop(
    game_window,
    center_y_finder=FIND_PLAYER_CENTER,
    center_x_finder=FIND_PLAYER_CENTER,
    buffer_y=PLAYER_BUFFER_Y,
    buffer_x=PLAYER_BUFFER_X,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )


def report_button_focus_crop(
    game_window,
    center_y_finder=FIND_REPORT_BUTTON_CENTER_Y_800x600,
    center_x_finder=FIND_REPORT_BUTTON_CENTER_X_800x600,
    buffer_y=REPORT_BUTTON_BUFFER_Y_800x600,
    buffer_x=REPORT_BUTTON_BUFFER_X_800x600,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )


FIND_CAFE_PLAYER_CALIBRATE_CENTER_Y_800x600 = lambda n: n//2 - n//6 + n//128
FIND_CAFE_PLAYER_CALIBRATE_CENTER_X_800x600 = lambda n: n//2 - n//256
CAFE_PLAYER_CALIBRATE_BUFFER_Y_800x600 = 10
CAFE_PLAYER_CALIBRATE_BUFFER_X_800x600 = 10
def cafe_player_calibrate_focus_crop(
    game_window,
    center_y_finder=FIND_CAFE_PLAYER_CALIBRATE_CENTER_Y_800x600,
    center_x_finder=FIND_CAFE_PLAYER_CALIBRATE_CENTER_X_800x600,
    buffer_y=CAFE_PLAYER_CALIBRATE_BUFFER_Y_800x600,
    buffer_x=CAFE_PLAYER_CALIBRATE_BUFFER_X_800x600,
):
    return center_buffer_focus_crop(
        game_window, center_y_finder, center_x_finder, buffer_y, buffer_x
    )
