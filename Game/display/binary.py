import pygame


class Binary:
    def __init__(self, width, height, bit=None, idle=None):
        # Screen Dimensions
        self.width = width
        self.height = height

        # Bit Sequence
        self.bit = bit or pygame.Color('red')
        self.idle = idle or pygame.Color(211, 211, 211)
        self._bit_sequence = "00000000"

    @property
    def sequence(self):
        return self._bit_sequence

    @sequence.setter
    def sequence(self, new_bit_value):
        # Check Length
        if len(new_bit_value) != 8:
            raise ValueError("Binary sequence must be 8 characters long")

        # Check Type
        if type(new_bit_value) is not str:
            raise TypeError("Binary sequence must be a string")

        # Check Characters
        for char in new_bit_value:
            if char not in "01":
                raise ValueError("Binary sequence must only contain 0s and 1s")

        # Set New Value
        self._bit_sequence = new_bit_value

    def draw_binary(self, screen, y_level):
        bit_spacing = self.width // 9
        bit_y = min(y_level, self.height - 8)
        bit_positions = [(bit_spacing * (i + 1), bit_y) for i in range(8)]

        for i, (x, y) in enumerate(bit_positions):
            color = self.bit if self._bit_sequence[i] == "1" else self.idle
            pygame.draw.circle(screen, color, (x, y), 8)
