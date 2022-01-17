# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:18:28 2022

@author: Axel
"""
import matplotlib.pyplot as plt


class Track:
    def __init__(self, width, height):
        """
        A class to represent a Track

        Parameters
        ----------
        width : INT
            Number of grid-cells in x direction.
        height : INT
            Number of grid-cells in y direction.

        Returns
        -------
        None.

        """
        self.height = self._is_valid_height(height)
        self.width = self._is_valid_width(width)
        self.track_grid = self._track_base()

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

    def _is_legal_position(self, position):
        if not isinstance(position, list):
            raise TypeError("position should be a list")
        if len(position) != 2:
            raise ValueError("position should have two values")
        try:
            self.track_grid[tuple(position)]
            return position
        except KeyError:
            raise ValueError("position is out of bounds")

    def _track_base(self):
        """
        Fills the cells with 'r', for cells of type road

        Returns
        -------
        None.

        """
        track_grid = {}
        for x_idx in range(self.width):
            for y_idx in range(self.height):
                track_grid[x_idx, y_idx] = 'r'
        return track_grid

    def print_track(self):
        """
        Shows current track as a grid of dots.
        Black dots represent cells of type road
        Magenta dots represent cells of type finish
        Returns
        -------
        None.

        """
        # Obtaining x-y pairs from track_grid dict
        x_road_vector = []
        y_road_vector = []
        x_finish_vector = []
        y_finish_vector = []
        for position in self.track_grid.keys():
            cell_type = self.track_grid[position]
            x_coord = position[0]
            y_coord = position[1]
            if cell_type == 'r':
                x_road_vector.append(x_coord)
                y_road_vector.append(y_coord)
            elif cell_type == 'f':
                x_finish_vector.append(x_coord)
                y_finish_vector.append(y_coord)
        # Plotting track as scatter plot
        plt.plot(x_road_vector, y_road_vector, 'ko')
        plt.plot(x_finish_vector, y_finish_vector, 'mo')

    def set_finishline(self, point_1, point_2):
        """
        Sets finishline of track

        Parameters
        ----------
        point_1 : LIST
            Position of one of .
        point_2 : LIST
            DESCRIPTION.

        Raises
        ------
        ValueError
            DESCRIPTION.

        Returns
        -------
        None.

        """
        point_1 = self._is_legal_position(point_1)
        point_2 = self._is_legal_position(point_2)
        x_min = min(point_1[0], point_2[0])
        x_max = max(point_1[0], point_2[0])
        y_min = min(point_1[1], point_2[1])
        y_max = max(point_1[1], point_2[1])
        same_x_bool = x_min == x_max
        same_y_bool = y_min == y_max
        if same_x_bool and not same_y_bool:
            x_coord = x_min
            for y_idx in range(y_min, y_max+1):
                self.track_grid[x_coord, y_idx] = 'f'
        elif not same_x_bool and same_y_bool:
            y_coord = y_min
            for x_idx in range(x_min, x_max+1):
                self.track_grid[x_idx, y_coord] = 'f'
        elif same_x_bool and same_y_bool:
            self.track_grid[x_min, y_min] = 'f'
        elif not same_x_bool and not same_y_bool:
            raise ValueError("Selected points are not aligned")


class Car:
    def __init__(self, track, x_pos=0, y_pos=0, x_speed=0, y_speed=0):
        self.track = track
        self.position = [x_pos, y_pos]
        self.speed = [x_speed, y_speed]

    def change_speed(self, x_change, y_change):
        self.speed[0] = self.speed[0]+x_change
        self.speed[1] = self.speed[1]+y_change

    def move_once(self):
        new_x = self.position[0] + self.speed[0]
        new_y = self.position[1] + self.speed[1]
        new_position = self._is_valid_position(new_x, new_y)
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]

    def _is_valid_position(self, x_pos, y_pos):
        """
        Checks if the position is legal

        Parameters
        ----------
        x_pos : INT
            X coordinate of position.
        y_pos : INT
            Y coordinate of position.

        Returns
        -------
        If position is legal, returns [x_pos, y_pos].

        """
        track_grid = self.track.track_grid
        current_position = self.position
        try:
            cell_type = track_grid[x_pos, y_pos]
        except KeyError:
            print("Position out of bounds, can't move")
            return current_position
        if cell_type == 'r':
            return[x_pos, y_pos]
        if cell_type == 'f':
            print("You reached the finish line!")
            return[x_pos, y_pos]

    def print_current_status(self):
        """
        Prints track, car and current speed

        Returns
        -------
        None.

        """
        self.track.print_track()
        plt.plot(self.position[0], self.position[1], 'bo')
        plt.arrow(self.position[0], self.position[1],
                  self.speed[0], self.speed[1],
                  width=0.05,
                  length_includes_head=True,
                  color='g')
        plt.show()
