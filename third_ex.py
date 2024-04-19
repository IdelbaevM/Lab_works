import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("RedBall")
pygame.display.set_icon(pygame.image.load('images/ball.png'))

ball_x = 250
ball_y = 250
ball_radius = 25

clock = pygame.time.Clock()  # Clock for controlling the frame rate

run = True
while run:
    screen.fill('White')

    pygame.draw.circle(screen, 'red', (ball_x, ball_y), ball_radius)

    pygame.display.update()
    clock.tick(60)  # Limit to 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball_x -= 20
            elif event.key == pygame.K_RIGHT:
                ball_x += 20
            elif event.key == pygame.K_UP:
                ball_y -= 20
            elif event.key == pygame.K_DOWN:
                ball_y += 20

pygame.quit()
