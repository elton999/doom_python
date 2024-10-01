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
                pixels[x][y] = "blue"

def Render():
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            pygame.draw.rect(screen, pixels[x][y], pygame.Rect(x * pixelSize, y * pixelSize, pixelSize, pixelSize))

def DrawLine(p1x : int, p1y : int, p2x : int, p2y : int):
    directionX = p2x - p1x
    directionY = p2y - p1y	

    for y in range(p1y, p2y + 1):
        yy = y - p1y
        x = int(yy / directionY * directionX) + p1x
        
        if x > 0 and x < SCREEN_WIDTH and y > 0 and y < SCREEN_HEIGHT:
            pixels[x][y] = "yellow"
    
    if p1x > 0 and p1x < SCREEN_WIDTH and p1y > 0 and p1y < SCREEN_HEIGHT:
        pixels[p1x][p1y] = "red"
    if p2x > 0 and p2x < SCREEN_WIDTH and p2y > 0 and p2y < SCREEN_HEIGHT:
        pixels[p2x][p2y] = "red"

SetUp()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]: pygame.quit()

    screen.fill("white")
    Clear()
    DrawLine(100, 100, 159, 159)
    Render()

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()