import pygame
from settings import BLACK, GREEN, RED

def draw_track(screen):
    # Path points
    path_points = [
        (100, 500),
        (200, 500),
        (300, 400),
        (400, 400),
        (500, 300),
        (600, 300),
        (700, 200)
    ]

    # Draw the black line
    pygame.draw.lines(screen, BLACK, False, path_points, 15)

    # Draw Start Point (Green Circle)
    start_x, start_y = path_points[0]
    pygame.draw.circle(screen, GREEN, (start_x, start_y), 10)

    # Draw End Flag (Red Rectangle)
    end_x, end_y = path_points[-1]
    pygame.draw.rect(screen, RED, (end_x - 10, end_y - 20, 20, 40))  # vertical flag
