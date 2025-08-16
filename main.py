# Section 1: Importpygame. & Initialization
import pygame
import sys

# Initialize Pygame
pygame.init()

#Section 2: Constants & Game Settings
WIDTH = 800
HEIGHT = 600
WHITE = (255,0, 0)
BLACK = (255, 255, 255)
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
SPEED = 5

# Section 3: Setup Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ping pong")
clock = pygame.time.Clock()

# Section 4: Create Game Objects
# Paddles and Ball
left_paddle = pygame.Rect(20, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 30, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_vel = [SPEED, SPEED]

#Section 5: Initialize Scores & Fonts
# Scores
left_score, right_score = 0, 0
font = pygame.font.SysFont(None, 50)

# Section 6: Main Game Loop
# Game loop
while True:
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += SPEED

    # Ball movement
    ball.x += ball_vel[0]
    ball.y += ball_vel[1]

    # Wall collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel[1] = -ball_vel[1]

    # Paddle collision
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_vel[0] = -ball_vel[0]

    # Score update
    if ball.left <= 0:
        right_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_vel = [SPEED, SPEED]

    if ball.right >= WIDTH:
        left_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_vel = [-SPEED, SPEED]

    # Draw everything
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH//4, 20))
    screen.blit(right_text, (WIDTH*3//4, 20))

    pygame.display.flip()
    clock.tick(60)
