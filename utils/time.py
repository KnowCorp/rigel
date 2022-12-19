from utils.print import console_print

import time


def print_time(initial_time, msg: str = "") -> None:
    """
    Print the time elapsed since the initial time

    The function takes two arguments:

    - `initial_time`: The initial time
    - `msg`: The message to print

    The function returns `None`

    :param initial_time: The time at which the function was called
    :param msg: The message to print
    :type msg: str
    """

    final_time = time.time()
    total_time = f"{(final_time - initial_time):.5f}"

    console_print(msg=msg, status=total_time)
