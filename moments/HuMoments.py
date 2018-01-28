__author__ = 'Sudheer'
import cv2


def load_image(source):
    photo = cv2.imread(source)
    photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    return photo


def calculate_hu_moments(photo):
    hu_moments = cv2.HuMoments(cv2.moments(photo)).flatten()
    return hu_moments
