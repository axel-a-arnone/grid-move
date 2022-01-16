# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:18:28 2022

@author: Axel
"""


class Track:
    def __init__(self, width, height):
        self.height = self._is_valid_height(height)
        self.width = self._is_valid_width(width)

    def _is_valid_height(self, height):
        if not isinstance(height, int):
            raise TypeError("selected height is not an int")
        else:
            return height

    def _is_valid_width(self, width):
        if not isinstance(width, int):
            raise TypeError("selected width is not an int")
        else:
            return width


class Car:
    def __init__(self, track, x_pos=0, y_pos=0, x_speed=0, y_speed=0):
        self.track = track
        self.position = [x_pos, y_pos]
        self.speed = [x_speed, y_speed]

    def change_speed(self, x_change, y_change):
        self.speed[0] = self.speed[0]+x_change
        self.speed[1] = self.speed[1]+y_change

    def move_once(self):
        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]
