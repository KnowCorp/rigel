from utils.print import console_print
from .start import start_rigel

import os


class BackgroundJob:
    def __init__(self, print_settings=False, first_run=False):
        """
        The function is called with the default parameters of print_settings=False and first_run=False

        If first_run is True, the function starts the Orion Nebula If print_settings is True, the function prints the environment

        :param print_settings: Boolean, if True, prints the system configuration, defaults to False
        (optional)
        :param first_run: True if this is the first time the program is being run, defaults to False
        (optional)
        """

        context = os.environ.get("ENVIRONMENT", "dev")

        if first_run:
            self.rigel, self.rigel_state = start_rigel()

        if print_settings:
            console_print(msg="system running on", status=context)
