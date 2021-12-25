import pygame
import random


class Apple:
    def __init__(self):
        self.apple_skin = pygame.Surface((10, 10))
        self.apple_skin.fill((255, 0, 0))

        self.pos = (random.randint(0, 400) // 10 * 10, random.randint(0, 400) // 10 * 10)

    def new_pos(self):
        self.pos = (random.randint(0, 400) // 10 * 10, random.randint(0, 400) // 10 * 10)

    def apple_collected(self, snake, player, frame_rate):
        if self.pos == snake.snake_size[0]:
            self.new_pos()
            player.increase_score()
            frame_rate += 1
            snake.snake_size.append((0, 0))
        return frame_rate