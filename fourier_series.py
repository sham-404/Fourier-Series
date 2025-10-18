import pygame
import math 

WIDTH = 800
HEIGHT = 350
FPS = 60

def update():
    pass

def main():
    rad = 0

    def update():
        nonlocal rad
        rad += 0.0005

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((10, 10, 10))

        center = (200, HEIGHT // 2)
        radius = 100
        pygame.draw.aacircle(screen, (70, 70, 70), center, radius, 2)
        update()
        x = center[0] + radius * math.sin(math.degrees(rad))
        y = center[1] + radius * math.cos(math.degrees(rad))
        pygame.draw.aacircle(screen, (225, 225, 225), (x, y), 3)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

main()
