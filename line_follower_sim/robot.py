import pygame
from settings import BLUE

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = BLUE
        self.speed = 1
        self.goal_x = 700
        self.goal_y = 200
        self.goal_radius = 25
        self.reached_goal = False


        # Sensor offset distance (from center)
        self.sensor_offset = 20
        self.sensor_gap = 20  # vertical distance between sensors

    def draw(self, screen):
        # Draw robot body
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        # Sensor positions ahead of the robot
        sensor_x = self.x + self.sensor_offset
        sensors = [
            (sensor_x, self.y - self.sensor_gap),  # Top
            (sensor_x, self.y),                    # Center
            (sensor_x, self.y + self.sensor_gap)   # Bottom
        ]

        # Draw green dots at sensor positions
        for sx, sy in sensors:
            pygame.draw.circle(screen, (0, 255, 0), (int(sx), int(sy)), 3)

    def get_sensor_data(self, screen):
        sensor_x = self.x + self.sensor_offset
        sensors = [
            (sensor_x, self.y - self.sensor_gap),  # Top
            (sensor_x, self.y),                    # Center
            (sensor_x, self.y + self.sensor_gap)   # Bottom
        ]

        readings = []
        for i, (sx, sy) in enumerate(sensors):
            color = screen.get_at((int(sx), int(sy)))[:3]
            is_black = color == (0, 0, 0)
            readings.append(is_black)

            position = ["Top", "Center", "Bottom"][i]
            print(f"{position} Sensor at ({int(sx)}, {int(sy)}) sees color: {color} → {'BLACK' if is_black else 'NOT BLACK'}")

        return readings  # [Top, Center, Bottom]
    
    def update(self, screen):
    # Stop if goal is already reached
        if self.reached_goal:
            return

        self.speed = 1  # Reset speed each frame

    # Get sensor readings
        left, center, right = self.get_sensor_data(screen)
    
        dx = self.x - self.goal_x
        dy = self.y - self.goal_y
        distance = (dx**2 + dy**2)**0.5

        if distance < self.goal_radius:
            self.reached_goal = True
            print("🎉 Goal Reached!")
            return
    # Movement logic
        if center:
            self.x += self.speed  # Go straight
        elif left:
            self.x += self.speed / 2  # turn left
            self.y -= self.speed / 2
        elif right:
            self.x += self.speed / 2  # turn right
            self.y += self.speed / 2
        else:
            self.x += 0.3 # Do nothing if no black line detected

          