'''
@Author: your name
@Date: 2020-01-14 23:16:46
@LastEditTime : 2020-01-15 23:41:52
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /PythonPersonal/小项目/外星人入侵/settings.py
'''


class Settings():
    """外星入侵的设置类"""
    def __init__(self):
        """初始化游戏设置"""
        # 窗口大小
        self.screen_height = 700
        self.screen_width = 1200
        # 背景色
        self.bg_color = (230, 230, 230)
        # 飞船速度
        self.ship_speed_factor = 5.5
