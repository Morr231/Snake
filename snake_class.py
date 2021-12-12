import pygame

from bd import add_user_on_table


class Snake:

    def __init__(self, init_position):
        self.snake_size = init_position
        self.snake_skin = pygame.Surface((10, 10))

        self.snake_skin.fill((255, 255, 255))

    def move_up(self):
        self.snake_size[0] = (
            self.snake_size[0][0], self.snake_size[0][1] - 10
        )

    def move_down(self):
        self.snake_size[0] = (
            self.snake_size[0][0], self.snake_size[0][1] + 10
        )

    def move_right(self):
        self.snake_size[0] = (
            self.snake_size[0][0] + 10, self.snake_size[0][1]
        )

    def move_left(self):
        self.snake_size[0] = (
            self.snake_size[0][0] - 10, self.snake_size[0][1]
        )

    def move(self):
        for i in range(len(self.snake_size) - 1, 0, -1):
            self.snake_size[i] = (
                self.snake_size[i - 1][0], self.snake_size[i - 1][1]
            )

    def reset_snake_size(self):
        self.snake_size = [(200, 200), (210, 200), (220, 200)]

    def collision(self, menu, player, health):
        for segment in self.snake_size[1:]:
            if self.snake_size[0] == segment:
                if health - 1 != 0:
                    health -= 1
                    break
                else:
                    print('=============== Конец игры !===============')
                    add_user_on_table(menu.get_player_name()['name_input'], str(player))
                    self.reset_snake_size()
                    menu.show_menu_lose()
                    break
        return health
