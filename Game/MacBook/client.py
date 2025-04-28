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
msg = server.recv(1024).__str__()
print(msg)

# Create Window
pygame.display.set_caption('Hexadecimal Game')
window_surface = pygame.display.set_mode((800, 600))

# Background
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# Create Manager
manager = pygame_gui.UIManager((800, 600))

# Buttons
close_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 550), (90, 40)), text='Close',
                                            manager=manager)

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

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == close_button:
                running = False
                break

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()
