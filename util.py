import datetime
import time
from threading import Thread

from zxtouch.client import zxtouch
from zxtouch.touchtypes import TOUCH_DOWN, TOUCH_UP


IPHONE_ADDRESS = "192.168.31.70"
REFRESH_GAP = 0.01
COLOR_GAP = 10

device = zxtouch(IPHONE_ADDRESS)


def click(x, y):
    device.touch(TOUCH_DOWN, 5, x, y)
    device.touch(TOUCH_UP, 5, x, y)


def color_equal(color, target):
    try:
        red = int(color["red"].strip().replace("\r\n0", ""))
        green = int(color["green"].strip().replace("\r\n0", ""))
        blue = int(color["blue"].strip().replace("\r\n0", ""))
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
    device = zxtouch(IPHONE_ADDRESS)
    num = 0
    while True:
        now_color = device.pick_color(*position)[1]
        # print(f"{btn_name} {position}, target color: {target_color}  now color: {now_color}")
        if color_equal(now_color, target_color):
            click(*position)
            num += 1
            print(f"{datetime.datetime.now()}       click {btn_name} button!  {num}")
        time.sleep(REFRESH_GAP)


def run(btn_list):
    for btn in btn_list:
        t = Thread(target=click_forever, args=(btn["btn_name"], btn["position"], btn["color"]))
        t.start()
