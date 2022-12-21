from datetime import datetime
from .color import Color

import logging
import emojis

logging.basicConfig(level=logging.INFO)


def console_print(msg: str = None, status: str = None, **kwargs) -> None:
    """
    It takes a message and a status code and prints them to the console with colors and emojis

    :param msg: str = None, status: str = None, **kwargs
    :type msg: str
    :param status: str = None,
    :type status: str
    """

    if msg is None or status is None:
        date = datetime.now().strftime("%Y%m%d %X")

        for key, value in kwargs.items():
            value = str(value)

            if key == "error":
                logging.error(
                    emojis.encode(
                        f":no_entry: {Color.RED}{value}{Color.END} [ {Color.YELLOW}{date}{Color.END} ]"
                    )
                )
            elif key == "warning":
                logging.warning(
                    emojis.encode(
                        f":warning: {Color.YELLOW}{value}{Color.END} [ {Color.YELLOW}{date}{Color.END} ]"
                    )
                )
            elif key == "info":
                logging.info(
                    emojis.encode(
                        f" :information_source: {Color.CYAN}{value}{Color.END} [ {Color.YELLOW}{date}{Color.END} ]"
                    )
                )
            elif key == "success":
                logging.info(
                    emojis.encode(
                        f":ok: {Color.GREEN}{value}{Color.END} [ {Color.YELLOW}{date}{Color.END} ]"
                    )
                )
            elif key == "debug":
                logging.info(
                    emojis.encode(
                        f":snake: {Color.PURPLE}{value}{Color.END} [ {Color.YELLOW}{date}{Color.END} ]"
                    )
                )
            else:
                logging.info(
                    emojis.encode(
                        f":heavy_minus_sign: {Color.BOLD}{value}{Color.END} [ {Color.YELLOW}{date}{Color.END} ]"
                    )
                )

    else:
        logging.info(
            emojis.encode(
                f":snake: {Color.PURPLE}{msg} [ {Color.YELLOW}{status}{Color.PURPLE} ]{Color.END}"
            )
        )
