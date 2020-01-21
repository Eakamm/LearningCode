'''
@Author: your name
@Date: 2020-01-15 21:50:58
@LastEditTime : 2020-01-15 23:36:18
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonPersonal\小项目\外星人入侵\game_function.py
'''
import sys
import pygame


def check_event(ship):
    # 监听游戏的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(screen, ship, my_settings):
    screen.fill(my_settings.bg_color)
    ship.blitme()
    pygame.display.flip()


def check_keydown_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_move_right = True
    elif event.key == pygame.K_LEFT:
        ship.is_move_left = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.is_move_right = False
    elif event.key == pygame.K_LEFT:
        ship.is_move_left = False
