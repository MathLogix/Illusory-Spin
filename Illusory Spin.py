import pygame
import math
import sys

WIDTH, HEIGHT = 800, 800
CENTER = WIDTH // 2, HEIGHT // 2
RADIUS = 300
NUM_LINES = 16
# NUM_LINES = 48
NUM_BALLS = NUM_LINES // 2
DELAY_FRAMES = 20
AMPLITUDE = 300
SPEED = 0.02
BALL_RADIUS = 10
FPS = 100

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Illusory Spin")
clock = pygame.time.Clock()

all_angles = [2 * math.pi * i / NUM_LINES for i in range(NUM_LINES)]

ball_angles = all_angles[:NUM_BALLS]

frame_count = 0

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (100, 100, 100), CENTER, RADIUS, 1)

    for angle in all_angles:
        x_end = CENTER[0] + RADIUS * math.cos(angle)
        y_end = CENTER[1] + RADIUS * math.sin(angle)
        pygame.draw.line(screen, (50, 50, 50), CENTER, (x_end, y_end), 1)

    for i, angle in enumerate(ball_angles):
        x_end = CENTER[0] + RADIUS * math.cos(angle)
        y_end = CENTER[1] + RADIUS * math.sin(angle)

        delay = i * DELAY_FRAMES
        t = (frame_count - delay) * SPEED

        if t < 0:
            ball_x = x_end
            ball_y = y_end
        else:
            pos = AMPLITUDE * math.cos(t)
            ball_x = CENTER[0] + pos * math.cos(angle)
            ball_y = CENTER[1] + pos * math.sin(angle)

        pygame.draw.circle(screen, (0, 150, 255), (int(ball_x), int(ball_y)), BALL_RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)
    frame_count += 1

pygame.quit()
sys.exit()