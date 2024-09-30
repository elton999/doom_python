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

def DrawWall(x1 : int , x2 : int, b1 : int,  b2 : int, t1 : int, t2 : int):
    dyb = b2 - b1
    dyt = t2 - t1
    dx = x2 - x1

    if dx == 0:
        dx = 1
    xs = x1

    for x in range(int(x2 - x1)):
        xx = int(x + x1)
        y1 = int(dyb * (xx - xs + 0.5) / dx + b1)
        y2 = int(dyt * (xx - xs + 0.5) / dx + t1)

        for y in range(int(y2 - y1)):
            yy = y + y1
            if xx > 0 and xx< SW and yy > 0 and yy < SH:
                pixels[xx][yy] = "yellow"


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
    worldX[2] = worldX[0]
    worldX[3] = worldX[1]
    
    worldY[0] = y1 * cs + x1 * sn
    worldY[1] = y2 * cs + x2 * sn
    worldY[2] = worldY[0] + 40
    worldY[3] = worldY[1] + 40

    worldZ[0] = 0 - cameraZ + ((cameraL * worldY[0]) / 32)
    worldZ[1] = 0 - cameraZ + ((cameraL * worldY[1]) / 32)

    worldX[0] = worldX[0] * 200 / worldY[0] + (SW / 2)
    worldY[0] = worldZ[0] * 200 / worldY[0] + (SH / 2)
    worldX[1] = worldX[1] * 200 / worldY[1] + (SW / 2)
    worldY[1] = worldZ[1] * 200 / worldY[1] + (SH / 2)

    worldX[2] = worldX[2] * 200 / worldY[2] + (SW / 2)
    worldY[2] = worldZ[2] * 200 / worldY[2] + (SH / 2)
    worldX[3] = worldX[3] * 200 / worldY[3] + (SW / 2)
    worldY[3] = worldZ[3] * 200 / worldY[3] + (SH / 2)

    DrawWall(worldX[0], worldX[1], worldY[0], worldY[1], worldY[2], worldY[3])

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