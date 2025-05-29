import pygame


class Hexadecimal:
    def __init__(self, width, height, colour=None):
        self.width = width
        self.height = height

        self.colour = colour or pygame.Color(211, 211, 211)
        self._letters = ""

        # Render the character onto a new surface
        self.font = pygame.font.Font(None, 160)

    @property
    def letters(self):
        return self._letters

    @letters.setter
    def letters(self, new_letters):
        # Check Length
        if len(new_letters) != 2:
            raise ValueError("Hexadecimal sequence must be 2 characters long")

        # I may have forgotten the to write the line below and spent 20 mins troubleshooting, then found that I wasn't
        # actually assigning the new value to the property.
        self._letters = new_letters.upper()

    def draw_hexadecimal(self, screen):
        # TODO: blit characters to surface
        character_surface = self.font.render(self._letters, True, self.colour)

        # Get the size of the rendered character
        char_width, char_height = character_surface.get_size()

        center_x = (self.width - char_width) // 2
        center_y = (self.height - char_height) // 2

        screen.blit(character_surface, (center_x, center_y))
