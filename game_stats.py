class GameStats():

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.score = 0
        self.level = 1
        self.game_active = False
        self.game_over = False
        self.game_win = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.game_over = False
        self.score = 0
        self.level = 1
        self.game_win = False