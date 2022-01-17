# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 03:46:43 2022

@author: Axel
"""

import track_environment

# TRACK SETTINGS
TRACK_WIDTH = 10
TRACK_HEIGHT = 10
FINISH_LINE_P1 = [0, 9]
FINISH_LINE_P2 = [9, 9]


def valid_acceleration():
    """
    Prompts user action and checks for errors

    Raises
    ------
    TypeError
        If input isn't a string
    ValueError
        If input isn't a legal action.

    Returns
    -------
    user_action : str
        String containing legal user action.

    """
    legal_actions = ['FL', 'FN', 'FR',
                     'NL', 'NN', 'NR',
                     'BL', 'BN', 'BR']
    user_action = input("""Insert acceleration as 'V''H' pair
                    V: F = +1, N = 0, B = -1
                    H: R = +1, N = 0, L = -1\n""")
    if not isinstance(user_action, str):
        raise TypeError("Please insert two characters")
        user_action = 'NN'
    if len(user_action) != 2:
        raise ValueError("Please insert only two characters")
        user_action = 'NN'
    if user_action not in legal_actions:
        raise ValueError("Inserted action isn't legal")
        user_action = 'NN'
    return user_action


def user_action_to_speed_change(user_action):
    """
    Transforms user input in x and y changes

    Parameters
    ----------
    user_action : str
        Action in 'V''H' format.

    Returns
    -------
    x_change : int
        Speed change along x axis.
    y_change : int
        Speed change along y axis.

    """
    acceleration_dict = {'FL': [1, -1], 'FN': [1, 0], 'FR': [1, 1],
                         'NL': [0, -1], 'NN': [0, 0], 'NR': [0, 1],
                         'BL': [-1, -1], 'BN': [-1, 0], 'BR': [-1, 1]}
    vert_horiz_variations = acceleration_dict[user_action]
    x_change = vert_horiz_variations[1]
    y_change = vert_horiz_variations[0]
    return x_change, y_change


def accelerate(car):
    """
    Prompts user input, verifies it and changes car speed

    Parameters
    ----------
    car : obj
        valid car.

    Returns
    -------
    None.

    """
    user_action = valid_acceleration()
    x_change, y_change = user_action_to_speed_change(user_action)
    car.change_speed(x_change, y_change)


def run_game_step(car):
    """
    Accelerates car, moves it and prints new situation

    Parameters
    ----------
    car : obj
        Valid car.

    Returns
    -------
    None.

    """
    accelerate(car)
    car.move_once()
    car.print_current_status()


def main():
    game_track = track_environment.Track(TRACK_WIDTH, TRACK_HEIGHT)
    game_track.set_finishline(FINISH_LINE_P1, FINISH_LINE_P2)
    game_car = track_environment.Car(game_track)
    game_car.print_current_status()
    for _ in range(10):
        run_game_step(game_car)


if __name__ == '__main__':
    main()
