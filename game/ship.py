import pygame

class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        ##相对路径依赖于当前运行目录，如果这个相对运行目录发生变化，相对路径就会失效self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.image.load('/Users/dabaobaodemac/Desktop/LearnPython/game/images/ship.bmp')
        self.rect = self.image.get_rect()

        #每艘新飞船都放在屏幕最底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 在飞船的属性x中存在一个浮点数
        self.x = float(self.rect.x)

        # 移动标志（飞船一开始不移动）
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的属性x的值，而不是其外接矩形的属性x的值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            if self.moving_right:
                self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            if self.moving_left:
                self.x -= self.settings.ship_speed

        # 根据self.x 更新rect对象
        self.rect.x = self.x

    def blitme(self):
        """在指定位置描绘飞船"""
        self.screen.blit(self.image, self.rect)