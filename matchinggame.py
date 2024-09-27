import pygame
pygame.init()

screen = pygame.display.set_mode((600,500))
screen.fill((0,0,0))
pygame.display.update()

t = pygame.image.load(r"Game dev 2\matching game\Image20240920170922.png")
c = pygame.image.load(r"Game dev 2\matching game\Image20240920170941.jpg")
s = pygame.image.load(r"Game dev 2\matching game\Image20240920170954.png")
l = pygame.image.load(r"Game dev 2\matching game\Image20240920171003.png")

font1 = pygame.font.SysFont("Arial",40)

screen.blit(t,(20,20))
screen.blit(c,(20,120))
screen.blit(s,(20,220))
screen.blit(l,(20,320))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    tem = font1.render("Temple Run",True,(234,234,134))
    can = font1.render("Candy Crush",True,(234,234,134))
    sub = font1.render("Subway Surfers",True,(234,234,134))
    lud = font1.render("Ludo",True,(234,234,134))
    screen.blit(can,(300,20))
    screen.blit(lud,(300,120))
    screen.blit(tem,(300,220))
    screen.blit(sub,(300,320))
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_position = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONUP:
        mouse_position1 = pygame.mouse.get_pos()
        pygame.draw.line(screen,"red",mouse_position,mouse_position1)
    pygame.display.update()

    