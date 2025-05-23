
def hexadecimal_to_binary(letter):
    """
    converts a single hexadecimal character to its binary coded equivalent as a
    4-bit string.
    :param letter: a single character representing a hexadecimal digit.
    :type letter: str
    :return: The 4-bit binary representation of the input character.
    :rtype: str
    :raises KeyError: If the input character is not valid and not found in the
        predefined conversion dictionary.
    """
    conversion = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111"
    }

    return conversion[letter]


def binary_to_hexadecimal(coding):
    """
    convert a 4-bit binary string to its hexadecimal representation.

    :param coding: a 4-bit binary string.
    :return: the hexadecimal representation of the binary input as a string.
    :rtype: str
    """
    conversion = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F"
    }

    return conversion[coding]
