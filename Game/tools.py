
def hexadecimal_to_binary(letters):
    """
    converts two hexadecimal characters to its binary coded equivalent as a
    8-bit string.
    :param letters: two characters representing the hexadecimal digits.
    :type letters: str
    :return: The 8-bit binary representation of the input characters.
    :rtype: str
    :raises KeyError: If the input characters are not valid and not found in the
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

    return conversion[letters[0]] + conversion[letters[1]]


def binary_to_hexadecimal(coding):
    """
    convert an 8-bit binary string to its hexadecimal representation.

    :param coding: an 8-bit binary string.
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

    return conversion[coding[:4]] + conversion[coding[4:]]
