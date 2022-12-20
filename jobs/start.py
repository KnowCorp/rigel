from utils.print import console_print
from Questgen import main


def get_state_message(rigel_state):
    if rigel_state:
        state_message = "up"
    else:
        state_message = "down"

    return state_message


def start_rigel():
    """
    It starts the background task to keep the model and Rigel state up

    :return: The rigel object and the rigel_state object
    """

    rigel = main.QGen()

    rigel_state = rigel.get_rigel_state()

    state_message = get_state_message(rigel_state)

    console_print(msg="rigel", status=state_message)

    return rigel, rigel_state
