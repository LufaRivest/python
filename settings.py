class Settings():
    """存储游戏所有设置的类"""

    def __init__(self):
        """游戏的初始设置"""
        self.init_image_path = "images/init_image.jpg"
        self.game_over_image_path = "images/game_over.jpg"
        self.screen_width=480
        self.screen_height=600
        self.bg_color=(255,255,255)

        self.ship_limit = 3
        self.ship_invincible_time = 200
        self.ship_speed_factor=2

        self.bullet_speed_factor = 1.5
        self.bullet_width = 2
        self.bullet_height = 6
        self.bullet_color =(255,20,20)
        self.add_bullet_interval = 30

        self.boss_heart = 50

        self.alien_speed=((0.5,0.55),(0.65,0.7),
                          (0.55,0.6),(0.6,0.65),
                          (0.5,0.55),(0.55,0.6),
                          (0.6, 0.65), (0.8, 0.9),
                          (0.85, 0.95),(1.5,1.5),
                          )
        self.alien_lines_by_level=(2,2,3,3,4,4,4,3,3,1)