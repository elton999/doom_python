import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

pixelSize = 4
cameraX = pixelSize
cameraY = pixelSize
cameraZ = pixelSize
cameraA = 0
cameraL = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cameraY -= pixelSize
    if keys[pygame.K_s]:
        cameraY += pixelSize
    if keys[pygame.K_a]:
        cameraX -= pixelSize
    if keys[pygame.K_d]:
        cameraX += pixelSize


    pygame.draw.rect(screen, "red", pygame.Rect(cameraX,cameraY, pixelSize, pixelSize))

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()
