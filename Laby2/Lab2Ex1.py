import pygame
import math
 
pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")
 
# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

PressedKey = None
 
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            PressedKey = event.key
 
    points = []
    duration = 0
    for x in range(10):
        points.append((math.sin(duration) * 150 + 150, math.cos(duration) * 150 + 150))
        duration += math.pi * 2 / 10

    skew = 0
    if (PressedKey == pygame.K_4 or PressedKey == pygame.K_6 or PressedKey == pygame.K_9):
        skew = 0.4
    for i in range(10):
        points[i] = (points[i][0] + ((points[i][1] - 150) * skew), points[i][1])
 
    win.fill(ZOLTY)
    sur = pygame.Surface((300, 300))
    sur.fill(ZOLTY)
    pygame.draw.polygon(sur, ZIELONY, points)

    YOffset = 0
    XOffset = 0
    if (PressedKey == pygame.K_1):
        sur = pygame.transform.scale(sur, (150, 150))
    if (PressedKey == pygame.K_2): 
        sur = pygame.transform.rotate(sur, 45)
        sur = pygame.transform.scale(sur, (500, 500))
    if (PressedKey == pygame.K_3):
        sur = pygame.transform.flip(sur, 0, 1)
        sur = pygame.transform.scale(sur, (200, 400))
    if (PressedKey == pygame.K_5):
        sur = pygame.transform.scale(sur, (500, 300))
        YOffset = 150
    if (PressedKey == pygame.K_6):
        sur = pygame.transform.rotate(sur, 90)
    if (PressedKey == pygame.K_7):
        sur = pygame.transform.flip(sur, 1, 1)
        sur = pygame.transform.scale(sur, (200, 400))
    if (PressedKey == pygame.K_8):
        sur = pygame.transform.rotate(sur, 25)
        sur = pygame.transform.scale(sur, (400, 250))
        YOffset = -100
        XOffset = -100
    if (PressedKey == pygame.K_9):
        sur = pygame.transform.scale(sur, (400, 400))
        sur = pygame.transform.rotate(sur, 180)
        XOffset = 100
    
    win.blit(sur, (300-(sur.get_width()/2)+XOffset, 300-(sur.get_height()/2)-YOffset))
    pygame.display.update()
   