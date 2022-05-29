# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 09:05:42 2022

@author: henri
"""

from os import listdir
from os.path import isfile, join
import random
import time
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 

from jdlv_data import * 
from jdlv_model import *
from jdlv_outils import *
import plan_planisphere_individuel
from plan_planisphere_individuel import *
import plan_planisphere_global
from plan_planisphere_global import *
import plan_france_individuel
from plan_france_individuel import *
import plan_france_global
from plan_france_global import *
import plan_moto_position1
from plan_moto_position1 import *
import plan_moto_position2
from plan_moto_position2 import *
import plan_moto_position3
from plan_moto_position3 import *
import plan_arc_de_triomphe
from plan_arc_de_triomphe import *




def make_test (grid, i, j, color):
    grid = clean_grid (grid)
    cases = grid.cases
    for n in range (10) : 
        color = "black"
        cases [i + 0] [j + n] ['s'] = life_status
        cases [i + 0] [j + n] ['c'] = color 
        color = "black" 
        cases [i + 1] [j + n] ['s'] = life_status
        cases [i + 1] [j + n] ['c'] = color
        next_grid = n+1 
    return grid 


def make_conway (grid, i, j, color):
    try:
        #grid = clean_grid (grid)
        cases = grid.cases
        cases [i] [j] ['s'] = life_status
        cases [i] [j] ['c'] = color
        cases [i + 1] [j + 1] ['s'] = life_status
        cases [i + 1] [j + 1] ['c'] = color
        cases [i + 1] [j + 1] ['s'] = life_status
        cases [i + 1] [j + 1] ['c'] = color
        cases [i + 2] [j + 1] ['s'] = life_status
        cases [i + 2] [j + 1] ['c'] = color
        cases [i + 3] [j + 1] ['s'] = life_status
        cases [i + 3] [j + 1] ['c'] = color
        cases [i + 3] [j + 2] ['s'] = life_status
        cases [i + 3] [j + 2] ['c'] = color
    except:
        pass
    return grid

def apply_game_of_life_rules (grid):
    previous_grid = grid
    previous_cases = previous_grid.cases
    cases = grid.cases # cases is a list of lists of dictionnaries
    next_grid = Grid (len (cases))
    next_cases = next_grid.cases
    for i in range (1, len (cases) - 1):
        for j in range (1, len (cases) - 1):
            previous_status = cases [i][j]['s']
            voisins = get_voisins (cases, i, j)
            nbre_alive_voisins = count_alive_voisins (voisins)
            if nbre_alive_voisins == 3:
                next_cases [i] [j] = revive_case (next_cases [i] [j])
            elif nbre_alive_voisins <= 1 or nbre_alive_voisins >= 4:
                next_cases [i] [j] = kill_case (next_cases [i] [j])
            else:
                next_cases [i] [j] = cases [i] [j]
    return next_grid




def scene_1 (grid, compteur):
    next_grid = grid 
    if compteur == 0 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
           clean_grid (grid)
        time.sleep (0)
    elif compteur <= 1 :
        print ("COMPTEUR % 11  is  56")
        next_grid = \
           make_planisphere_plan1 (grid, 4, 4, "grey")
        time.sleep (3.08)
    elif compteur <= 2 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan2 (grid, 4, 4, "grey")
        time.sleep (0.8)
    elif compteur <= 3:
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan3 (grid, 4, 4, "grey")
        time.sleep (0.4)
    elif compteur <= 4 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan4 (grid, 4, 4, "grey")
        time.sleep (0.4)
    elif compteur <= 5 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan5 (grid, 4, 4, "grey")
        time.sleep (0.5)
    elif compteur <= 6:
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan6 (grid, 4, 4, "grey")
        time.sleep (0.7)
    elif compteur <= 7 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan7 (grid, 4, 4, "grey")
        time.sleep (1.25)
    elif compteur <= 8 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan8 (grid, 4, 4, "grey")
        time.sleep (0.4)
    elif compteur <= 9:
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan9 (grid, 4, 4, "grey")
        time.sleep (0.3)
    elif compteur <= 10 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan10 (grid, 4, 4, "grey")
        time.sleep (0.3)
    elif compteur <= 11 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan11 (grid, 4, 4, "grey")
        time.sleep (0.3)
    elif compteur <= 12:
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan12 (grid, 4, 4, "grey")
        time.sleep (0.3)
    elif compteur <= 13 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan13 (grid, 4, 4, "grey")
        time.sleep (0.3)
    elif compteur <= 14 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_plan14 (grid, 4, 4, "grey")
        time.sleep (0.5)
    else :
        print ("COMPTEUR % 11 is NOT 0")
        time.sleep (0.4)
        next_grid = scene_2 (grid, compteur)
    return next_grid


def scene_2 (grid, compteur) : 
    if compteur <= 15 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_global (grid, 4, 4, "grey")
        time.sleep (0.2)
    elif compteur <= 16 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
        time.sleep (0.2)
    elif compteur <= 17 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_global (grid, 4, 4, "grey")
        time.sleep (0.2)
    elif compteur <= 18 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
        time.sleep (0.2)
    elif compteur <= 19 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_global (grid, 4, 4, "grey")
        time.sleep (0.2)
    elif compteur <= 20 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
        time.sleep (0.2)
    elif compteur <= 21 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_global (grid, 4, 4, "grey")
        time.sleep (0.2)
    elif compteur <= 22 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
        time.sleep (0.2)
    elif compteur <= 23 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_global (grid, 4, 4, "grey")
        time.sleep (0.2)
    elif compteur <= 24 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
        time.sleep (0.2)
    elif compteur <= 25 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_planisphere_global (grid, 4, 4, "grey")
    elif compteur <= 26 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 27 :
        print ("COMPTEUR % 11  is not 0")
        next_grid = \
            clean_grid(grid)
    elif compteur <= 27 :
        print ("COMPTEUR % 11  is not 0")
        next_grid = \
            clean_grid(grid)
    else : 
        print ("COMPTEUR % 11 is NOT 0")
        next_grid = scene_3 (grid, compteur) 
    return next_grid


def scene_3 (grid, compteur) :
    if compteur <= 29 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_plan1 (grid, 4, 4, "grey")
    elif compteur <= 30 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_plan2 (grid, 4, 4, "grey")
    elif compteur <= 31 :
         print ("COMPTEUR % 11  is  0")
         next_grid = \
             make_france_plan3 (grid, 4, 4, "grey")
    elif compteur <= 32 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_plan4 (grid, 4, 4, "grey")
    elif compteur <= 33 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_plan5 (grid, 4, 4, "grey")
    elif compteur <= 34 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_plan6 (grid, 4, 4, "grey")
    elif compteur <= 35 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_plan7 (grid, 4, 4, "grey")
    else : 
        print ("COMPTEUR % 11 is NOT 0")
        next_grid = scene_4 (grid, compteur)
    return next_grid


def scene_4 (grid, compteur) : 
    if compteur <= 36 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 37 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 38 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 39 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 40 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 41 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <=42 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 43 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 44 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 45 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 46 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 47 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 48 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_france_global (grid, 4, 4, "grey")
    elif compteur <= 49 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    else : 
        print ("COMPTEUR % 11 is NOT 0")
        next_grid = scene_5 (grid, compteur)
    return next_grid

def scene_5 (grid, compteur) : 
    if compteur <= 50 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position1 (grid, 4, 4, "grey")
    elif compteur <= 51 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position2 (grid, 4, 4, "grey")
    elif compteur <= 52 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position3 (grid, 4, 4, "grey")
    elif compteur <= 53 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position1 (grid, 4, 4, "grey")
    elif compteur <= 54 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position2 (grid, 4, 4, "grey")
    elif compteur <= 55 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position3 (grid, 4, 4, "grey")
    elif compteur <= 56 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position1 (grid, 4, 4, "grey")
    elif compteur <= 57 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position2 (grid, 4, 4, "grey")
    elif compteur <= 58 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_moto_position3 (grid, 4, 4, "grey")
    elif compteur <= 59 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            clean_grid (grid)
    elif compteur <= 60 :
        print ("COMPTEUR % 11  is  0")
        next_grid = \
            make_arc_de_triomphe (grid, 4, 4, "grey")
        time.sleep (0)
    else:
        print ("COMPTEUR % 11 is NOT 0")
        time.sleep (0.5)
        next_grid = apply_game_of_life_rules (grid)
    return next_grid
