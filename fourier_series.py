import pygame
import math

WIDTH = 800
HEIGHT = 350
FPS = 60

def main():
    rad = 0
    y_arr = []
    points = []

    def update():
        nonlocal rad
        rad += 0.0006

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    transparent_screen = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    running = True
    frame_count = 0
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        transparent_screen.fill((0, 0, 0, 0))
        screen.fill((10, 10, 10))

        center = (200, HEIGHT // 2)
        x = center[0]
        y = center[1]
        for n in range(1, 20, 2):
            radius = 70 * 4 / (n * math.pi)
            prev_x = x
            prev_y = y

            x += radius * math.cos(n * math.degrees(rad))
            y += radius * math.sin(n * math.degrees(rad))

            # Code to draw the circles and the lines within the circles
            pygame.draw.aaline(screen, (255, 255, 255), (prev_x, prev_y), (x, y), 1)
            pygame.draw.aacircle(transparent_screen, (70, 70, 70, 55), (prev_x, prev_y), radius, 2)

        update()

        # Code that creates the wave pattern
        y_arr.insert(0, y)
        points = [(i, y) for i, y in enumerate(y_arr, 450)]
        if len(points) > 1:
            pygame.draw.aalines(screen, (0, 200, 0), False, points)
            pygame.draw.aaline(screen, (100, 100, 200), (x, y), points[0])
        if len(y_arr) > 400:
            y_arr.pop()



        screen.blit(transparent_screen, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
        frame_count += 1

    pygame.quit()

if __name__ == "__main__":
    main()
