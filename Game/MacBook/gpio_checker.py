from gpiozero import Button


def _gpio_to_binary(buttons: list[Button]):
    """
    Convert a list of Button objects to a binary string representation based on their states.

    :param buttons: A list of Button objects where each object has a 'state' attribute.
    :type buttons: list[Button]
    :return: A binary string representing the states of the given Button objects.
    :rtype: str
    """
    binary = ""
    for button in buttons:
        binary += str(button.value)
    return binary


def check_gpio(button_sequence, desired_sequence: str) -> bool:
    """
    Checks if the binary sequence generated from the provided GPIO button sequence matches
    the desired sequence.

    :param button_sequence: Sequence of GPIO Buttons to be converted to binary.
    :type button_sequence: list[int]
    :param desired_sequence: Binary value to compare with the converted GPIO button sequence.
    :type desired_sequence: str
    :return: Returns True if the binary sequence matches the supplied answer, otherwise
        returns False.
    :rtype: bool
    """
    binary_sequence = _gpio_to_binary(button_sequence)
    return binary_sequence == desired_sequence
