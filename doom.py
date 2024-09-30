import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

SH = 200
SW = 200

pixelSize = 4
cameraX =  70
cameraY =  -110 
cameraZ = 20
cameraA = 0
cameraL = 0

pixels = []

def SetUp():
    for x in range(SW):
        pixels.append([])
        for y in range(SH):
            pixels[x].append("black")

def Clear():
    for x in range(SW):
        for y in range(SH):
            pixels[x][y] = "white"

def Render():
    if cameraX > 0 and cameraX < SW and cameraY> 0 and cameraY < SH:
        pixels[int(cameraX)][int(cameraY)] = "red"
    for x in range(SW):
        for y in range(SH):
            pygame.draw.rect(screen, pixels[x][y], pygame.Rect(x * pixelSize, y * pixelSize, pixelSize, pixelSize))


def Draw3D():
    worldX = [0,0,0,0]
    worldY = [0,0,0,0]
    worldZ = [0,0,0,0]

    cs = math.cos(math.radians(cameraA))
    sn = math.sin(math.radians(cameraA))
    
    x1 = 40 - cameraX
    y1 = 10 - cameraY

    x2 = 40 - cameraX
    y2 = 290 - cameraY

    worldX[0] = x1 * cs - y1 * sn
    worldX[1] = x2 * cs - y2 * sn

    worldY[0] = y1 * cs + x1 * sn
    worldY[1] = y2 * cs + x2 * sn

    worldZ[0] = 0 - cameraZ + ((cameraL * worldY[0]) / 32)
    worldZ[1] = 0 - cameraZ + ((cameraL * worldY[1]) / 32)

    worldX[0] = worldX[0] * 200 / worldY[0] + (SW / 2)
    worldY[0] = worldZ[0] * 200 / worldY[0] + (SH / 2)
    worldX[1] = worldX[1] * 200 / worldY[1] + (SW / 2)
    worldY[1] = worldZ[1] * 200 / worldY[1] + (SH / 2)

    if worldX[0] > 0 and worldX[0] < SW and worldY[0] > 0 and worldY[0] < SH:
        pixels[int(worldX[0])][int(worldY[0])] = "blue"
    if worldX[1] > 0 and worldX[1] < SW and worldY[1] > 0 and worldY[1] < SH:
        pixels[int(worldX[1])][int(worldY[1])] = "blue"

SetUp()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not keys[pygame.K_LSHIFT]:
        cameraA -=  4
        if(cameraA < 0):
            cameraA += 360
    if keys[pygame.K_d] and not keys[pygame.K_LSHIFT]:
        cameraA +=   4
        if(cameraA > 359):
            cameraA -= 360

    dx = math.radians(math.sin(cameraA)) * 10
    dy = math.radians(math.cos(cameraA)) * 10

    if keys[pygame.K_w] and not keys[pygame.K_m]:
        cameraX += dx
        cameraY += dy
    if keys[pygame.K_s] and not keys[pygame.K_m]:
        cameraX -= dx
        cameraY -= dy
    
    if keys[pygame.K_RIGHT]:
        cameraX += dx
        cameraY -= dy
    if keys[pygame.K_LEFT]:
        cameraX -= dx
        cameraY += dy
        
    if keys[pygame.K_a] and keys[pygame.K_m]:
        cameraL -= 1
    if keys[pygame.K_d] and keys[pygame.K_m]:
        cameraL += 1
    if keys[pygame.K_w] and keys[pygame.K_m]:
        cameraZ -= 4
    if keys[pygame.K_s] and keys[pygame.K_m]:
        cameraZ += 4

    screen.fill("white")
    Clear()
    Draw3D()
    Render()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()