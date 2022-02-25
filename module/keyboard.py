import time

import PIL.Image
import pyautogui

from .image import Image
from .logger import logger
from .utils import *


def randomize_values(x, w, y, h):
    x_rand = randomize_int(x, w, 0.20)
    y_rand = randomize_int(y, h, 0.20)
    move_duration = randomize(0.1, 0.5)
    click_duration = randomize(0.05, 0.2)
    time_between = randomize(0.05, 0.3)

    return x_rand, y_rand, move_duration, click_duration, time_between

def click_and_fill_one_target(target: str, input_text: str):
    """click in a target. Returns number of clicks"""
    result = None
    try:
        x_left, y_top, w, h = Image.get_one_target_position(target)
        x, y, move_duration, click_duration, time_between  = randomize_values(x_left, w, y_top, h)
        pyautogui.moveTo(x, y, duration=move_duration, tween=pyautogui.easeOutQuad)
        time.sleep(time_between)
        pyautogui.click(duration=click_duration)
        pyautogui.write(input_text, inteval=0.25)
        result = True
    except Exception as e:
        return None
        # logger(f"Error: {e}")
    
    return result


def click_and_fill_when_target_appears(target: str, input_text: str, time_beteween: float = 0.5, timeout: float = 10):
    """ Click in a target when it appears.
        It will check for target every `time_beteween` seconds.
        After timeout seconds it will return 0 if no target was found.
        Returns 1 if target was found.
    """
    
    return do_with_timeout(click_and_fill_one_target, args = [target, input_text])