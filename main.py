import datetime
import time
from threading import Thread


import sys

sys.path.append("./IOS13-SimulateTouch/layout/usr/lib/python3.7/site-packages/")

from zxtouch.client import zxtouch
from zxtouch.touchtypes import TOUCH_DOWN, TOUCH_UP

OK_POSITION = (400, 1000)
OK_COLOR = (47, 204, 48)
# OK_COLOR = (102, 102, 102)

SUBMIT_POSITION = (700, 1550)
SUBMIT_COLOR = (254, 72, 41)
# SUBMIT_COLOR = (254, 128, 106)

PAY_POSITION = (700, 1550)
PAY_COLOR = (254, 72, 41)

REFRESH_GAP = 0.05
COLOR_GAP = 10

device = zxtouch("192.168.31.70")


def click(x, y):
    device.touch(TOUCH_DOWN, 5, x, y)
    device.touch(TOUCH_UP, 5, x, y)


def color_equal(color, target):
    try:
        red = int(color["red"].strip())
        green = int(color["green"].strip())
        blue = int(color["blue"].strip())
    except Exception:
        red, green, blue = 255, 255, 255

    if (
        target[0] - COLOR_GAP <= red <= target[0] + COLOR_GAP
        and target[1] - COLOR_GAP <= green <= target[1] + COLOR_GAP
        and target[2] - COLOR_GAP <= blue <= target[2] + COLOR_GAP
    ):
        return True

    return False


def click_forever(btn_name: str, position: tuple, target_color: tuple):
    while True:
        now_color = device.pick_color(*position)[1]
        print(f"{btn_name} {position}, target color: {target_color}  now color: {now_color}")
        if color_equal(now_color, target_color):
            click(*position)
            print(f"{datetime.datetime.now()}       click {btn_name} button!")
        time.sleep(REFRESH_GAP)


btn_list = [
    {"btn_name": "ok", "position": OK_POSITION, "color": OK_COLOR},
    {"btn_name": "submit", "position": SUBMIT_POSITION, "color": SUBMIT_COLOR},
    # {"btn_name": "pay", "position": PAY_POSITION, "color": PAY_COLOR},
]

for btn in btn_list:
    t = Thread(target=click_forever, args=(btn["btn_name"], btn["position"], btn["color"]))
    t.start()
