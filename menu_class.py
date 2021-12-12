import pygame
import pygame_menu

from bd import list_score


class Menu:
    def __init__(self, game_function, screen):
        self.menu_layout = pygame_menu.Menu(
            500, 550, 'Змейка', theme=pygame_menu.themes.THEME_DARK)
        self.top_layout = pygame_menu.Menu(
            500, 550, "Лучшие игроки", theme=pygame_menu.themes.THEME_DARK)

        users = list_score()
        text = 'Лучшие игроки:\n'
        if len(users) > 5:
            for i in range(5):
                text += f'\n Top {i + 1}: {users[i]["name"]} | Score: {users[i]["score"]}'
        else:
            for i in range(len(users)):
                text += f'\n Top {i + 1}: {users[i]["name"]} | Score: {users[i]["score"]}'

        self.top = self.top_layout.add_label(text, font_size=20)
        self.top_menu = self.top_layout.add_button(
            'В меню', self.menu_top)

        self.menu_input_name = self.menu_layout.add_text_input(
            'Игрок: ', default="User", textinput_id='name_input')
        self.top_play = self.top_layout.add_button(
            'Играть', game_function)
        self.help = self.menu_layout.add_label("Как играть?\n"
                                               "Управление простое!\n"
                                               "Змейку можно управлять стрелками\n"
                                               "Что бы выиграть наберите 10 очков и старайтесь не сьест свой хвост!"
                                               , max_char=-1, font_size=20)
        self.menu_start_btn = self.menu_layout.add_button(
            'Играть', game_function)
        self.menu_start_btn = self.menu_layout.add_button(
            'Выйти', pygame_menu.events.EXIT)
        self.game_screen = screen

    def menu_top(self):
        pygame.display.update()
        self.show_menu()

    def show_menu(self):
        self.menu_layout.mainloop(self.game_screen)

    def show_menu_lose(self):
        self.top_layout.set_title('Вы проиграли!')
        self.top_layout.mainloop(self.game_screen)

    def show_menu_win(self):
        self.top_layout.set_title('Вы выиграли!')
        self.top_layout.mainloop(self.game_screen)

    def get_player_name(self):
        return self.menu_layout.get_input_data()
