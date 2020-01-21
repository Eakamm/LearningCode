'''
@Author: your name
@Date: 2020-01-15 21:06:02
@LastEditTime : 2020-01-15 23:47:08
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonPersonal\小项目\外星人入侵\ship.py
'''

import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        # 加载图像并获取其外接矩形
        self.image = pygame.image.load('小项目/外星人入侵/images/ship.bmp')
        # 飞船放到屏幕底部
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        # self.screen_rect.centerx为整数，想要把速度调为小数需要转化一下
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # 检测方向键是否被按下
        self.is_move_right = False
        self.is_move_left = False

    def blitme(self):
        # 在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def update(self, my_settings):
        if self.is_move_right and self.center <= int(
                self.screen_rect.right - my_settings.ship_speed_factor):
            self.center += my_settings.ship_speed_factor
        elif self.is_move_left and self.center >= int(
                my_settings.ship_speed_factor):
            self.center -= my_settings.ship_speed_factor
        self.rect.centerx = self.center
