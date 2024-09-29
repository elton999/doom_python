import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    pygame.draw.rect(screen, "red", pygame.Rect(400,400, 4, 4))

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()
