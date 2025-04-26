import pygame

pygame.init() 
screen = pygame.display.set_mode((500, 500))


pygame.display.set_caption('meu jogo')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        
        screen.fill('darkRed')
        pygame.draw.rect(screen, (0, 122, 233), (250, 250, 50, 50))
        pygame.draw.circle(screen, (0, 255, 125), (70, 100), 20)
        pygame.draw.ellipse(screen, 'darkBlue', (120, 350, 200, 350))
        pygame.draw.polygon(screen, 'black', [(120, 120), (150, 120), (140, 130)])
        pygame.display.flip()

