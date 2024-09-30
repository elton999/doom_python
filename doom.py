import pygame
import math

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

def Draw3D():
    worldX = [0,0,0,0]
    worldY = [0,0,0,0]
    worldZ = [0,0,0,0]

    cs = math.radians(math.cos(cameraA))
    sn = math.radians(math.sin(cameraA))
    
    x1 = 40 - cameraX
    y1 = 10 - cameraY

    x2 = 40 - cameraX
    y2 = 290 - cameraY

    worldX[0] = x1 - y1
    worldX[1] = x2 - y2 

    worldY[0] = y1 + x1
    worldY[1] = y2 + x2

    worldZ[0] = 0 - cameraZ + ((cameraL * worldY[0]) / 32)
    worldZ[1] = 0 - cameraZ + ((cameraL * worldY[1]) / 32)

    worldX[0] = worldX[0] * 200 / worldY[0] + 200
    worldY[0] = worldZ[0] * 200 / worldY[0] + 200
    worldX[1] = worldX[1] * 200 / worldY[1] + 200
    worldY[1] = worldZ[1] * 200 / worldY[1] + 200

    pygame.draw.rect(screen, "blue", pygame.Rect(worldX[0], worldY[0], pixelSize, pixelSize))
    pygame.draw.rect(screen, "blue", pygame.Rect(worldX[1], worldY[1], pixelSize, pixelSize))

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
    Draw3D()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()



