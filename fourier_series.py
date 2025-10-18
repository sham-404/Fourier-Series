import pygame
import math 

WIDTH = 800
HEIGHT = 350
FPS = 40

def main():
    rad = 0
    y_arr = []
    points = []

    def update():
        nonlocal rad
        rad += 0.0005

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    frame_count = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((10, 10, 10))

        center = (200, HEIGHT // 2)
        radius = 100
        pygame.draw.aacircle(screen, (70, 70, 70), center, radius, 1)

        x = center[0] + radius * math.sin(math.degrees(rad))
        y = center[1] + radius * math.cos(math.degrees(rad))
        y_arr.insert(0, y)

        pygame.draw.aacircle(screen, (225, 225, 225), (x, y), 3)
        pygame.draw.aaline(screen, (100, 100, 100), center, (x, y), 1)

        points = [(i, y) for i, y in enumerate(y_arr, 450)]
        if len(points) > 1:
            pygame.draw.aalines(screen, (0, 200, 0), False, points)
        if len(y_arr) > 200:
            y_arr.pop()

        update()

        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()

main()
