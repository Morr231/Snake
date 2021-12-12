class Player:
    def __init__(self, name):
        self.player_score = 0
        self.player_name = name

    def increase_score(self):
        self.player_score += 1

    def get_name(self):
        return self.player_name['name_input']

    def __str__(self):
        return f'{self.player_score}'
