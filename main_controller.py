__author__ = 'Sudheer'
from matplotlib import pyplot as plt

from zernike import *

accuracy_percentage_list = []


def zernike_moments_for_all_angles():
    angle_list = [0, 30, 45, 60, 90, 180, 360]
    mean_list = []
    mean = controller_function(result_values_file.filename, 0)
    mean_list.append(mean)
    for x in angle_list[1:]:
        mean = controller_function(result_values_file.filename, x)
        mean_list.append(mean)

    for x in mean_list:
        accuracy_percentage = (x / mean_list[0]) * 100
        accuracy_percentage_list.append(accuracy_percentage)


def print_outline_for_all_angles():
    titles = ['Rotated 30 Degrees', 'Rotated 45 Degrees', 'Rotated 60 Degrees', 'Rotated 90 Degrees',
              'Rotated 180 Degrees', 'Rotated 360 Degrees']
    images = [result_values_file.image_1, result_values_file.image_2, result_values_file.image_3,
              result_values_file.image_4, result_values_file.image_5, result_values_file.image_6]
    for i in xrange(6):
        plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
        plt.xlabel(repr(accuracy_percentage_list[i + 1]) + "%")
    plt.show()
