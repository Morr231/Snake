import pygame
import sys
from apple_class import Apple
from menu_class import Menu
from player_class import Player
from snake_class import Snake


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


def end_of_screen():
    if snake.snake_size[0][0] == 0 or snake.snake_size[0][0] == 600 or snake.snake_size[0][1] == 0 or snake.snake_size[0][1] == 600:
        menu.show_menu_lose()


def start_the_game():
    my_direction = LEFT
    change_dir = my_direction

    health = 3
    frame_rate = 15
    player = Player(menu.get_player_name())
    while True:
        clock.tick(frame_rate)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_dir = UP
                elif event.key == pygame.K_DOWN:
                    change_dir = DOWN
                elif event.key == pygame.K_RIGHT:
                    change_dir = RIGHT
                elif event.key == pygame.K_LEFT:
                    change_dir = LEFT

        if change_dir == UP and my_direction != DOWN:
            my_direction = UP
        if change_dir == DOWN and my_direction != UP:
            my_direction = DOWN
        if change_dir == LEFT and my_direction != RIGHT:
            my_direction = LEFT
        if change_dir == RIGHT and my_direction != LEFT:
            my_direction = RIGHT

        if my_direction == UP:
            snake.move_up()

        if my_direction == DOWN:
            snake.move_down()

        if my_direction == RIGHT:
            snake.move_right()

        if my_direction == LEFT:
            snake.move_left()

        frame_rate = apple.apple_collected(snake, player, frame_rate)
        end_of_screen()

        health = Snake.collision(snake, menu, player, health)

        if player.player_score == 10:
            menu.show_menu_win()
            break

        snake.move()

        screen.fill((0, 0, 0))

        draw_text(screen, f'{player.get_name()} | {player.player_score}', 18, 300, 20)
        draw_text(screen, f"Жизни: {health}", 18, 550, 20)

        screen.blit(apple.apple_skin, apple.pos)
        for pos in snake.snake_size:
            screen.blit(snake.snake_skin, pos)

        pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((600, 600))
font_name = pygame.font.match_font('arial')
pygame.display.set_caption('Змейка')

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = Snake([(200, 200), (210, 200), (220, 200)])

apple = Apple()

clock = pygame.time.Clock()
menu = Menu(start_the_game, screen)
menu.show_menu()

start_the_game()

menu.show_menu_lose()
