import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('First Game')

x = 50
y = 50
width = 40
height = 60
vel = 15
isJump = False
jumpConst = 6

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x > vel:
            x -= vel
        else:
            x -= x

    if keys[pygame.K_RIGHT]:
        if x < 500 - vel - width:
            x += vel
        else:
            x += 500 - width - x

    if not isJump:
        if keys[pygame.K_UP]:
            if y < vel:
                y -= y
            else:
                y -= vel

        if keys[pygame.K_DOWN]:
            if y < 500 - vel - height:
                y += vel
            else:
                y += 500 - height - y

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

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
