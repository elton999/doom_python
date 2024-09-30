import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

SCREEN_HEIGHT = 200
SCREEN_WIDTH = 200

pixelSize = 4
cameraX =  70
cameraY =  -110 
cameraZ = 20
cameraA = 0
cameraL = 0

pixels = []

def SetUp():
    for x in range(SCREEN_WIDTH):
        pixels.append([])
        for y in range(SCREEN_HEIGHT):
            pixels[x].append("black")

def Clear():
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
                pixels[x][y] = "black"

def Render():
    if cameraX > 0 and cameraX < SCREEN_WIDTH and cameraY> 0 and cameraY < SCREEN_HEIGHT:
        pixels[int(cameraX)][int(cameraY)] = "red"
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            pygame.draw.rect(screen, pixels[x][y], pygame.Rect(x * pixelSize, y * pixelSize, pixelSize, pixelSize))

def DrawWall(x1 : int , x2 : int, b1 : int,  b2 : int, t1 : int, t2 : int):
    dyb = b2 - b1
    dyt = t2 - t1
    dx = x2 - x1

    if dx == 0: dx = 1
    xs = x1

    if x1 < 1:  x1 = 1
    if x2 < 1: x2 = 1
    if x1 > SCREEN_WIDTH - 1: x1 = SCREEN_WIDTH - 1
    if x2 > SCREEN_WIDTH - 1: x2 = SCREEN_WIDTH - 1 

    for x in range(int(x2 - x1)):
        xx = int(x + x1)
        y1 = int(dyb * (xx - xs) / dx + b1)
        y2 = int(dyt * (xx - xs) / dx + t1)

        if y1 < 1: y1 = 1
        if y2 < 1: x2 = 1
        if y1 > SCREEN_HEIGHT - 1: y1 = SCREEN_HEIGHT - 1
        if y2 > SCREEN_HEIGHT - 1: y2 = SCREEN_HEIGHT - 1 

        for y in range(int(y2 - y1)):
            yy = y + y1
            if xx > 0 and xx< SCREEN_WIDTH and yy > 0 and yy < SCREEN_HEIGHT:
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
    worldY[2] = worldY[0]
    worldY[3] = worldY[1]

    worldZ[0] = 0 - cameraZ + ((cameraL * worldY[0]) / 32)
    worldZ[1] = 0 - cameraZ + ((cameraL * worldY[1]) / 32)
    worldZ[2] = worldZ[0] + 40
    worldZ[3] = worldZ[1] + 40


    worldX[0] = worldX[0] * 200 / worldY[0] + (SCREEN_WIDTH / 2)
    worldY[0] = worldZ[0] * 200 / worldY[0] + (SCREEN_HEIGHT / 2)
    worldX[1] = worldX[1] * 200 / worldY[1] + (SCREEN_WIDTH / 2)
    worldY[1] = worldZ[1] * 200 / worldY[1] + (SCREEN_HEIGHT / 2)

    worldX[2] = worldX[2] * 200 / worldY[2] + (SCREEN_WIDTH / 2)
    worldY[2] = worldZ[2] * 200 / worldY[2] + (SCREEN_HEIGHT / 2)
    worldX[3] = worldX[3] * 200 / worldY[3] + (SCREEN_WIDTH / 2)
    worldY[3] = worldZ[3] * 200 / worldY[3] + (SCREEN_HEIGHT / 2)

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