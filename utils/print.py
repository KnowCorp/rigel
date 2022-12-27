from datetime import datetime
from .color import Color

import logging
import emojis

logging.basicConfig(level=logging.INFO)

SYSTEM: str = "orion"


def console_print(msg: str = None, status: str = None, **kwargs) -> None:
    """
    It takes a message and a status code and prints them to the console with colors and emojis

    :param msg: str = None, status: str = None, **kwargs
    :type msg: str
    :param status: str = None,
    :type status: str
    """

    system = f"[{Color.BOLD}{SYSTEM.title()}{Color.END}]"

    if msg is None or status is None:
        date = datetime.now().strftime("%Y%m%d %X")

        for key, value in kwargs.items():
            value = str(value)

            if key == "error":
                logging.error(
                    emojis.encode(
                        f" {system} :no_entry: {Color.RED}{value}{Color.END} | {Color.YELLOW}{date}{Color.END}"
                    )
                )
            elif key == "warning":
                logging.warning(
                    emojis.encode(
                        f" {system} :warning: {Color.YELLOW}{value}{Color.END} | {Color.YELLOW}{date}{Color.END}"
                    )
                )
            elif key == "info":
                logging.info(
                    emojis.encode(
                        f"  {system} :information_source: {Color.CYAN}{value}{Color.END} | {Color.YELLOW}{date}{Color.END}"
                    )
                )
            elif key == "success":
                logging.info(
                    emojis.encode(
                        f" {system} :ok: {Color.GREEN}{value}{Color.END} | {Color.YELLOW}{date}{Color.END}"
                    )
                )
            elif key == "debug":
                logging.info(
                    emojis.encode(
                        f" {system} :snake: {Color.PURPLE}{value}{Color.END} | {Color.YELLOW}{date}{Color.END}"
                    )
                )
            else:
                logging.info(
                    emojis.encode(
                        f" {system} :heavy_minus_sign: {Color.BOLD}{value}{Color.END} | {Color.YELLOW}{date}{Color.END}"
                    )
                )

    else:
        logging.info(
            emojis.encode(
                f" {system} :snake: {Color.PURPLE}{msg}{Color.END} | {Color.YELLOW}{status}{Color.END}"
            )
        )
