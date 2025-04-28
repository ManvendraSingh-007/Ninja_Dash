import pygame
import sys

# Initialize all the Pygame modules
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Create the display surface (the window)
# The screen variable is the surface we'll draw on
screen = pygame.display.set_mode(screen_size)

# Set the window title
pygame.display.set_caption("Simple Pygame Screen")

# Create a clock object to help control the frame rate
clock = pygame.time.Clock()

# --- Main Game Loop ---
running = True 
while running:

    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # Stop the loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # --- Game Logic ---

    # --- Drawing ---
    screen.fill((255, 255, 255))

    # --- Update the Display ---
    pygame.display.flip() # Updates the entire screen

    # --- Control Frame Rate ---
    clock.tick(60)

print("Exiting the game...")
pygame.quit()
sys.exit()