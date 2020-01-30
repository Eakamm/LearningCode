'''
@Author: your name
@Date: 2020-01-14 22:52:22
@LastEditTime : 2020-01-15 23:41:24
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /PythonPersonal/小项目/外星人入侵/alien_invasion.py
'''
import pygame
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
    # 加载屏幕的配置
    my_settings = Settings()
    # 初始化游戏，创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode(
        (my_settings.screen_width, my_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # 加载飞船
    ship = Ship(screen)
    # Start the main loop for the game.
    while True:
        # 监听游戏的事件
        gf.check_event(ship)
        ship.update(my_settings)
        # 更新屏幕
        gf.update_screen(screen, ship, my_settings)


run_game()
