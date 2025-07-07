import pygame
from path import draw_track
from robot import Robot
from settings import WIDTH, HEIGHT, FPS, WHITE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
robot = Robot(100, 500)  # Start at path beginning
pygame.display.set_caption("Line Follower Simulation")
clock = pygame.time.Clock()

running = True
while running:
    screen.fill(WHITE)
    draw_track(screen)
    robot.update(screen)
    robot.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
