import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont(None, 50)

# Clock
clock = pygame.time.Clock()

# Game variables
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_vel_x = random.choice([-5, 5])
ball_vel_y = random.choice([-5, 5])
paddle_width = 10
paddle_height = 100
paddle_vel = 5
player_score = 0
computer_score = 0

# Draw ball
def draw_ball():
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), ball_radius)

# Draw paddles
def draw_paddles():
    pygame.draw.rect(win, WHITE, (0, paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(win, WHITE, (WIDTH - paddle_width, computer_y, paddle_width, paddle_height))

# Move paddles
def move_paddles():
    global paddle_y, computer_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle_y > 0:
        paddle_y -= paddle_vel
    if keys[pygame.K_DOWN] and paddle_y < HEIGHT - paddle_height:
        paddle_y += paddle_vel
    if ball_y < computer_y + paddle_height // 2 and computer_y > 0:
        computer_y -= paddle_vel
    elif ball_y > computer_y + paddle_height // 2 and computer_y < HEIGHT - paddle_height:
        computer_y += paddle_vel

# Move ball
def move_ball():
    global ball_x, ball_y, ball_vel_x, ball_vel_y, player_score, computer_score
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Collision with walls
    if ball_y <= 0 or ball_y >= HEIGHT:
        ball_vel_y = -ball_vel_y

    # Collision with paddles
    if ball_x <= paddle_width and paddle_y <= ball_y <= paddle_y + paddle_height:
        ball_vel_x = -ball_vel_x
        player_score += 1
    elif ball_x >= WIDTH - paddle_width and computer_y <= ball_y <= computer_y + paddle_height:
        ball_vel_x = -ball_vel_x
        computer_score += 1

    # Reset ball if goes out of bounds
    if ball_x < 0 or ball_x > WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_vel_x = random.choice([-5, 5])
        ball_vel_y = random.choice([-5, 5])

# Display scores
def display_scores():
    player_score_text = font.render("Player: " + str(player_score), True, WHITE)
    computer_score_text = font.render("Computer: " + str(computer_score), True, WHITE)
    win.blit(player_score_text, (50, 50))
    win.blit(computer_score_text, (WIDTH - 250, 50))

# Main function
def main():
    global paddle_y, computer_y

    paddle_y = HEIGHT // 2 - paddle_height // 2
    computer_y = HEIGHT // 2 - paddle_height // 2

    # Game loop
    run = True
    while run:
        # Set FPS
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Move paddles
        move_paddles()

        # Move ball
        move_ball()

        # Draw everything
        win.fill(BLACK)
        draw_ball()
        draw_paddles()
        display_scores()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
