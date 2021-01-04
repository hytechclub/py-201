import pygame
import random

WIDTH = 800
HEIGHT = 600
BACKGROUND = (0, 0, 0)

class Ball:
    def __init__(self):
        self.image = pygame.image.load("small_tennis.png")
        self.speed = [random.randrange(-4,4), 3]
        self.rect = self.image.get_rect()
        self.alive = True

    def update(self):
        if self.rect.top < 0:
            self.speed[1] = -self.speed[1]
            self.speed[0] = random.randrange(-2, 2)
        elif self.rect.left < 0 or self.rect.right > WIDTH:
            self.speed[0] = -self.speed[0]
        elif self.rect.bottom > HEIGHT:
            self.alive = False
        self.move()

    def move(self):
        self.rect = self.rect.move(self.speed)


def main():
    clock = pygame.time.Clock()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    ball1 = Ball()
    ball2 = Ball()
    ball3 = Ball()

    balls = [ball1, ball2, ball3]
    num_successful_throws = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    if ball.rect.collidepoint(pygame.mouse.get_pos()):
                        ball.speed[0] = random.randrange(-4, 4)
                        ball.speed[1] = -2
                        num_successful_throws += 1
                        break

        if num_successful_throws > 3:
            ball = Ball()
            balls.append(ball)
            num_successful_throws = 0
    
        screen.fill(BACKGROUND)
        for i, ball in enumerate(balls):
            if ball.alive:
                screen.blit(ball.image, ball.rect)
                ball.update()
                if not ball.alive:
                    del balls[i]
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()