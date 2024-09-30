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
cameraY = -110 
cameraZ =  20
cameraAngle = 0
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

    cs = math.cos(math.radians(cameraAngle))
    sn = math.sin(math.radians(cameraAngle))

    point1X = 40
    point1Y = 10

    point2X = 40
    point2Y = 290
    
    dist1X = point1X - cameraX
    dist1Y = point1Y - cameraY

    dist2X = point2X - cameraX
    dist2Y = point2Y - cameraY

    worldX[0] = dist1X * cs - dist1Y * sn
    worldX[1] = dist2X * cs - dist2Y * sn
    worldX[2] = worldX[0]
    worldX[3] = worldX[1]
    
    worldY[0] = dist1Y * cs + dist1X * sn
    worldY[1] = dist2Y * cs + dist2X * sn
    worldY[2] = worldY[0]
    worldY[3] = worldY[1]

    worldZ[0] = 0 - cameraZ #+ ((cameraL * worldY[0]) / 32)
    worldZ[1] = 0 - cameraZ #+ ((cameraL * worldY[1]) / 32)
    worldZ[2] = worldZ[0] + 40
    worldZ[3] = worldZ[1] + 40

    widthRation =  SCREEN_WIDTH / 2
    centerScreenW = SCREEN_WIDTH / 2
    centerScreenH =  SCREEN_HEIGHT / 2

    worldX[0] = worldX[0] * widthRation / worldY[0] + centerScreenW
    worldY[0] = worldZ[0] * widthRation / worldY[0] + centerScreenH
    worldX[1] = worldX[1] * widthRation / worldY[1] + centerScreenW
    worldY[1] = worldZ[1] * widthRation / worldY[1] + centerScreenH

    worldX[2] = worldX[2] * widthRation / worldY[2] + centerScreenW
    worldY[2] = worldZ[2] * widthRation / worldY[2] + centerScreenH
    worldX[3] = worldX[3] * widthRation / worldY[3] + centerScreenW
    worldY[3] = worldZ[3] * widthRation / worldY[3] + centerScreenH

    DrawWall(worldX[0], worldX[1], worldY[0], worldY[1], worldY[2], worldY[3])

SetUp()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not keys[pygame.K_LSHIFT]:
        cameraAngle -=  4
        if(cameraAngle < 0):
            cameraAngle += 360
    if keys[pygame.K_d] and not keys[pygame.K_LSHIFT]:
        cameraAngle +=   4
        if(cameraAngle > 359):
            cameraAngle -= 360

    dx = math.radians(math.sin(cameraAngle)) * 10
    dy = math.radians(math.cos(cameraAngle)) * 10

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