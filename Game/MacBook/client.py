import socket
import pygame
import pygame_gui

# Initialize Pygame
pygame.init()

# Create Server
SERVER, PORT = "127.0.0.1", 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect Client
server.connect((SERVER, PORT))

# Test Message
message = server.recv(1024).decode()
letters = message[:2]
dot_states = message[2:]
print(letters)
print(dot_states)

# Create Window
pygame.display.set_caption('Hexadecimal Game')
window_surface = pygame.display.set_mode((800, 600))

# Background
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# Create Manager
manager = pygame_gui.UIManager((800, 600))

# Initialize a Font object
font = pygame.font.Font(None, 160)  # None will use the default font, 160 is the size

# Render the character onto a new surface
character_surface = font.render(letters, True, pygame.Color('#FFFFFF'))  # Change 'A' to whatever character you want

# Get the size of the rendered character
char_width, char_height = character_surface.get_size()

# Calculate position to centre the character
center_x = (800 - char_width) // 2  # 800 is the screen width
center_y = (600 - char_height) // 2  # 600 is the screen height

# Bit Colours
GREEN = pygame.Color('green')
GRAY = pygame.Color('gray')

# Dot settings
num_dots = 8
dot_radius = 10
dot_y = 500

# Distribute dots evenly across the screen width
dot_spacing = 800 // (num_dots + 1)  # Spacing between dots
dot_positions = [(dot_spacing * (i + 1), dot_y) for i in range(num_dots)]

# Runtime variables
clock = pygame.time.Clock()
running = True

# Main Loop
while running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))

    # Draw the character at the calculated position
    window_surface.blit(character_surface, (center_x, center_y))

    # Draw the dots
    for i, (x, y) in enumerate(dot_positions):
        color = GREEN if dot_states[i] == "1" else GRAY
        pygame.draw.circle(window_surface, color, (x, y), dot_radius)

    manager.draw_ui(window_surface)

    pygame.display.update()


server.close()
