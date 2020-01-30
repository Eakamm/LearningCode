'''
@Author: your name
@Date: 2020-01-16 20:33:50
@LastEditTime : 2020-01-16 20:41:48
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \PythonPersonal\小项目\数据可视化\rw_visual.py
'''
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 创建散点图
    # plt.scatter(rw.x_values, rw.y_values, s=12)
    # plt.show()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,
                rw.y_values,
                c=point_numbers,
                cmap=plt.cm.Blues,
                s=12)

    # # Set the size of the plotting window.
    # plt.figure(dpi=128, figsize=(10, 6))

    # point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values,
    #             rw.y_values,
    #             c=point_numbers,
    #             cmap=plt.cm.Blues,
    #             edgecolor='none',
    #             s=1)

    # # Emphasize the first and last points.
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1],
    #             rw.y_values[-1],
    #             c='red',
    #             edgecolors='none',
    #             s=100)

    # # Remove the axes.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
