# 山姆抢菜
from util import run

SUBMIT_POSITION = (700, 1600)
SUBMIT_COLOR = (1, 101, 184)
# SAM_COLOR = (38, 68, 93)

PAY_POSITION = (700, 1700)
PAY_COLOR = (1, 101, 184)
# SAM_COLOR = (38, 68, 93)

btn_list = [
    {"btn_name": "submit", "position": SUBMIT_POSITION, "color": SUBMIT_COLOR},
    {"btn_name": "pay", "position": PAY_POSITION, "color": PAY_COLOR},
]


if __name__ == "__main__":
    run(btn_list)
