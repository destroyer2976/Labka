import pygame
import random
import time

# Initialize pygame
pygame.init()

# Game window dimensions
window_x = 720
window_y = 480
snake_speed = 15

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Game window setup
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Snake initial position
snake_position = [100, 50]

# Initial snake body segments
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Initial direction the snake is moving towards
direction = 'RIGHT'
change_to = direction

# Initial score
score = 0

# Food class
class Food:
    def __init__(self):
        self.position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
        self.spawn_time = pygame.time.get_ticks()
        self.color = red if random.randint(0, 1) == 0 else white  # Red or white food
        self.score = 10 if self.color == white else 20  # 10 or 20 points
        self.duration = 5000  # Food disappears after 5 seconds

# Initial food
food = Food()

# Function to show the score at the top
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

# Function to end the game
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction changes
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food.position[0] and snake_position[1] == food.position[1]:
        score += food.score
        food = Food()
    else:
        snake_body.pop()

    # Check food duration
    if pygame.time.get_ticks() - food.spawn_time > food.duration:
        food = Food()

    # Drawing
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, food.color, pygame.Rect(food.position[0], food.position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_position == block:
            game_over()

    show_score(white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snake_speed)
