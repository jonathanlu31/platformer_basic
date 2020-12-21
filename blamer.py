import pygame
pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption('First Game')

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 15
isJump = False
jumpConst = 6
left = False
right = False
walkCount = 0

#draw function
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount >= 26:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    pygame.display.update()

#main loop
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > vel:
            x -= vel
        else:
            x -= x
        left = True
        right = False

    elif keys[pygame.K_RIGHT]:
        if x < 500 - vel - width:
            x += vel
        else:
            x += 500 - width - x
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpConst >= -6:
            neg = 1
            if jumpConst < 0:
                neg = -1
            y -= (jumpConst ** 2) // 1.5 * neg
            jumpConst -= 1
        else:
            isJump = False
            jumpConst = 6

    redrawGameWindow()

pygame.quit()
