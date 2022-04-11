from util import run


OK_POSITION = (400, 1000)
OK_COLOR = (47, 204, 48)
# OK_COLOR = (67, 209, 68)


SUBMIT_POSITION = (700, 1550)
SUBMIT_COLOR = (254, 72, 41)
# SUBMIT_COLOR = (254, 128, 106)


PAY_POSITION = (700, 1670)
PAY_COLOR = (255, 58, 38)


btn_list = [
    {"btn_name": "ok", "position": OK_POSITION, "color": OK_COLOR},
    {"btn_name": "submit", "position": SUBMIT_POSITION, "color": SUBMIT_COLOR},
    {"btn_name": "pay", "position": PAY_POSITION, "color": PAY_COLOR},
]


if __name__ == "__main__":
    run(btn_list)
