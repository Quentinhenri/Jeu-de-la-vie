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

def make_moto_position1 (grid, i, j, color) :
    try:
        grid = clean_grid (grid)
        cases = grid.cases
        color = 'grey'
        cases [i + 50] [j + 26] ['s'] = life_status
        cases [i + 50] [j + 26] ['c'] = color
        cases [i + 50] [j + 27] ['s'] = life_status
        cases [i + 50] [j + 27] ['c'] = color
        cases [i + 50] [j + 28] ['s'] = life_status
        cases [i + 50] [j + 28] ['c'] = color
        cases [i + 50] [j + 29] ['s'] = life_status
        cases [i + 50] [j + 29] ['c'] = color
        cases [i + 50] [j + 30] ['s'] = life_status
        cases [i + 50] [j + 30] ['c'] = color
        cases [i + 50] [j + 31] ['s'] = life_status
        cases [i + 50] [j + 31] ['c'] = color
        cases [i + 50] [j + 32] ['s'] = life_status
        cases [i + 50] [j + 32] ['c'] = color
        cases [i + 50] [j + 33] ['s'] = life_status
        cases [i + 50] [j + 33] ['c'] = color
        cases [i + 50] [j + 34] ['s'] = life_status
        cases [i + 50] [j + 34] ['c'] = color
        cases [i + 50] [j + 35] ['s'] = life_status
        cases [i + 50] [j + 35] ['c'] = color
        cases [i + 50] [j + 36] ['s'] = life_status
        cases [i + 50] [j + 36] ['c'] = color
        cases [i + 50] [j + 37] ['s'] = life_status
        cases [i + 50] [j + 37] ['c'] = color
        cases [i + 50] [j + 38] ['s'] = life_status
        cases [i + 50] [j + 38] ['c'] = color
        cases [i + 50] [j + 39] ['s'] = life_status
        cases [i + 50] [j + 39] ['c'] = color
        cases [i + 50] [j + 40] ['s'] = life_status
        cases [i + 50] [j + 40] ['c'] = color
        cases [i + 50] [j + 41] ['s'] = life_status
        cases [i + 50] [j + 41] ['c'] = color
        cases [i + 50] [j + 42] ['s'] = life_status
        cases [i + 50] [j + 42] ['c'] = color
        cases [i + 50] [j + 43] ['s'] = life_status
        cases [i + 50] [j + 43] ['c'] = color
        cases [i + 50] [j + 44] ['s'] = life_status
        cases [i + 50] [j + 44] ['c'] = color
        cases [i + 50] [j + 45] ['s'] = life_status
        cases [i + 50] [j + 45] ['c'] = color
        cases [i + 50] [j + 46] ['s'] = life_status
        cases [i + 50] [j + 46] ['c'] = color
        cases [i + 50] [j + 47] ['s'] = life_status
        cases [i + 50] [j + 47] ['c'] = color
        cases [i + 50] [j + 48] ['s'] = life_status
        cases [i + 50] [j + 48] ['c'] = color
        cases [i + 50] [j + 49] ['s'] = life_status
        cases [i + 50] [j + 49] ['c'] = color
        cases [i + 50] [j + 50] ['s'] = life_status
        cases [i + 50] [j + 50] ['c'] = color
        cases [i + 50] [j + 51] ['s'] = life_status
        cases [i + 50] [j + 51] ['c'] = color
        cases [i + 50] [j + 52] ['s'] = life_status
        cases [i + 50] [j + 52] ['c'] = color
        cases [i + 50] [j + 53] ['s'] = life_status
        cases [i + 50] [j + 53] ['c'] = color
        cases [i + 50] [j + 54] ['s'] = life_status
        cases [i + 50] [j + 54] ['c'] = color
        cases [i + 50] [j + 55] ['s'] = life_status
        cases [i + 50] [j + 55] ['c'] = color
        cases [i + 50] [j + 56] ['s'] = life_status
        cases [i + 50] [j + 56] ['c'] = color
        cases [i + 50] [j + 57] ['s'] = life_status
        cases [i + 50] [j + 57] ['c'] = color
        cases [i + 50] [j + 58] ['s'] = life_status
        cases [i + 50] [j + 58] ['c'] = color
        cases [i + 50] [j + 59] ['s'] = life_status
        cases [i + 50] [j + 59] ['c'] = color
        cases [i + 50] [j + 60] ['s'] = life_status
        cases [i + 50] [j + 60] ['c'] = color
        cases [i + 50] [j + 61] ['s'] = life_status
        cases [i + 50] [j + 61] ['c'] = color
        
        
        
        
        
        color = 'black'
        cases [i + 49] [j + 28] ['s'] = life_status
        cases [i + 49] [j + 28] ['c'] = color
        cases [i + 49] [j + 29] ['s'] = life_status
        cases [i + 49] [j + 29] ['c'] = color
        cases [i + 49] [j + 30] ['s'] = life_status
        cases [i + 49] [j + 30] ['c'] = color
        cases [i + 49] [j + 31] ['s'] = life_status
        cases [i + 49] [j + 31] ['c'] = color
        cases [i + 49] [j + 32] ['s'] = life_status
        cases [i + 49] [j + 32] ['c'] = color
        cases [i + 49] [j + 33] ['s'] = life_status
        cases [i + 49] [j + 33] ['c'] = color
        
        cases [i + 49] [j + 61] ['s'] = life_status
        cases [i + 49] [j + 61] ['c'] = color
        cases [i + 49] [j + 62] ['s'] = life_status
        cases [i + 49] [j + 62] ['c'] = color
        cases [i + 49] [j + 63] ['s'] = life_status
        cases [i + 49] [j + 63] ['c'] = color
        cases [i + 49] [j + 64] ['s'] = life_status
        cases [i + 49] [j + 64] ['c'] = color
        cases [i + 49] [j + 65] ['s'] = life_status
        cases [i + 49] [j + 65] ['c'] = color
        cases [i + 49] [j + 66] ['s'] = life_status
        cases [i + 49] [j + 66] ['c'] = color
        
        
        cases [i + 48] [j + 27] ['s'] = life_status
        cases [i + 48] [j + 27] ['c'] = color
        cases [i + 48] [j + 28] ['s'] = life_status
        cases [i + 48] [j + 28] ['c'] = color
        cases [i + 48] [j + 29] ['s'] = life_status
        cases [i + 48] [j + 29] ['c'] = color
        cases [i + 48] [j + 30] ['s'] = life_status
        cases [i + 48] [j + 30] ['c'] = color
        cases [i + 48] [j + 31] ['s'] = life_status
        cases [i + 48] [j + 31] ['c'] = color
        cases [i + 48] [j + 32] ['s'] = life_status
        cases [i + 48] [j + 32] ['c'] = color
        cases [i + 48] [j + 33] ['s'] = life_status
        cases [i + 48] [j + 33] ['c'] = color
        cases [i + 48] [j + 34] ['s'] = life_status
        cases [i + 48] [j + 34] ['c'] = color
        
        cases [i + 48] [j + 60] ['s'] = life_status
        cases [i + 48] [j + 60] ['c'] = color
        cases [i + 48] [j + 61] ['s'] = life_status
        cases [i + 48] [j + 61] ['c'] = color
        cases [i + 48] [j + 62] ['s'] = life_status
        cases [i + 48] [j + 62] ['c'] = color
        cases [i + 48] [j + 63] ['s'] = life_status
        cases [i + 48] [j + 63] ['c'] = color
        cases [i + 48] [j + 64] ['s'] = life_status
        cases [i + 48] [j + 64] ['c'] = color
        cases [i + 48] [j + 65] ['s'] = life_status
        cases [i + 48] [j + 65] ['c'] = color
        cases [i + 48] [j + 66] ['s'] = life_status
        cases [i + 48] [j + 66] ['c'] = color
        cases [i + 48] [j + 67] ['s'] = life_status
        cases [i + 48] [j + 67] ['c'] = color
        
        
        cases [i + 47] [j + 26] ['s'] = life_status
        cases [i + 47] [j + 26] ['c'] = color
        cases [i + 47] [j + 27] ['s'] = life_status
        cases [i + 47] [j + 27] ['c'] = color
        cases [i + 47] [j + 28] ['s'] = life_status
        cases [i + 47] [j + 28] ['c'] = color
        cases [i + 47] [j + 29] ['s'] = life_status
        cases [i + 47] [j + 29] ['c'] = color
        cases [i + 47] [j + 30] ['s'] = life_status
        cases [i + 47] [j + 30] ['c'] = color
        cases [i + 47] [j + 31] ['s'] = life_status
        cases [i + 47] [j + 31] ['c'] = color
        cases [i + 47] [j + 32] ['s'] = life_status
        cases [i + 47] [j + 32] ['c'] = color
        cases [i + 47] [j + 33] ['s'] = life_status
        cases [i + 47] [j + 33] ['c'] = color
        cases [i + 47] [j + 34] ['s'] = life_status
        cases [i + 47] [j + 34] ['c'] = color
        cases [i + 47] [j + 35] ['s'] = life_status
        cases [i + 47] [j + 35] ['c'] = color
        
        cases [i + 47] [j + 59] ['s'] = life_status
        cases [i + 47] [j + 59] ['c'] = color
        cases [i + 47] [j + 60] ['s'] = life_status
        cases [i + 47] [j + 60] ['c'] = color
        cases [i + 47] [j + 61] ['s'] = life_status
        cases [i + 47] [j + 61] ['c'] = color
        cases [i + 47] [j + 62] ['s'] = life_status
        cases [i + 47] [j + 62] ['c'] = color
        cases [i + 47] [j + 63] ['s'] = life_status
        cases [i + 47] [j + 63] ['c'] = color
        cases [i + 47] [j + 64] ['s'] = life_status
        cases [i + 47] [j + 64] ['c'] = color
        cases [i + 47] [j + 65] ['s'] = life_status
        cases [i + 47] [j + 65] ['c'] = color
        cases [i + 47] [j + 66] ['s'] = life_status
        cases [i + 47] [j + 66] ['c'] = color
        cases [i + 47] [j + 67] ['s'] = life_status
        cases [i + 47] [j + 67] ['c'] = color
        cases [i + 47] [j + 68] ['s'] = life_status
        cases [i + 47] [j + 68] ['c'] = color
        
        
        cases [i + 46] [j + 25] ['s'] = life_status
        cases [i + 46] [j + 25] ['c'] = color
        cases [i + 46] [j + 26] ['s'] = life_status
        cases [i + 46] [j + 26] ['c'] = color
        cases [i + 46] [j + 27] ['s'] = life_status
        cases [i + 46] [j + 27] ['c'] = color
        cases [i + 46] [j + 28] ['s'] = life_status
        cases [i + 46] [j + 28] ['c'] = color
        cases [i + 46] [j + 33] ['s'] = life_status
        cases [i + 46] [j + 33] ['c'] = color
        cases [i + 46] [j + 34] ['s'] = life_status
        cases [i + 46] [j + 34] ['c'] = color
        cases [i + 46] [j + 35] ['s'] = life_status
        cases [i + 46] [j + 35] ['c'] = color
        cases [i + 46] [j + 36] ['s'] = life_status
        cases [i + 46] [j + 36] ['c'] = color
        
        cases [i + 46] [j + 58] ['s'] = life_status
        cases [i + 46] [j + 58] ['c'] = color
        cases [i + 46] [j + 59] ['s'] = life_status
        cases [i + 46] [j + 59] ['c'] = color
        cases [i + 46] [j + 60] ['s'] = life_status
        cases [i + 46] [j + 60] ['c'] = color
        cases [i + 46] [j + 61] ['s'] = life_status
        cases [i + 46] [j + 61] ['c'] = color
        cases [i + 46] [j + 66] ['s'] = life_status
        cases [i + 46] [j + 66] ['c'] = color
        cases [i + 46] [j + 67] ['s'] = life_status
        cases [i + 46] [j + 67] ['c'] = color
        cases [i + 46] [j + 68] ['s'] = life_status
        cases [i + 46] [j + 68] ['c'] = color
        cases [i + 46] [j + 69] ['s'] = life_status
        cases [i + 46] [j + 69] ['c'] = color
        
        
        cases [i + 45] [j + 25] ['s'] = life_status
        cases [i + 45] [j + 25] ['c'] = color
        cases [i + 45] [j + 26] ['s'] = life_status
        cases [i + 45] [j + 26] ['c'] = color
        cases [i + 45] [j + 27] ['s'] = life_status
        cases [i + 45] [j + 27] ['c'] = color
        cases [i + 45] [j + 34] ['s'] = life_status
        cases [i + 45] [j + 34] ['c'] = color
        cases [i + 45] [j + 35] ['s'] = life_status
        cases [i + 45] [j + 35] ['c'] = color
        cases [i + 45] [j + 36] ['s'] = life_status
        cases [i + 45] [j + 36] ['c'] = color
        
        cases [i + 45] [j + 58] ['s'] = life_status
        cases [i + 45] [j + 58] ['c'] = color
        cases [i + 45] [j + 59] ['s'] = life_status
        cases [i + 45] [j + 59] ['c'] = color
        cases [i + 45] [j + 60] ['s'] = life_status
        cases [i + 45] [j + 60] ['c'] = color
        cases [i + 45] [j + 67] ['s'] = life_status
        cases [i + 45] [j + 67] ['c'] = color
        cases [i + 45] [j + 68] ['s'] = life_status
        cases [i + 45] [j + 68] ['c'] = color
        cases [i + 45] [j + 69] ['s'] = life_status
        cases [i + 45] [j + 69] ['c'] = color
        
        
        
        cases [i + 44] [j + 25] ['s'] = life_status
        cases [i + 44] [j + 25] ['c'] = color
        cases [i + 44] [j + 26] ['s'] = life_status
        cases [i + 44] [j + 26] ['c'] = color
        cases [i + 44] [j + 27] ['s'] = life_status
        cases [i + 44] [j + 27] ['c'] = color
        cases [i + 44] [j + 34] ['s'] = life_status
        cases [i + 44] [j + 34] ['c'] = color
        cases [i + 44] [j + 35] ['s'] = life_status
        cases [i + 44] [j + 35] ['c'] = color
        cases [i + 44] [j + 36] ['s'] = life_status
        cases [i + 44] [j + 36] ['c'] = color
        
        cases [i + 44] [j + 58] ['s'] = life_status
        cases [i + 44] [j + 58] ['c'] = color
        cases [i + 44] [j + 59] ['s'] = life_status
        cases [i + 44] [j + 59] ['c'] = color
        cases [i + 44] [j + 60] ['s'] = life_status
        cases [i + 44] [j + 60] ['c'] = color
        cases [i + 44] [j + 67] ['s'] = life_status
        cases [i + 44] [j + 67] ['c'] = color
        cases [i + 44] [j + 68] ['s'] = life_status
        cases [i + 44] [j + 68] ['c'] = color
        cases [i + 44] [j + 69] ['s'] = life_status
        cases [i + 44] [j + 69] ['c'] = color
        
        
        cases [i + 43] [j + 25] ['s'] = life_status
        cases [i + 43] [j + 25] ['c'] = color
        cases [i + 43] [j + 26] ['s'] = life_status
        cases [i + 43] [j + 26] ['c'] = color
        cases [i + 43] [j + 27] ['s'] = life_status
        cases [i + 43] [j + 27] ['c'] = color
        cases [i + 43] [j + 34] ['s'] = life_status
        cases [i + 43] [j + 34] ['c'] = color
        cases [i + 43] [j + 35] ['s'] = life_status
        cases [i + 43] [j + 35] ['c'] = color
        cases [i + 43] [j + 36] ['s'] = life_status
        cases [i + 43] [j + 36] ['c'] = color
        
        cases [i + 43] [j + 58] ['s'] = life_status
        cases [i + 43] [j + 58] ['c'] = color
        cases [i + 43] [j + 59] ['s'] = life_status
        cases [i + 43] [j + 59] ['c'] = color
        cases [i + 43] [j + 60] ['s'] = life_status
        cases [i + 43] [j + 60] ['c'] = color
        cases [i + 43] [j + 67] ['s'] = life_status
        cases [i + 43] [j + 67] ['c'] = color
        cases [i + 43] [j + 68] ['s'] = life_status
        cases [i + 43] [j + 68] ['c'] = color
        cases [i + 43] [j + 69] ['s'] = life_status
        cases [i + 43] [j + 69] ['c'] = color
        
        
        cases [i + 42] [j + 25] ['s'] = life_status
        cases [i + 42] [j + 25] ['c'] = color
        cases [i + 42] [j + 26] ['s'] = life_status
        cases [i + 42] [j + 26] ['c'] = color
        cases [i + 42] [j + 27] ['s'] = life_status
        cases [i + 42] [j + 27] ['c'] = color
        cases [i + 42] [j + 34] ['s'] = life_status
        cases [i + 42] [j + 34] ['c'] = color
        cases [i + 42] [j + 35] ['s'] = life_status
        cases [i + 42] [j + 35] ['c'] = color
        
        cases [i + 42] [j + 58] ['s'] = life_status
        cases [i + 42] [j + 58] ['c'] = color
        cases [i + 42] [j + 59] ['s'] = life_status
        cases [i + 42] [j + 59] ['c'] = color
        cases [i + 42] [j + 60] ['s'] = life_status
        cases [i + 42] [j + 60] ['c'] = color
        cases [i + 42] [j + 67] ['s'] = life_status
        cases [i + 42] [j + 67] ['c'] = color
        cases [i + 42] [j + 68] ['s'] = life_status
        cases [i + 42] [j + 68] ['c'] = color
        cases [i + 42] [j + 69] ['s'] = life_status
        cases [i + 42] [j + 69] ['c'] = color
        
        
        cases [i + 41] [j + 25] ['s'] = life_status
        cases [i + 41] [j + 25] ['c'] = color
        cases [i + 41] [j + 26] ['s'] = life_status
        cases [i + 41] [j + 26] ['c'] = color
        cases [i + 41] [j + 27] ['s'] = life_status
        cases [i + 41] [j + 27] ['c'] = color
        cases [i + 41] [j + 28] ['s'] = life_status
        cases [i + 41] [j + 28] ['c'] = color
        cases [i + 41] [j + 34] ['s'] = life_status
        cases [i + 41] [j + 34] ['c'] = color
        
        
        cases [i + 40] [j + 26] ['s'] = life_status
        cases [i + 40] [j + 26] ['c'] = color
        cases [i + 40] [j + 27] ['s'] = life_status
        cases [i + 40] [j + 27] ['c'] = color
        cases [i + 40] [j + 28] ['s'] = life_status
        cases [i + 40] [j + 28] ['c'] = color
        cases [i + 40] [j + 29] ['s'] = life_status
        cases [i + 40] [j + 29] ['c'] = color
        cases [i + 40] [j + 30] ['s'] = life_status
        cases [i + 40] [j + 30] ['c'] = color
        cases [i + 40] [j + 31] ['s'] = life_status
        cases [i + 40] [j + 31] ['c'] = color
        cases [i + 40] [j + 32] ['s'] = life_status
        cases [i + 40] [j + 32] ['c'] = color
        
        
        
        cases [i + 39] [j + 27] ['s'] = life_status
        cases [i + 39] [j + 27] ['c'] = color
        cases [i + 39] [j + 28] ['s'] = life_status
        cases [i + 39] [j + 28] ['c'] = color
        cases [i + 39] [j + 29] ['s'] = life_status
        cases [i + 39] [j + 29] ['c'] = color
        cases [i + 39] [j + 30] ['s'] = life_status
        cases [i + 39] [j + 30] ['c'] = color
        cases [i + 39] [j + 31] ['s'] = life_status
        cases [i + 39] [j + 31] ['c'] = color
        
    
        
        color = "grey"
        cases [i + 46] [j + 29] ['s'] = life_status
        cases [i + 46] [j + 29] ['c'] = color
        cases [i + 46] [j + 30] ['s'] = life_status
        cases [i + 46] [j + 30] ['c'] = color
        cases [i + 46] [j + 31] ['s'] = life_status
        cases [i + 46] [j + 31] ['c'] = color
        cases [i + 46] [j + 32] ['s'] = life_status
        cases [i + 46] [j + 32] ['c'] = color
        
        cases [i + 46] [j + 62] ['s'] = life_status
        cases [i + 46] [j + 62] ['c'] = color
        cases [i + 46] [j + 63] ['s'] = life_status
        cases [i + 46] [j + 63] ['c'] = color
        cases [i + 46] [j + 64] ['s'] = life_status
        cases [i + 46] [j + 64] ['c'] = color
        cases [i + 46] [j + 65] ['s'] = life_status
        cases [i + 46] [j + 65] ['c'] = color
        
        
        cases [i + 45] [j + 28] ['s'] = life_status
        cases [i + 45] [j + 28] ['c'] = color
        cases [i + 45] [j + 29] ['s'] = life_status
        cases [i + 45] [j + 29] ['c'] = color
        cases [i + 45] [j + 30] ['s'] = life_status
        cases [i + 45] [j + 30] ['c'] = color
        cases [i + 45] [j + 31] ['s'] = life_status
        cases [i + 45] [j + 31] ['c'] = color
        cases [i + 45] [j + 32] ['s'] = life_status
        cases [i + 45] [j + 32] ['c'] = color
        cases [i + 45] [j + 33] ['s'] = life_status
        cases [i + 45] [j + 33] ['c'] = color
        
        cases [i + 45] [j + 61] ['s'] = life_status
        cases [i + 45] [j + 61] ['c'] = color
        cases [i + 45] [j + 62] ['s'] = life_status
        cases [i + 45] [j + 62] ['c'] = color
        cases [i + 45] [j + 63] ['s'] = life_status
        cases [i + 45] [j + 63] ['c'] = color
        cases [i + 45] [j + 64] ['s'] = life_status
        cases [i + 45] [j + 64] ['c'] = color
        cases [i + 45] [j + 65] ['s'] = life_status
        cases [i + 45] [j + 65] ['c'] = color
        cases [i + 45] [j + 66] ['s'] = life_status
        cases [i + 45] [j + 66] ['c'] = color
        
        
        cases [i + 44] [j + 28] ['s'] = life_status
        cases [i + 44] [j + 28] ['c'] = color
        cases [i + 44] [j + 29] ['s'] = life_status
        cases [i + 44] [j + 29] ['c'] = color
        cases [i + 44] [j + 30] ['s'] = life_status
        cases [i + 44] [j + 30] ['c'] = color
        cases [i + 44] [j + 31] ['s'] = life_status
        cases [i + 44] [j + 31] ['c'] = color
        cases [i + 44] [j + 32] ['s'] = life_status
        cases [i + 44] [j + 32] ['c'] = color
        cases [i + 44] [j + 33] ['s'] = life_status
        cases [i + 44] [j + 33] ['c'] = color
        
        cases [i + 44] [j + 61] ['s'] = life_status
        cases [i + 44] [j + 61] ['c'] = color
        cases [i + 44] [j + 62] ['s'] = life_status
        cases [i + 44] [j + 62] ['c'] = color
        cases [i + 44] [j + 63] ['s'] = life_status
        cases [i + 44] [j + 63] ['c'] = color
        cases [i + 44] [j + 64] ['s'] = life_status
        cases [i + 44] [j + 64] ['c'] = color
        cases [i + 44] [j + 65] ['s'] = life_status
        cases [i + 44] [j + 65] ['c'] = color
        cases [i + 44] [j + 66] ['s'] = life_status
        cases [i + 44] [j + 66] ['c'] = color
        
        
        cases [i + 43] [j + 28] ['s'] = life_status
        cases [i + 43] [j + 28] ['c'] = color
        cases [i + 43] [j + 29] ['s'] = life_status
        cases [i + 43] [j + 29] ['c'] = color
        cases [i + 43] [j + 30] ['s'] = life_status
        cases [i + 43] [j + 30] ['c'] = color
        cases [i + 43] [j + 31] ['s'] = life_status
        cases [i + 43] [j + 31] ['c'] = color
        cases [i + 43] [j + 32] ['s'] = life_status
        cases [i + 43] [j + 32] ['c'] = color
        cases [i + 43] [j + 33] ['s'] = life_status
        cases [i + 43] [j + 33] ['c'] = color
        
        cases [i + 43] [j + 61] ['s'] = life_status
        cases [i + 43] [j + 61] ['c'] = color
        cases [i + 43] [j + 62] ['s'] = life_status
        cases [i + 43] [j + 62] ['c'] = color
        cases [i + 43] [j + 63] ['s'] = life_status
        cases [i + 43] [j + 63] ['c'] = color
        cases [i + 43] [j + 64] ['s'] = life_status
        cases [i + 43] [j + 64] ['c'] = color
        cases [i + 43] [j + 65] ['s'] = life_status
        cases [i + 43] [j + 65] ['c'] = color
        cases [i + 43] [j + 66] ['s'] = life_status
        cases [i + 43] [j + 66] ['c'] = color
        
        
        cases [i + 42] [j + 28] ['s'] = life_status
        cases [i + 42] [j + 28] ['c'] = color
        cases [i + 42] [j + 29] ['s'] = life_status
        cases [i + 42] [j + 29] ['c'] = color
        cases [i + 42] [j + 30] ['s'] = life_status
        cases [i + 42] [j + 30] ['c'] = color
        cases [i + 42] [j + 32] ['s'] = life_status
        cases [i + 42] [j + 32] ['c'] = color
        cases [i + 42] [j + 33] ['s'] = life_status
        cases [i + 42] [j + 33] ['c'] = color
        
        cases [i + 42] [j + 61] ['s'] = life_status
        cases [i + 42] [j + 61] ['c'] = color
        cases [i + 42] [j + 62] ['s'] = life_status
        cases [i + 42] [j + 62] ['c'] = color
        cases [i + 42] [j + 63] ['s'] = life_status
        cases [i + 42] [j + 63] ['c'] = color
        cases [i + 42] [j + 64] ['s'] = life_status
        cases [i + 42] [j + 64] ['c'] = color
        cases [i + 42] [j + 65] ['s'] = life_status
        cases [i + 42] [j + 65] ['c'] = color
        cases [i + 42] [j + 66] ['s'] = life_status
        cases [i + 42] [j + 66] ['c'] = color
        
        
        cases [i + 41] [j + 29] ['s'] = life_status
        cases [i + 41] [j + 29] ['c'] = color
        cases [i + 41] [j + 30] ['s'] = life_status
        cases [i + 41] [j + 30] ['c'] = color
        cases [i + 41] [j + 31] ['s'] = life_status
        cases [i + 41] [j + 31] ['c'] = color
        cases [i + 41] [j + 33] ['s'] = life_status
        cases [i + 41] [j + 33] ['c'] = color
        
        
        
        color = "red"
        
        cases [i + 38] [j + 26] ['s'] = life_status
        cases [i + 38] [j + 26] ['c'] = color
        cases [i + 38] [j + 27] ['s'] = life_status
        cases [i + 38] [j + 27] ['c'] = color
        cases [i + 38] [j + 28] ['s'] = life_status
        cases [i + 38] [j + 28] ['c'] = color
        cases [i + 38] [j + 29] ['s'] = life_status
        cases [i + 38] [j + 29] ['c'] = color
        cases [i + 38] [j + 30] ['s'] = life_status
        cases [i + 38] [j + 30] ['c'] = color
        cases [i + 38] [j + 31] ['s'] = life_status
        cases [i + 38] [j + 31] ['c'] = color
        cases [i + 38] [j + 32] ['s'] = life_status
        cases [i + 38] [j + 32] ['c'] = color
        cases [i + 38] [j + 33] ['s'] = life_status
        cases [i + 38] [j + 33] ['c'] = color
        cases [i + 38] [j + 34] ['s'] = life_status
        cases [i + 38] [j + 34] ['c'] = color
        cases [i + 38] [j + 35] ['s'] = life_status
        cases [i + 38] [j + 35] ['c'] = color
        cases [i + 38] [j + 36] ['s'] = life_status
        cases [i + 38] [j + 36] ['c'] = color
        
        
        cases [i + 37] [j + 27] ['s'] = life_status
        cases [i + 37] [j + 27] ['c'] = color
        cases [i + 37] [j + 28] ['s'] = life_status
        cases [i + 37] [j + 28] ['c'] = color
        cases [i + 37] [j + 29] ['s'] = life_status
        cases [i + 37] [j + 29] ['c'] = color
        cases [i + 37] [j + 30] ['s'] = life_status
        cases [i + 37] [j + 30] ['c'] = color
        cases [i + 37] [j + 31] ['s'] = life_status
        cases [i + 37] [j + 31] ['c'] = color
        cases [i + 37] [j + 32] ['s'] = life_status
        cases [i + 37] [j + 32] ['c'] = color
        cases [i + 37] [j + 33] ['s'] = life_status
        cases [i + 37] [j + 33] ['c'] = color
        cases [i + 37] [j + 34] ['s'] = life_status
        cases [i + 37] [j + 34] ['c'] = color
        cases [i + 37] [j + 35] ['s'] = life_status
        cases [i + 37] [j + 35] ['c'] = color
        
        
        cases [i + 36] [j + 28] ['s'] = life_status
        cases [i + 36] [j + 28] ['c'] = color
        cases [i + 36] [j + 29] ['s'] = life_status
        cases [i + 36] [j + 29] ['c'] = color
        cases [i + 36] [j + 30] ['s'] = life_status
        cases [i + 36] [j + 30] ['c'] = color
        cases [i + 36] [j + 31] ['s'] = life_status
        cases [i + 36] [j + 31] ['c'] = color
        cases [i + 36] [j + 32] ['s'] = life_status
        cases [i + 36] [j + 32] ['c'] = color
        cases [i + 36] [j + 33] ['s'] = life_status
        cases [i + 36] [j + 33] ['c'] = color
        cases [i + 36] [j + 34] ['s'] = life_status
        cases [i + 36] [j + 34] ['c'] = color
        cases [i + 36] [j + 35] ['s'] = life_status
        cases [i + 36] [j + 35] ['c'] = color
        
        
        cases [i + 35] [j + 30] ['s'] = life_status
        cases [i + 35] [j + 30] ['c'] = color
        cases [i + 35] [j + 31] ['s'] = life_status
        cases [i + 35] [j + 31] ['c'] = color
        cases [i + 35] [j + 32] ['s'] = life_status
        cases [i + 35] [j + 32] ['c'] = color
        cases [i + 35] [j + 33] ['s'] = life_status
        cases [i + 35] [j + 33] ['c'] = color
        cases [i + 35] [j + 34] ['s'] = life_status
        cases [i + 35] [j + 34] ['c'] = color
        
        
        cases [i + 39] [j + 32] ['s'] = life_status
        cases [i + 39] [j + 32] ['c'] = color
        cases [i + 39] [j + 33] ['s'] = life_status
        cases [i + 39] [j + 33] ['c'] = color
        cases [i + 39] [j + 34] ['s'] = life_status
        cases [i + 39] [j + 34] ['c'] = color
        cases [i + 39] [j + 35] ['s'] = life_status
        cases [i + 39] [j + 35] ['c'] = color
        cases [i + 39] [j + 36] ['s'] = life_status
        cases [i + 39] [j + 36] ['c'] = color
        
        
        cases [i + 40] [j + 33] ['s'] = life_status
        cases [i + 40] [j + 33] ['c'] = color
        cases [i + 40] [j + 34] ['s'] = life_status
        cases [i + 40] [j + 34] ['c'] = color
        cases [i + 40] [j + 35] ['s'] = life_status
        cases [i + 40] [j + 35] ['c'] = color
        cases [i + 40] [j + 36] ['s'] = life_status
        cases [i + 40] [j + 36] ['c'] = color
        cases [i + 40] [j + 37] ['s'] = life_status
        cases [i + 40] [j + 37] ['c'] = color
        cases [i + 40] [j + 38] ['s'] = life_status
        cases [i + 40] [j + 38] ['c'] = color
        cases [i + 40] [j + 39] ['s'] = life_status
        cases [i + 40] [j + 39] ['c'] = color
        
        
        cases [i + 41] [j + 35] ['s'] = life_status
        cases [i + 41] [j + 35] ['c'] = color
        cases [i + 41] [j + 36] ['s'] = life_status
        cases [i + 41] [j + 36] ['c'] = color
        cases [i + 41] [j + 37] ['s'] = life_status
        cases [i + 41] [j + 37] ['c'] = color
        cases [i + 41] [j + 38] ['s'] = life_status
        cases [i + 41] [j + 38] ['c'] = color
        cases [i + 41] [j + 39] ['s'] = life_status
        cases [i + 41] [j + 39] ['c'] = color
        
        
        cases [i + 42] [j + 36] ['s'] = life_status
        cases [i + 42] [j + 36] ['c'] = color
        cases [i + 42] [j + 37] ['s'] = life_status
        cases [i + 42] [j + 37] ['c'] = color
        cases [i + 42] [j + 38] ['s'] = life_status
        cases [i + 42] [j + 38] ['c'] = color
        cases [i + 42] [j + 39] ['s'] = life_status
        cases [i + 42] [j + 39] ['c'] = color
        
        
        cases [i + 43] [j + 38] ['s'] = life_status
        cases [i + 43] [j + 38] ['c'] = color
        cases [i + 43] [j + 39] ['s'] = life_status
        cases [i + 43] [j + 39] ['c'] = color
        cases [i + 43] [j + 40] ['s'] = life_status
        cases [i + 43] [j + 40] ['c'] = color
        
        cases [i + 44] [j + 39] ['s'] = life_status
        cases [i + 44] [j + 39] ['c'] = color
        cases [i + 44] [j + 40] ['s'] = life_status
        cases [i + 44] [j + 40] ['c'] = color
        
        cases [i + 42] [j + 31] ['s'] = life_status
        cases [i + 42] [j + 31] ['c'] = color
        cases [i + 41] [j + 32] ['s'] = life_status
        cases [i + 41] [j + 32] ['c'] = color
        
        
        
        
        color = "palegoldenrod"
        cases [i + 43] [j + 41] ['s'] = life_status
        cases [i + 43] [j + 41] ['c'] = color
        cases [i + 43] [j + 42] ['s'] = life_status
        cases [i + 43] [j + 42] ['c'] = color
        cases [i + 43] [j + 43] ['s'] = life_status
        cases [i + 43] [j + 43] ['c'] = color
        cases [i + 43] [j + 44] ['s'] = life_status
        cases [i + 43] [j + 44] ['c'] = color
        cases [i + 43] [j + 45] ['s'] = life_status
        cases [i + 43] [j + 45] ['c'] = color
        cases [i + 43] [j + 46] ['s'] = life_status
        cases [i + 43] [j + 46] ['c'] = color
        cases [i + 43] [j + 47] ['s'] = life_status
        cases [i + 43] [j + 47] ['c'] = color
        cases [i + 43] [j + 48] ['s'] = life_status
        cases [i + 43] [j + 48] ['c'] = color
        cases [i + 43] [j + 49] ['s'] = life_status
        cases [i + 43] [j + 49] ['c'] = color
        cases [i + 43] [j + 50] ['s'] = life_status
        cases [i + 43] [j + 50] ['c'] = color
        cases [i + 43] [j + 51] ['s'] = life_status
        cases [i + 43] [j + 51] ['c'] = color
        cases [i + 43] [j + 52] ['s'] = life_status
        cases [i + 43] [j + 52] ['c'] = color
        cases [i + 43] [j + 53] ['s'] = life_status
        cases [i + 43] [j + 53] ['c'] = color
        cases [i + 43] [j + 54] ['s'] = life_status
        cases [i + 43] [j + 54] ['c'] = color
        cases [i + 43] [j + 55] ['s'] = life_status
        cases [i + 43] [j + 55] ['c'] = color
        cases [i + 43] [j + 56] ['s'] = life_status
        cases [i + 43] [j + 56] ['c'] = color
        cases [i + 43] [j + 57] ['s'] = life_status
        cases [i + 43] [j + 57] ['c'] = color
        
        
        
        
        cases [i + 42] [j + 40] ['s'] = life_status
        cases [i + 42] [j + 40] ['c'] = color
        cases [i + 42] [j + 41] ['s'] = life_status
        cases [i + 42] [j + 41] ['c'] = color
        cases [i + 42] [j + 42] ['s'] = life_status
        cases [i + 42] [j + 42] ['c'] = color
        cases [i + 42] [j + 43] ['s'] = life_status
        cases [i + 42] [j + 43] ['c'] = color
        cases [i + 42] [j + 44] ['s'] = life_status
        cases [i + 42] [j + 44] ['c'] = color
        cases [i + 42] [j + 45] ['s'] = life_status
        cases [i + 42] [j + 45] ['c'] = color
        cases [i + 42] [j + 46] ['s'] = life_status
        cases [i + 42] [j + 46] ['c'] = color
        cases [i + 42] [j + 47] ['s'] = life_status
        cases [i + 42] [j + 47] ['c'] = color
        cases [i + 42] [j + 48] ['s'] = life_status
        cases [i + 42] [j + 48] ['c'] = color
        cases [i + 42] [j + 49] ['s'] = life_status
        cases [i + 42] [j + 49] ['c'] = color
        cases [i + 42] [j + 50] ['s'] = life_status
        cases [i + 42] [j + 50] ['c'] = color
        cases [i + 42] [j + 51] ['s'] = life_status
        cases [i + 42] [j + 51] ['c'] = color
        cases [i + 42] [j + 52] ['s'] = life_status
        cases [i + 42] [j + 52] ['c'] = color
        cases [i + 42] [j + 53] ['s'] = life_status
        cases [i + 42] [j + 53] ['c'] = color
        cases [i + 42] [j + 54] ['s'] = life_status
        cases [i + 42] [j + 54] ['c'] = color
        cases [i + 42] [j + 55] ['s'] = life_status
        cases [i + 42] [j + 55] ['c'] = color
        cases [i + 42] [j + 56] ['s'] = life_status
        cases [i + 42] [j + 56] ['c'] = color
        cases [i + 42] [j + 57] ['s'] = life_status
        cases [i + 42] [j + 57] ['c'] = color
        
        
        cases [i + 41] [j + 40] ['s'] = life_status
        cases [i + 41] [j + 40] ['c'] = color
        cases [i + 41] [j + 41] ['s'] = life_status
        cases [i + 41] [j + 41] ['c'] = color
        cases [i + 41] [j + 42] ['s'] = life_status
        cases [i + 41] [j + 42] ['c'] = color
        cases [i + 41] [j + 43] ['s'] = life_status
        cases [i + 41] [j + 43] ['c'] = color
        cases [i + 41] [j + 44] ['s'] = life_status
        cases [i + 41] [j + 44] ['c'] = color
        cases [i + 41] [j + 45] ['s'] = life_status
        cases [i + 41] [j + 45] ['c'] = color
        cases [i + 41] [j + 46] ['s'] = life_status
        cases [i + 41] [j + 46] ['c'] = color
        cases [i + 41] [j + 50] ['s'] = life_status
        cases [i + 41] [j + 50] ['c'] = color
        cases [i + 41] [j + 51] ['s'] = life_status
        cases [i + 41] [j + 51] ['c'] = color
        cases [i + 41] [j + 52] ['s'] = life_status
        cases [i + 41] [j + 52] ['c'] = color
        cases [i + 41] [j + 53] ['s'] = life_status
        cases [i + 41] [j + 53] ['c'] = color
        cases [i + 41] [j + 54] ['s'] = life_status
        cases [i + 41] [j + 54] ['c'] = color
        cases [i + 41] [j + 55] ['s'] = life_status
        cases [i + 41] [j + 55] ['c'] = color
        
        
        cases [i + 40] [j + 51] ['s'] = life_status
        cases [i + 40] [j + 51] ['c'] = color
        cases [i + 40] [j + 52] ['s'] = life_status
        cases [i + 40] [j + 52] ['c'] = color
        cases [i + 39] [j + 51] ['s'] = life_status
        cases [i + 39] [j + 51] ['c'] = color
        cases [i + 39] [j + 52] ['s'] = life_status
        cases [i + 39] [j + 52] ['c'] = color
        cases [i + 38] [j + 51] ['s'] = life_status
        cases [i + 38] [j + 51] ['c'] = color
        cases [i + 38] [j + 52] ['s'] = life_status
        cases [i + 38] [j + 52] ['c'] = color
        cases [i + 37] [j + 51] ['s'] = life_status
        cases [i + 37] [j + 51] ['c'] = color
        cases [i + 37] [j + 52] ['s'] = life_status
        cases [i + 37] [j + 52] ['c'] = color
        cases [i + 36] [j + 51] ['s'] = life_status
        cases [i + 36] [j + 51] ['c'] = color
        cases [i + 36] [j + 52] ['s'] = life_status
        cases [i + 36] [j + 52] ['c'] = color
        cases [i + 35] [j + 51] ['s'] = life_status
        cases [i + 35] [j + 51] ['c'] = color
        cases [i + 35] [j + 52] ['s'] = life_status
        cases [i + 35] [j + 52] ['c'] = color
        
        cases [i + 34] [j + 50] ['s'] = life_status
        cases [i + 34] [j + 50] ['c'] = color
        cases [i + 34] [j + 51] ['s'] = life_status
        cases [i + 34] [j + 51] ['c'] = color
        cases [i + 34] [j + 52] ['s'] = life_status
        cases [i + 34] [j + 52] ['c'] = color
        cases [i + 34] [j + 53] ['s'] = life_status
        cases [i + 34] [j + 53] ['c'] = color
        
        
        cases [i + 33] [j + 50] ['s'] = life_status
        cases [i + 33] [j + 50] ['c'] = color
        cases [i + 33] [j + 51] ['s'] = life_status
        cases [i + 33] [j + 51] ['c'] = color
        cases [i + 33] [j + 52] ['s'] = life_status
        cases [i + 33] [j + 52] ['c'] = color
        cases [i + 33] [j + 53] ['s'] = life_status
        cases [i + 33] [j + 53] ['c'] = color
        cases [i + 33] [j + 54] ['s'] = life_status
        cases [i + 33] [j + 54] ['c'] = color
        
        
        cases [i + 32] [j + 55] ['s'] = life_status
        cases [i + 32] [j + 55] ['c'] = color
        cases [i + 32] [j + 56] ['s'] = life_status
        cases [i + 32] [j + 56] ['c'] = color
        cases [i + 32] [j + 57] ['s'] = life_status
        cases [i + 32] [j + 57] ['c'] = color
        cases [i + 32] [j + 58] ['s'] = life_status
        cases [i + 32] [j + 58] ['c'] = color
        cases [i + 32] [j + 59] ['s'] = life_status
        cases [i + 32] [j + 59] ['c'] = color
        cases [i + 32] [j + 60] ['s'] = life_status
        cases [i + 32] [j + 60] ['c'] = color
        cases [i + 32] [j + 61] ['s'] = life_status
        cases [i + 32] [j + 61] ['c'] = color
        cases [i + 32] [j + 62] ['s'] = life_status
        cases [i + 32] [j + 62] ['c'] = color
        cases [i + 32] [j + 63] ['s'] = life_status
        cases [i + 32] [j + 63] ['c'] = color
        cases [i + 32] [j + 64] ['s'] = life_status
        cases [i + 32] [j + 64] ['c'] = color
        cases [i + 32] [j + 65] ['s'] = life_status
        cases [i + 32] [j + 65] ['c'] = color
        cases [i + 32] [j + 66] ['s'] = life_status
        cases [i + 32] [j + 66] ['c'] = color
        cases [i + 32] [j + 67] ['s'] = life_status
        cases [i + 32] [j + 67] ['c'] = color
        cases [i + 32] [j + 68] ['s'] = life_status
        cases [i + 32] [j + 68] ['c'] = color
        cases [i + 32] [j + 69] ['s'] = life_status
        cases [i + 32] [j + 69] ['c'] = color
        cases [i + 32] [j + 70] ['s'] = life_status
        cases [i + 32] [j + 70] ['c'] = color
        
        
        cases [i + 33] [j + 67] ['s'] = life_status
        cases [i + 33] [j + 67] ['c'] = color
        cases [i + 33] [j + 68] ['s'] = life_status
        cases [i + 33] [j + 68] ['c'] = color
        cases [i + 33] [j + 69] ['s'] = life_status
        cases [i + 33] [j + 69] ['c'] = color
        cases [i + 33] [j + 70] ['s'] = life_status
        cases [i + 33] [j + 70] ['c'] = color
        cases [i + 33] [j + 71] ['s'] = life_status
        cases [i + 33] [j + 71] ['c'] = color
        
        cases [i + 34] [j + 69] ['s'] = life_status
        cases [i + 34] [j + 69] ['c'] = color
        cases [i + 34] [j + 70] ['s'] = life_status
        cases [i + 34] [j + 70] ['c'] = color
        cases [i + 34] [j + 71] ['s'] = life_status
        cases [i + 34] [j + 71] ['c'] = color
        
        cases [i + 35] [j + 70] ['s'] = life_status
        cases [i + 35] [j + 70] ['c'] = color
        cases [i + 35] [j + 71] ['s'] = life_status
        cases [i + 35] [j + 71] ['c'] = color
        cases [i + 35] [j + 72] ['s'] = life_status
        cases [i + 35] [j + 72] ['c'] = color
        
        
        cases [i + 36] [j + 71] ['s'] = life_status
        cases [i + 36] [j + 71] ['c'] = color
        cases [i + 36] [j + 72] ['s'] = life_status
        cases [i + 36] [j + 72] ['c'] = color
        cases [i + 36] [j + 73] ['s'] = life_status
        cases [i + 36] [j + 73] ['c'] = color
        
        cases [i + 37] [j + 72] ['s'] = life_status
        cases [i + 37] [j + 72] ['c'] = color
        cases [i + 37] [j + 73] ['s'] = life_status
        cases [i + 37] [j + 73] ['c'] = color
        
        cases [i + 38] [j + 72] ['s'] = life_status
        cases [i + 38] [j + 72] ['c'] = color
        cases [i + 38] [j + 73] ['s'] = life_status
        cases [i + 38] [j + 73] ['c'] = color
        
        cases [i + 39] [j + 73] ['s'] = life_status
        cases [i + 39] [j + 73] ['c'] = color
        
        cases [i + 40] [j + 73] ['s'] = life_status
        cases [i + 40] [j + 73] ['c'] = color
        
        #FUMEE 
        color = "grey"
        cases [i + 38] [j + 77] ['s'] = life_status
        cases [i + 38] [j + 77] ['c'] = color
        cases [i + 38] [j + 78] ['s'] = life_status
        cases [i + 38] [j + 78] ['c'] = color
        
        cases [i + 39] [j + 75] ['s'] = life_status
        cases [i + 39] [j + 75] ['c'] = color
        cases [i + 39] [j + 76] ['s'] = life_status
        cases [i + 39] [j + 76] ['c'] = color
        cases [i + 39] [j + 77] ['s'] = life_status
        cases [i + 39] [j + 77] ['c'] = color
        cases [i + 39] [j + 78] ['s'] = life_status
        cases [i + 39] [j + 78] ['c'] = color
        cases [i + 39] [j + 79] ['s'] = life_status
        cases [i + 39] [j + 79] ['c'] = color
        
        cases [i + 40] [j + 74] ['s'] = life_status
        cases [i + 40] [j + 74] ['c'] = color
        cases [i + 40] [j + 75] ['s'] = life_status
        cases [i + 40] [j + 75] ['c'] = color
        cases [i + 40] [j + 76] ['s'] = life_status
        cases [i + 40] [j + 76] ['c'] = color
        cases [i + 40] [j + 77] ['s'] = life_status
        cases [i + 40] [j + 77] ['c'] = color
        cases [i + 40] [j + 78] ['s'] = life_status
        cases [i + 40] [j + 78] ['c'] = color
        cases [i + 40] [j + 79] ['s'] = life_status
        cases [i + 40] [j + 79] ['c'] = color
        
        cases [i + 41] [j + 76] ['s'] = life_status
        cases [i + 41] [j + 76] ['c'] = color
        cases [i + 41] [j + 77] ['s'] = life_status
        cases [i + 41] [j + 77] ['c'] = color
        cases [i + 41] [j + 78] ['s'] = life_status
        cases [i + 41] [j + 78] ['c'] = color
        
        # MOTO 
        color = "palegoldenrod"
        cases [i + 41] [j + 73] ['s'] = life_status
        cases [i + 41] [j + 73] ['c'] = color
        
        
        
        cases [i + 31] [j + 62] ['s'] = life_status
        cases [i + 31] [j + 62] ['c'] = color
        cases [i + 31] [j + 63] ['s'] = life_status
        cases [i + 31] [j + 63] ['c'] = color
        cases [i + 31] [j + 64] ['s'] = life_status
        cases [i + 31] [j + 64] ['c'] = color
        cases [i + 31] [j + 65] ['s'] = life_status
        cases [i + 31] [j + 65] ['c'] = color
        cases [i + 31] [j + 66] ['s'] = life_status
        cases [i + 31] [j + 66] ['c'] = color
        cases [i + 31] [j + 67] ['s'] = life_status
        cases [i + 31] [j + 67] ['c'] = color
        cases [i + 31] [j + 68] ['s'] = life_status
        cases [i + 31] [j + 68] ['c'] = color
        cases [i + 31] [j + 69] ['s'] = life_status
        cases [i + 31] [j + 69] ['c'] = color
        
        cases [i + 30] [j + 63] ['s'] = life_status
        cases [i + 30] [j + 63] ['c'] = color
        cases [i + 30] [j + 64] ['s'] = life_status
        cases [i + 30] [j + 64] ['c'] = color
        cases [i + 30] [j + 65] ['s'] = life_status
        cases [i + 30] [j + 65] ['c'] = color
        cases [i + 30] [j + 66] ['s'] = life_status
        cases [i + 30] [j + 66] ['c'] = color
        cases [i + 30] [j + 67] ['s'] = life_status
        cases [i + 30] [j + 67] ['c'] = color
        cases [i + 30] [j + 68] ['s'] = life_status
        cases [i + 30] [j + 68] ['c'] = color
        
        cases [i + 29] [j + 64] ['s'] = life_status
        cases [i + 29] [j + 64] ['c'] = color
        cases [i + 29] [j + 65] ['s'] = life_status
        cases [i + 29] [j + 65] ['c'] = color
        cases [i + 29] [j + 66] ['s'] = life_status
        cases [i + 29] [j + 66] ['c'] = color
        cases [i + 29] [j + 67] ['s'] = life_status
        cases [i + 29] [j + 67] ['c'] = color
        
        
        color = "red"
        cases [i + 41] [j + 56] ['s'] = life_status
        cases [i + 41] [j + 56] ['c'] = color
        cases [i + 41] [j + 57] ['s'] = life_status
        cases [i + 41] [j + 57] ['c'] = color
        cases [i + 41] [j + 58] ['s'] = life_status
        cases [i + 41] [j + 58] ['c'] = color
        cases [i + 41] [j + 59] ['s'] = life_status
        cases [i + 41] [j + 59] ['c'] = color
        cases [i + 41] [j + 60] ['s'] = life_status
        cases [i + 41] [j + 60] ['c'] = color
        cases [i + 41] [j + 61] ['s'] = life_status
        cases [i + 41] [j + 61] ['c'] = color
        cases [i + 41] [j + 62] ['s'] = life_status
        cases [i + 41] [j + 62] ['c'] = color
        cases [i + 41] [j + 63] ['s'] = life_status
        cases [i + 41] [j + 63] ['c'] = color
        cases [i + 41] [j + 64] ['s'] = life_status
        cases [i + 41] [j + 64] ['c'] = color
        cases [i + 41] [j + 65] ['s'] = life_status
        cases [i + 41] [j + 65] ['c'] = color
        cases [i + 41] [j + 66] ['s'] = life_status
        cases [i + 41] [j + 66] ['c'] = color
        cases [i + 41] [j + 67] ['s'] = life_status
        cases [i + 41] [j + 67] ['c'] = color
        cases [i + 41] [j + 68] ['s'] = life_status
        cases [i + 41] [j + 68] ['c'] = color
        cases [i + 41] [j + 69] ['s'] = life_status
        cases [i + 41] [j + 69] ['c'] = color
        cases [i + 41] [j + 70] ['s'] = life_status
        cases [i + 41] [j + 70] ['c'] = color
        cases [i + 41] [j + 71] ['s'] = life_status
        cases [i + 41] [j + 71] ['c'] = color
        cases [i + 41] [j + 72] ['s'] = life_status
        cases [i + 41] [j + 72] ['c'] = color
        
        
        
        cases [i + 40] [j + 53] ['s'] = life_status
        cases [i + 40] [j + 53] ['c'] = color
        cases [i + 40] [j + 54] ['s'] = life_status
        cases [i + 40] [j + 54] ['c'] = color
        cases [i + 40] [j + 55] ['s'] = life_status
        cases [i + 40] [j + 55] ['c'] = color
        cases [i + 40] [j + 56] ['s'] = life_status
        cases [i + 40] [j + 56] ['c'] = color
        cases [i + 40] [j + 57] ['s'] = life_status
        cases [i + 40] [j + 57] ['c'] = color
        cases [i + 40] [j + 58] ['s'] = life_status
        cases [i + 40] [j + 58] ['c'] = color
        cases [i + 40] [j + 59] ['s'] = life_status
        cases [i + 40] [j + 59] ['c'] = color
        cases [i + 40] [j + 60] ['s'] = life_status
        cases [i + 40] [j + 60] ['c'] = color
        cases [i + 40] [j + 61] ['s'] = life_status
        cases [i + 40] [j + 61] ['c'] = color
        cases [i + 40] [j + 62] ['s'] = life_status
        cases [i + 40] [j + 62] ['c'] = color
        cases [i + 40] [j + 63] ['s'] = life_status
        cases [i + 40] [j + 63] ['c'] = color
        cases [i + 40] [j + 64] ['s'] = life_status
        cases [i + 40] [j + 64] ['c'] = color
        cases [i + 40] [j + 65] ['s'] = life_status
        cases [i + 40] [j + 65] ['c'] = color
        cases [i + 40] [j + 66] ['s'] = life_status
        cases [i + 40] [j + 66] ['c'] = color
        cases [i + 40] [j + 67] ['s'] = life_status
        cases [i + 40] [j + 67] ['c'] = color
        cases [i + 40] [j + 68] ['s'] = life_status
        cases [i + 40] [j + 68] ['c'] = color
        cases [i + 40] [j + 69] ['s'] = life_status
        cases [i + 40] [j + 69] ['c'] = color
        cases [i + 40] [j + 70] ['s'] = life_status
        cases [i + 40] [j + 70] ['c'] = color
        cases [i + 40] [j + 71] ['s'] = life_status
        cases [i + 40] [j + 71] ['c'] = color
        cases [i + 40] [j + 72] ['s'] = life_status
        cases [i + 40] [j + 72] ['c'] = color
        
        
        cases [i + 39] [j + 53] ['s'] = life_status
        cases [i + 39] [j + 53] ['c'] = color
        cases [i + 39] [j + 54] ['s'] = life_status
        cases [i + 39] [j + 54] ['c'] = color
        cases [i + 39] [j + 55] ['s'] = life_status
        cases [i + 39] [j + 55] ['c'] = color
        cases [i + 39] [j + 56] ['s'] = life_status
        cases [i + 39] [j + 56] ['c'] = color
        cases [i + 39] [j + 57] ['s'] = life_status
        cases [i + 39] [j + 57] ['c'] = color
        cases [i + 39] [j + 58] ['s'] = life_status
        cases [i + 39] [j + 58] ['c'] = color
        cases [i + 39] [j + 59] ['s'] = life_status
        cases [i + 39] [j + 59] ['c'] = color
        cases [i + 39] [j + 60] ['s'] = life_status
        cases [i + 39] [j + 60] ['c'] = color
        cases [i + 39] [j + 61] ['s'] = life_status
        cases [i + 39] [j + 61] ['c'] = color
        cases [i + 39] [j + 62] ['s'] = life_status
        cases [i + 39] [j + 62] ['c'] = color
        cases [i + 39] [j + 63] ['s'] = life_status
        cases [i + 39] [j + 63] ['c'] = color
        cases [i + 39] [j + 64] ['s'] = life_status
        cases [i + 39] [j + 64] ['c'] = color
        cases [i + 39] [j + 65] ['s'] = life_status
        cases [i + 39] [j + 65] ['c'] = color
        cases [i + 39] [j + 66] ['s'] = life_status
        cases [i + 39] [j + 66] ['c'] = color
        cases [i + 39] [j + 67] ['s'] = life_status
        cases [i + 39] [j + 67] ['c'] = color
        cases [i + 39] [j + 68] ['s'] = life_status
        cases [i + 39] [j + 68] ['c'] = color
        cases [i + 39] [j + 69] ['s'] = life_status
        cases [i + 39] [j + 69] ['c'] = color
        cases [i + 39] [j + 70] ['s'] = life_status
        cases [i + 39] [j + 70] ['c'] = color
        cases [i + 39] [j + 71] ['s'] = life_status
        cases [i + 39] [j + 71] ['c'] = color
        cases [i + 39] [j + 72] ['s'] = life_status
        cases [i + 39] [j + 72] ['c'] = color
        
 
        cases [i + 38] [j + 53] ['s'] = life_status
        cases [i + 38] [j + 53] ['c'] = color
        cases [i + 38] [j + 54] ['s'] = life_status
        cases [i + 38] [j + 54] ['c'] = color
        cases [i + 38] [j + 55] ['s'] = life_status
        cases [i + 38] [j + 55] ['c'] = color
        cases [i + 38] [j + 56] ['s'] = life_status
        cases [i + 38] [j + 56] ['c'] = color
        cases [i + 38] [j + 57] ['s'] = life_status
        cases [i + 38] [j + 57] ['c'] = color
        cases [i + 38] [j + 58] ['s'] = life_status
        cases [i + 38] [j + 58] ['c'] = color
        cases [i + 38] [j + 59] ['s'] = life_status
        cases [i + 38] [j + 59] ['c'] = color
        cases [i + 38] [j + 60] ['s'] = life_status
        cases [i + 38] [j + 60] ['c'] = color
        cases [i + 38] [j + 61] ['s'] = life_status
        cases [i + 38] [j + 61] ['c'] = color
        cases [i + 38] [j + 62] ['s'] = life_status
        cases [i + 38] [j + 62] ['c'] = color
        cases [i + 38] [j + 63] ['s'] = life_status
        cases [i + 38] [j + 63] ['c'] = color
        cases [i + 38] [j + 64] ['s'] = life_status
        cases [i + 38] [j + 64] ['c'] = color
        cases [i + 38] [j + 65] ['s'] = life_status
        cases [i + 38] [j + 65] ['c'] = color
        cases [i + 38] [j + 66] ['s'] = life_status
        cases [i + 38] [j + 66] ['c'] = color
        cases [i + 38] [j + 67] ['s'] = life_status
        cases [i + 38] [j + 67] ['c'] = color
        cases [i + 38] [j + 68] ['s'] = life_status
        cases [i + 38] [j + 68] ['c'] = color
        cases [i + 38] [j + 69] ['s'] = life_status
        cases [i + 38] [j + 69] ['c'] = color
        cases [i + 38] [j + 70] ['s'] = life_status
        cases [i + 38] [j + 70] ['c'] = color
        cases [i + 38] [j + 71] ['s'] = life_status
        cases [i + 38] [j + 71] ['c'] = color
        cases [i + 38] [j + 72] ['s'] = life_status
        cases [i + 38] [j + 72] ['c'] = color
        
        
        
        cases [i + 37] [j + 53] ['s'] = life_status
        cases [i + 37] [j + 53] ['c'] = color
        cases [i + 37] [j + 54] ['s'] = life_status
        cases [i + 37] [j + 54] ['c'] = color
        cases [i + 37] [j + 55] ['s'] = life_status
        cases [i + 37] [j + 55] ['c'] = color
        cases [i + 37] [j + 56] ['s'] = life_status
        cases [i + 37] [j + 56] ['c'] = color
        cases [i + 37] [j + 57] ['s'] = life_status
        cases [i + 37] [j + 57] ['c'] = color
        cases [i + 37] [j + 58] ['s'] = life_status
        cases [i + 37] [j + 58] ['c'] = color
        cases [i + 37] [j + 59] ['s'] = life_status
        cases [i + 37] [j + 59] ['c'] = color
        cases [i + 37] [j + 60] ['s'] = life_status
        cases [i + 37] [j + 60] ['c'] = color
        cases [i + 37] [j + 61] ['s'] = life_status
        cases [i + 37] [j + 61] ['c'] = color
        cases [i + 37] [j + 62] ['s'] = life_status
        cases [i + 37] [j + 62] ['c'] = color
        cases [i + 37] [j + 63] ['s'] = life_status
        cases [i + 37] [j + 63] ['c'] = color
        cases [i + 37] [j + 64] ['s'] = life_status
        cases [i + 37] [j + 64] ['c'] = color
        cases [i + 37] [j + 65] ['s'] = life_status
        cases [i + 37] [j + 65] ['c'] = color
        cases [i + 37] [j + 66] ['s'] = life_status
        cases [i + 37] [j + 66] ['c'] = color
        cases [i + 37] [j + 67] ['s'] = life_status
        cases [i + 37] [j + 67] ['c'] = color
        cases [i + 37] [j + 68] ['s'] = life_status
        cases [i + 37] [j + 68] ['c'] = color
        cases [i + 37] [j + 69] ['s'] = life_status
        cases [i + 37] [j + 69] ['c'] = color
        cases [i + 37] [j + 70] ['s'] = life_status
        cases [i + 37] [j + 70] ['c'] = color
        cases [i + 37] [j + 71] ['s'] = life_status
        cases [i + 37] [j + 71] ['c'] = color
        
        
        cases [i + 36] [j + 53] ['s'] = life_status
        cases [i + 36] [j + 53] ['c'] = color
        cases [i + 36] [j + 54] ['s'] = life_status
        cases [i + 36] [j + 54] ['c'] = color
        cases [i + 36] [j + 55] ['s'] = life_status
        cases [i + 36] [j + 55] ['c'] = color
        cases [i + 36] [j + 56] ['s'] = life_status
        cases [i + 36] [j + 56] ['c'] = color
        cases [i + 36] [j + 57] ['s'] = life_status
        cases [i + 36] [j + 57] ['c'] = color
        cases [i + 36] [j + 58] ['s'] = life_status
        cases [i + 36] [j + 58] ['c'] = color
        cases [i + 36] [j + 59] ['s'] = life_status
        cases [i + 36] [j + 59] ['c'] = color
        cases [i + 36] [j + 60] ['s'] = life_status
        cases [i + 36] [j + 60] ['c'] = color
        cases [i + 36] [j + 61] ['s'] = life_status
        cases [i + 36] [j + 61] ['c'] = color
        cases [i + 36] [j + 62] ['s'] = life_status
        cases [i + 36] [j + 62] ['c'] = color
        cases [i + 36] [j + 63] ['s'] = life_status
        cases [i + 36] [j + 63] ['c'] = color
        cases [i + 36] [j + 64] ['s'] = life_status
        cases [i + 36] [j + 64] ['c'] = color
        cases [i + 36] [j + 65] ['s'] = life_status
        cases [i + 36] [j + 65] ['c'] = color
        cases [i + 36] [j + 66] ['s'] = life_status
        cases [i + 36] [j + 66] ['c'] = color
        cases [i + 36] [j + 67] ['s'] = life_status
        cases [i + 36] [j + 67] ['c'] = color
        cases [i + 36] [j + 68] ['s'] = life_status
        cases [i + 36] [j + 68] ['c'] = color
        cases [i + 36] [j + 71] ['s'] = life_status
        cases [i + 36] [j + 71] ['c'] = color
        
        
        cases [i + 35] [j + 53] ['s'] = life_status
        cases [i + 35] [j + 53] ['c'] = color
        cases [i + 35] [j + 54] ['s'] = life_status
        cases [i + 35] [j + 54] ['c'] = color
        cases [i + 35] [j + 55] ['s'] = life_status
        cases [i + 35] [j + 55] ['c'] = color
        cases [i + 35] [j + 56] ['s'] = life_status
        cases [i + 35] [j + 56] ['c'] = color
        cases [i + 35] [j + 57] ['s'] = life_status
        cases [i + 35] [j + 57] ['c'] = color
        cases [i + 35] [j + 58] ['s'] = life_status
        cases [i + 35] [j + 58] ['c'] = color
        cases [i + 35] [j + 59] ['s'] = life_status
        cases [i + 35] [j + 59] ['c'] = color
        cases [i + 35] [j + 60] ['s'] = life_status
        cases [i + 35] [j + 60] ['c'] = color
        cases [i + 35] [j + 61] ['s'] = life_status
        cases [i + 35] [j + 61] ['c'] = color
        cases [i + 35] [j + 62] ['s'] = life_status
        cases [i + 35] [j + 62] ['c'] = color
        cases [i + 35] [j + 63] ['s'] = life_status
        cases [i + 35] [j + 63] ['c'] = color
        cases [i + 35] [j + 64] ['s'] = life_status
        cases [i + 35] [j + 64] ['c'] = color
        cases [i + 35] [j + 65] ['s'] = life_status
        cases [i + 35] [j + 65] ['c'] = color
        cases [i + 35] [j + 66] ['s'] = life_status
        cases [i + 35] [j + 66] ['c'] = color
        cases [i + 35] [j + 67] ['s'] = life_status
        cases [i + 35] [j + 67] ['c'] = color
        
        cases [i + 34] [j + 53] ['s'] = life_status
        cases [i + 34] [j + 53] ['c'] = color
        cases [i + 34] [j + 54] ['s'] = life_status
        cases [i + 34] [j + 54] ['c'] = color
        cases [i + 34] [j + 55] ['s'] = life_status
        cases [i + 34] [j + 55] ['c'] = color
        cases [i + 34] [j + 56] ['s'] = life_status
        cases [i + 34] [j + 56] ['c'] = color
        cases [i + 34] [j + 57] ['s'] = life_status
        cases [i + 34] [j + 57] ['c'] = color
        cases [i + 34] [j + 58] ['s'] = life_status
        cases [i + 34] [j + 58] ['c'] = color
        cases [i + 34] [j + 59] ['s'] = life_status
        cases [i + 34] [j + 59] ['c'] = color
        cases [i + 34] [j + 60] ['s'] = life_status
        cases [i + 34] [j + 60] ['c'] = color
        cases [i + 34] [j + 61] ['s'] = life_status
        cases [i + 34] [j + 61] ['c'] = color
        cases [i + 34] [j + 62] ['s'] = life_status
        cases [i + 34] [j + 62] ['c'] = color
        cases [i + 34] [j + 63] ['s'] = life_status
        cases [i + 34] [j + 63] ['c'] = color
        cases [i + 34] [j + 64] ['s'] = life_status
        cases [i + 34] [j + 64] ['c'] = color
        cases [i + 34] [j + 65] ['s'] = life_status
        cases [i + 34] [j + 65] ['c'] = color
        cases [i + 34] [j + 66] ['s'] = life_status
        cases [i + 34] [j + 66] ['c'] = color
        cases [i + 34] [j + 67] ['s'] = life_status
        cases [i + 34] [j + 67] ['c'] = color
        cases [i + 34] [j + 68] ['s'] = life_status
        cases [i + 34] [j + 68] ['c'] = color
        cases [i + 34] [j + 69] ['s'] = life_status
        cases [i + 34] [j + 69] ['c'] = color
        
        cases [i + 33] [j + 54] ['s'] = life_status
        cases [i + 33] [j + 54] ['c'] = color
        cases [i + 33] [j + 55] ['s'] = life_status
        cases [i + 33] [j + 55] ['c'] = color
        cases [i + 33] [j + 56] ['s'] = life_status
        cases [i + 33] [j + 56] ['c'] = color
        cases [i + 33] [j + 57] ['s'] = life_status
        cases [i + 33] [j + 57] ['c'] = color
        cases [i + 33] [j + 58] ['s'] = life_status
        cases [i + 33] [j + 58] ['c'] = color
        cases [i + 33] [j + 59] ['s'] = life_status
        cases [i + 33] [j + 59] ['c'] = color
        cases [i + 33] [j + 60] ['s'] = life_status
        cases [i + 33] [j + 60] ['c'] = color
        cases [i + 33] [j + 61] ['s'] = life_status
        cases [i + 33] [j + 61] ['c'] = color
        cases [i + 33] [j + 62] ['s'] = life_status
        cases [i + 33] [j + 62] ['c'] = color
        cases [i + 33] [j + 63] ['s'] = life_status
        cases [i + 33] [j + 63] ['c'] = color
        cases [i + 33] [j + 64] ['s'] = life_status
        cases [i + 33] [j + 64] ['c'] = color
        cases [i + 33] [j + 65] ['s'] = life_status
        cases [i + 33] [j + 65] ['c'] = color
        cases [i + 33] [j + 66] ['s'] = life_status
        cases [i + 33] [j + 66] ['c'] = color
        cases [i + 33] [j + 67] ['s'] = life_status
        cases [i + 33] [j + 67] ['c'] = color
        cases [i + 33] [j + 68] ['s'] = life_status
        cases [i + 33] [j + 68] ['c'] = color
        
        cases [i + 32] [j + 55] ['s'] = life_status
        cases [i + 32] [j + 55] ['c'] = color
        cases [i + 32] [j + 56] ['s'] = life_status
        cases [i + 32] [j + 56] ['c'] = color
        cases [i + 32] [j + 57] ['s'] = life_status
        cases [i + 32] [j + 57] ['c'] = color
        cases [i + 32] [j + 58] ['s'] = life_status
        cases [i + 32] [j + 58] ['c'] = color
        cases [i + 32] [j + 59] ['s'] = life_status
        cases [i + 32] [j + 59] ['c'] = color
        cases [i + 32] [j + 60] ['s'] = life_status
        cases [i + 32] [j + 60] ['c'] = color
        cases [i + 32] [j + 61] ['s'] = life_status
        cases [i + 32] [j + 61] ['c'] = color
        cases [i + 32] [j + 62] ['s'] = life_status
        cases [i + 32] [j + 62] ['c'] = color
        cases [i + 32] [j + 63] ['s'] = life_status
        cases [i + 32] [j + 63] ['c'] = color
        cases [i + 32] [j + 64] ['s'] = life_status
        cases [i + 32] [j + 64] ['c'] = color
        cases [i + 32] [j + 65] ['s'] = life_status
        cases [i + 32] [j + 65] ['c'] = color
        cases [i + 32] [j + 66] ['s'] = life_status
        cases [i + 32] [j + 66] ['c'] = color
        cases [i + 32] [j + 67] ['s'] = life_status
        cases [i + 32] [j + 67] ['c'] = color
        
        
        color = "saddlebrown"
        cases [i + 32] [j + 50] ['s'] = life_status
        cases [i + 32] [j + 50] ['c'] = color
        cases [i + 32] [j + 51] ['s'] = life_status
        cases [i + 32] [j + 51] ['c'] = color
        cases [i + 32] [j + 52] ['s'] = life_status
        cases [i + 32] [j + 52] ['c'] = color
        cases [i + 32] [j + 53] ['s'] = life_status
        cases [i + 32] [j + 53] ['c'] = color
        cases [i + 32] [j + 54] ['s'] = life_status
        cases [i + 32] [j + 54] ['c'] = color
    
        cases [i + 31] [j + 50] ['s'] = life_status
        cases [i + 31] [j + 50] ['c'] = color
        cases [i + 31] [j + 51] ['s'] = life_status
        cases [i + 31] [j + 51] ['c'] = color
        cases [i + 31] [j + 52] ['s'] = life_status
        cases [i + 31] [j + 52] ['c'] = color
        cases [i + 31] [j + 53] ['s'] = life_status
        cases [i + 31] [j + 53] ['c'] = color
        cases [i + 31] [j + 54] ['s'] = life_status
        cases [i + 31] [j + 54] ['c'] = color
        cases [i + 31] [j + 55] ['s'] = life_status
        cases [i + 31] [j + 55] ['c'] = color
        cases [i + 31] [j + 56] ['s'] = life_status
        cases [i + 31] [j + 56] ['c'] = color
        cases [i + 31] [j + 57] ['s'] = life_status
        cases [i + 31] [j + 57] ['c'] = color
        cases [i + 31] [j + 58] ['s'] = life_status
        cases [i + 31] [j + 58] ['c'] = color
        cases [i + 31] [j + 59] ['s'] = life_status
        cases [i + 31] [j + 59] ['c'] = color
        cases [i + 31] [j + 60] ['s'] = life_status
        cases [i + 31] [j + 60] ['c'] = color
        cases [i + 31] [j + 61] ['s'] = life_status
        cases [i + 31] [j + 61] ['c'] = color
    
        cases [i + 30] [j + 51] ['s'] = life_status
        cases [i + 30] [j + 51] ['c'] = color
        cases [i + 30] [j + 52] ['s'] = life_status
        cases [i + 30] [j + 52] ['c'] = color
        cases [i + 30] [j + 53] ['s'] = life_status
        cases [i + 30] [j + 53] ['c'] = color
        cases [i + 30] [j + 54] ['s'] = life_status
        cases [i + 30] [j + 54] ['c'] = color
        cases [i + 30] [j + 55] ['s'] = life_status
        cases [i + 30] [j + 55] ['c'] = color
        cases [i + 30] [j + 56] ['s'] = life_status
        cases [i + 30] [j + 56] ['c'] = color
        cases [i + 30] [j + 57] ['s'] = life_status
        cases [i + 30] [j + 57] ['c'] = color
        cases [i + 30] [j + 58] ['s'] = life_status
        cases [i + 30] [j + 58] ['c'] = color
        cases [i + 30] [j + 59] ['s'] = life_status
        cases [i + 30] [j + 59] ['c'] = color
        cases [i + 30] [j + 60] ['s'] = life_status
        cases [i + 30] [j + 60] ['c'] = color
        cases [i + 30] [j + 61] ['s'] = life_status
        cases [i + 30] [j + 61] ['c'] = color
        cases [i + 30] [j + 62] ['s'] = life_status
        cases [i + 30] [j + 62] ['c'] = color
        
        
        cases [i + 29] [j + 52] ['s'] = life_status
        cases [i + 29] [j + 52] ['c'] = color
        cases [i + 29] [j + 53] ['s'] = life_status
        cases [i + 29] [j + 53] ['c'] = color
        cases [i + 29] [j + 54] ['s'] = life_status
        cases [i + 29] [j + 54] ['c'] = color
        cases [i + 29] [j + 55] ['s'] = life_status
        cases [i + 29] [j + 55] ['c'] = color
        cases [i + 29] [j + 56] ['s'] = life_status
        cases [i + 29] [j + 56] ['c'] = color
        cases [i + 29] [j + 57] ['s'] = life_status
        cases [i + 29] [j + 57] ['c'] = color
        cases [i + 29] [j + 58] ['s'] = life_status
        cases [i + 29] [j + 58] ['c'] = color
        cases [i + 29] [j + 59] ['s'] = life_status
        cases [i + 29] [j + 59] ['c'] = color
        cases [i + 29] [j + 60] ['s'] = life_status
        cases [i + 29] [j + 60] ['c'] = color
        cases [i + 29] [j + 61] ['s'] = life_status
        cases [i + 29] [j + 61] ['c'] = color
        cases [i + 29] [j + 62] ['s'] = life_status
        cases [i + 29] [j + 62] ['c'] = color
        cases [i + 29] [j + 63] ['s'] = life_status
        cases [i + 29] [j + 63] ['c'] = color

        cases [i + 28] [j + 61] ['s'] = life_status
        cases [i + 28] [j + 61] ['c'] = color
        cases [i + 28] [j + 62] ['s'] = life_status
        cases [i + 28] [j + 62] ['c'] = color
        cases [i + 28] [j + 63] ['s'] = life_status
        cases [i + 28] [j + 63] ['c'] = color
        cases [i + 28] [j + 64] ['s'] = life_status
        cases [i + 28] [j + 64] ['c'] = color
        cases [i + 28] [j + 65] ['s'] = life_status
        cases [i + 28] [j + 65] ['c'] = color
        
        cases [i + 27] [j + 63] ['c'] = color
        cases [i + 27] [j + 64] ['s'] = life_status
        cases [i + 27] [j + 64] ['c'] = color
        cases [i + 27] [j + 65] ['s'] = life_status
        cases [i + 27] [j + 65] ['c'] = color
    
        
        color = "grey"
        cases [i + 28] [j + 44] ['s'] = life_status
        cases [i + 28] [j + 44] ['c'] = color
        cases [i + 28] [j + 45] ['s'] = life_status
        cases [i + 28] [j + 45] ['c'] = color
        cases [i + 28] [j + 46] ['s'] = life_status
        cases [i + 28] [j + 46] ['c'] = color
        cases [i + 28] [j + 47] ['s'] = life_status
        cases [i + 28] [j + 47] ['c'] = color
        cases [i + 28] [j + 48] ['s'] = life_status
        cases [i + 28] [j + 48] ['c'] = color
        cases [i + 28] [j + 49] ['s'] = life_status
        cases [i + 28] [j + 49] ['c'] = color
        cases [i + 28] [j + 50] ['s'] = life_status
        cases [i + 28] [j + 50] ['c'] = color
        cases [i + 28] [j + 51] ['s'] = life_status
        cases [i + 28] [j + 51] ['c'] = color
        cases [i + 28] [j + 52] ['s'] = life_status
        cases [i + 28] [j + 52] ['c'] = color
        cases [i + 28] [j + 53] ['s'] = life_status
        cases [i + 28] [j + 53] ['c'] = color
        cases [i + 28] [j + 54] ['s'] = life_status
        cases [i + 28] [j + 54] ['c'] = color
        cases [i + 28] [j + 55] ['s'] = life_status
        cases [i + 28] [j + 55] ['c'] = color
        cases [i + 28] [j + 56] ['s'] = life_status
        cases [i + 28] [j + 56] ['c'] = color
        cases [i + 28] [j + 57] ['s'] = life_status
        cases [i + 28] [j + 57] ['c'] = color
        cases [i + 28] [j + 58] ['s'] = life_status
        cases [i + 28] [j + 58] ['c'] = color
        cases [i + 28] [j + 59] ['s'] = life_status
        cases [i + 28] [j + 59] ['c'] = color
        cases [i + 28] [j + 60] ['s'] = life_status
        cases [i + 28] [j + 60] ['c'] = color
        
        cases [i + 27] [j + 44] ['s'] = life_status
        cases [i + 27] [j + 44] ['c'] = color
        cases [i + 27] [j + 45] ['s'] = life_status
        cases [i + 27] [j + 45] ['c'] = color
        cases [i + 27] [j + 46] ['s'] = life_status
        cases [i + 27] [j + 46] ['c'] = color
        cases [i + 27] [j + 47] ['s'] = life_status
        cases [i + 27] [j + 47] ['c'] = color
        cases [i + 27] [j + 48] ['s'] = life_status
        cases [i + 27] [j + 48] ['c'] = color
        cases [i + 27] [j + 49] ['s'] = life_status
        cases [i + 27] [j + 49] ['c'] = color
        cases [i + 27] [j + 50] ['s'] = life_status
        cases [i + 27] [j + 50] ['c'] = color
        cases [i + 27] [j + 51] ['s'] = life_status
        cases [i + 27] [j + 51] ['c'] = color
        cases [i + 27] [j + 52] ['s'] = life_status
        cases [i + 27] [j + 52] ['c'] = color
        cases [i + 27] [j + 53] ['s'] = life_status
        cases [i + 27] [j + 53] ['c'] = color
        cases [i + 27] [j + 54] ['s'] = life_status
        cases [i + 27] [j + 54] ['c'] = color
        cases [i + 27] [j + 55] ['s'] = life_status
        cases [i + 27] [j + 55] ['c'] = color
        cases [i + 27] [j + 56] ['s'] = life_status
        cases [i + 27] [j + 56] ['c'] = color
        cases [i + 27] [j + 57] ['s'] = life_status
        cases [i + 27] [j + 57] ['c'] = color
        cases [i + 27] [j + 58] ['s'] = life_status
        cases [i + 27] [j + 58] ['c'] = color
        cases [i + 27] [j + 59] ['s'] = life_status
        cases [i + 27] [j + 59] ['c'] = color
        cases [i + 27] [j + 60] ['s'] = life_status
        cases [i + 27] [j + 60] ['c'] = color
        cases [i + 27] [j + 61] ['s'] = life_status
        cases [i + 27] [j + 61] ['c'] = color
        
        cases [i + 26] [j + 45] ['s'] = life_status
        cases [i + 26] [j + 45] ['c'] = color
        cases [i + 26] [j + 46] ['s'] = life_status
        cases [i + 26] [j + 46] ['c'] = color
        cases [i + 26] [j + 47] ['s'] = life_status
        cases [i + 26] [j + 47] ['c'] = color
        cases [i + 26] [j + 48] ['s'] = life_status
        cases [i + 26] [j + 48] ['c'] = color
        cases [i + 26] [j + 49] ['s'] = life_status
        cases [i + 26] [j + 49] ['c'] = color
        cases [i + 26] [j + 50] ['s'] = life_status
        cases [i + 26] [j + 50] ['c'] = color
        cases [i + 26] [j + 51] ['s'] = life_status
        cases [i + 26] [j + 51] ['c'] = color
        cases [i + 26] [j + 52] ['s'] = life_status
        cases [i + 26] [j + 52] ['c'] = color
        cases [i + 26] [j + 53] ['s'] = life_status
        cases [i + 26] [j + 53] ['c'] = color
        cases [i + 26] [j + 54] ['s'] = life_status
        cases [i + 26] [j + 54] ['c'] = color
        cases [i + 26] [j + 55] ['s'] = life_status
        cases [i + 26] [j + 55] ['c'] = color
        cases [i + 26] [j + 56] ['s'] = life_status
        cases [i + 26] [j + 56] ['c'] = color
        cases [i + 26] [j + 57] ['s'] = life_status
        cases [i + 26] [j + 57] ['c'] = color
        cases [i + 26] [j + 58] ['s'] = life_status
        cases [i + 26] [j + 58] ['c'] = color
        cases [i + 26] [j + 59] ['s'] = life_status
        cases [i + 26] [j + 59] ['c'] = color
        cases [i + 26] [j + 60] ['s'] = life_status
        cases [i + 26] [j + 60] ['c'] = color
        cases [i + 26] [j + 61] ['s'] = life_status
        cases [i + 26] [j + 61] ['c'] = color
        
        
        cases [i + 25] [j + 46] ['s'] = life_status
        cases [i + 25] [j + 46] ['c'] = color
        cases [i + 25] [j + 47] ['s'] = life_status
        cases [i + 25] [j + 47] ['c'] = color
        cases [i + 25] [j + 48] ['s'] = life_status
        cases [i + 25] [j + 48] ['c'] = color
        cases [i + 25] [j + 49] ['s'] = life_status
        cases [i + 25] [j + 49] ['c'] = color
        cases [i + 25] [j + 50] ['s'] = life_status
        cases [i + 25] [j + 50] ['c'] = color
        cases [i + 25] [j + 51] ['s'] = life_status
        cases [i + 25] [j + 51] ['c'] = color
        cases [i + 25] [j + 52] ['s'] = life_status
        cases [i + 25] [j + 52] ['c'] = color
        cases [i + 25] [j + 53] ['s'] = life_status
        cases [i + 25] [j + 53] ['c'] = color
        cases [i + 25] [j + 54] ['s'] = life_status
        cases [i + 25] [j + 54] ['c'] = color
        cases [i + 25] [j + 55] ['s'] = life_status
        cases [i + 25] [j + 55] ['c'] = color
        cases [i + 25] [j + 56] ['s'] = life_status
        cases [i + 25] [j + 56] ['c'] = color
        
        
        
        cases [i + 29] [j + 44] ['s'] = life_status
        cases [i + 29] [j + 44] ['c'] = color
        cases [i + 29] [j + 45] ['s'] = life_status
        cases [i + 29] [j + 45] ['c'] = color
        cases [i + 29] [j + 46] ['s'] = life_status
        cases [i + 29] [j + 46] ['c'] = color
        cases [i + 29] [j + 47] ['s'] = life_status
        cases [i + 29] [j + 47] ['c'] = color
        
        cases [i + 30] [j + 44] ['s'] = life_status
        cases [i + 30] [j + 44] ['c'] = color
        cases [i + 30] [j + 45] ['s'] = life_status
        cases [i + 30] [j + 45] ['c'] = color
        cases [i + 30] [j + 46] ['s'] = life_status
        cases [i + 30] [j + 46] ['c'] = color
        cases [i + 30] [j + 47] ['s'] = life_status
        cases [i + 30] [j + 47] ['c'] = color
        
        cases [i + 31] [j + 44] ['s'] = life_status
        cases [i + 31] [j + 44] ['c'] = color
        cases [i + 31] [j + 45] ['s'] = life_status
        cases [i + 31] [j + 45] ['c'] = color
        cases [i + 31] [j + 46] ['s'] = life_status
        cases [i + 31] [j + 46] ['c'] = color
        cases [i + 31] [j + 47] ['s'] = life_status
        cases [i + 31] [j + 47] ['c'] = color
        
        
        cases [i + 32] [j + 44] ['s'] = life_status
        cases [i + 32] [j + 44] ['c'] = color
        cases [i + 32] [j + 45] ['s'] = life_status
        cases [i + 32] [j + 45] ['c'] = color
        cases [i + 32] [j + 46] ['s'] = life_status
        cases [i + 32] [j + 46] ['c'] = color
        cases [i + 32] [j + 47] ['s'] = life_status
        cases [i + 32] [j + 47] ['c'] = color
        
        
        cases [i + 33] [j + 44] ['s'] = life_status
        cases [i + 33] [j + 44] ['c'] = color
        cases [i + 33] [j + 45] ['s'] = life_status
        cases [i + 33] [j + 45] ['c'] = color
        cases [i + 33] [j + 46] ['s'] = life_status
        cases [i + 33] [j + 46] ['c'] = color
        cases [i + 33] [j + 47] ['s'] = life_status
        cases [i + 33] [j + 47] ['c'] = color
        
        cases [i + 33] [j + 44] ['s'] = life_status
        cases [i + 34] [j + 44] ['c'] = color
        cases [i + 34] [j + 45] ['s'] = life_status
        cases [i + 34] [j + 45] ['c'] = color
        cases [i + 34] [j + 46] ['s'] = life_status
        cases [i + 34] [j + 46] ['c'] = color
        cases [i + 34] [j + 47] ['s'] = life_status
        cases [i + 34] [j + 47] ['c'] = color
        
        
        cases [i + 34] [j + 44] ['s'] = life_status
        cases [i + 35] [j + 44] ['c'] = color
        cases [i + 35] [j + 45] ['s'] = life_status
        cases [i + 35] [j + 45] ['c'] = color
        cases [i + 35] [j + 46] ['s'] = life_status
        cases [i + 35] [j + 46] ['c'] = color
        cases [i + 35] [j + 47] ['s'] = life_status
        cases [i + 35] [j + 47] ['c'] = color
        
        cases [i + 35] [j + 44] ['s'] = life_status
        cases [i + 36] [j + 44] ['c'] = color
        cases [i + 36] [j + 45] ['s'] = life_status
        cases [i + 36] [j + 45] ['c'] = color
        cases [i + 36] [j + 46] ['s'] = life_status
        cases [i + 36] [j + 46] ['c'] = color
        cases [i + 36] [j + 47] ['s'] = life_status
        cases [i + 36] [j + 47] ['c'] = color
        
        
        
        color = "red"
        cases [i + 25] [j + 57] ['s'] = life_status
        cases [i + 25] [j + 57] ['c'] = color
        cases [i + 25] [j + 58] ['s'] = life_status
        cases [i + 25] [j + 58] ['c'] = color
        cases [i + 25] [j + 59] ['s'] = life_status
        cases [i + 25] [j + 59] ['c'] = color
        cases [i + 25] [j + 60] ['s'] = life_status
        cases [i + 25] [j + 60] ['c'] = color
        cases [i + 25] [j + 61] ['s'] = life_status
        cases [i + 25] [j + 61] ['c'] = color
        
        cases [i + 23] [j + 55] ['s'] = life_status
        cases [i + 24] [j + 55] ['c'] = color
        cases [i + 24] [j + 56] ['s'] = life_status
        cases [i + 24] [j + 56] ['c'] = color
        cases [i + 24] [j + 57] ['s'] = life_status
        cases [i + 24] [j + 57] ['c'] = color
        cases [i + 24] [j + 58] ['s'] = life_status
        cases [i + 24] [j + 58] ['c'] = color
        cases [i + 24] [j + 59] ['s'] = life_status
        cases [i + 24] [j + 59] ['c'] = color
        cases [i + 24] [j + 60] ['s'] = life_status
        cases [i + 24] [j + 60] ['c'] = color
        cases [i + 24] [j + 61] ['s'] = life_status
        cases [i + 24] [j + 61] ['c'] = color

        cases [i + 23] [j + 55] ['s'] = life_status
        cases [i + 23] [j + 55] ['c'] = color
        cases [i + 23] [j + 56] ['s'] = life_status
        cases [i + 23] [j + 56] ['c'] = color
        cases [i + 23] [j + 57] ['s'] = life_status
        cases [i + 23] [j + 57] ['c'] = color
        cases [i + 23] [j + 58] ['s'] = life_status
        cases [i + 23] [j + 58] ['c'] = color
        cases [i + 23] [j + 59] ['s'] = life_status
        cases [i + 23] [j + 59] ['c'] = color
        cases [i + 23] [j + 60] ['s'] = life_status
        cases [i + 23] [j + 60] ['c'] = color
        cases [i + 23] [j + 61] ['s'] = life_status
        cases [i + 23] [j + 61] ['c'] = color
    
        cases [i + 22] [j + 55] ['s'] = life_status
        cases [i + 22] [j + 55] ['c'] = color
        cases [i + 22] [j + 56] ['s'] = life_status
        cases [i + 22] [j + 56] ['c'] = color
        cases [i + 22] [j + 57] ['s'] = life_status
        cases [i + 22] [j + 57] ['c'] = color
        cases [i + 22] [j + 58] ['s'] = life_status
        cases [i + 22] [j + 58] ['c'] = color
        cases [i + 22] [j + 59] ['s'] = life_status
        cases [i + 22] [j + 59] ['c'] = color
        cases [i + 22] [j + 60] ['s'] = life_status
        cases [i + 22] [j + 60] ['c'] = color
        cases [i + 22] [j + 61] ['s'] = life_status
        cases [i + 22] [j + 61] ['c'] = color
        
        cases [i + 21] [j + 55] ['s'] = life_status
        cases [i + 21] [j + 55] ['c'] = color
        cases [i + 21] [j + 56] ['s'] = life_status
        cases [i + 21] [j + 56] ['c'] = color
        cases [i + 21] [j + 57] ['s'] = life_status
        cases [i + 21] [j + 57] ['c'] = color
        cases [i + 21] [j + 58] ['s'] = life_status
        cases [i + 21] [j + 58] ['c'] = color
        cases [i + 21] [j + 59] ['s'] = life_status
        cases [i + 21] [j + 59] ['c'] = color
        cases [i + 21] [j + 60] ['s'] = life_status
        cases [i + 21] [j + 60] ['c'] = color
        cases [i + 21] [j + 61] ['s'] = life_status
        cases [i + 21] [j + 61] ['c'] = color

        cases [i + 20] [j + 55] ['s'] = life_status
        cases [i + 20] [j + 55] ['c'] = color
        cases [i + 20] [j + 56] ['s'] = life_status
        cases [i + 20] [j + 56] ['c'] = color
        cases [i + 20] [j + 57] ['s'] = life_status
        cases [i + 20] [j + 57] ['c'] = color
        cases [i + 20] [j + 58] ['s'] = life_status
        cases [i + 20] [j + 58] ['c'] = color
        cases [i + 20] [j + 59] ['s'] = life_status
        cases [i + 20] [j + 59] ['c'] = color
        cases [i + 20] [j + 60] ['s'] = life_status
        cases [i + 20] [j + 60] ['c'] = color
        cases [i + 20] [j + 61] ['s'] = life_status
        cases [i + 20] [j + 61] ['c'] = color
        
        cases [i + 19] [j + 56] ['s'] = life_status
        cases [i + 19] [j + 56] ['c'] = color
        cases [i + 19] [j + 57] ['s'] = life_status
        cases [i + 19] [j + 57] ['c'] = color
        cases [i + 19] [j + 58] ['s'] = life_status
        cases [i + 19] [j + 58] ['c'] = color
        cases [i + 19] [j + 59] ['s'] = life_status
        cases [i + 19] [j + 59] ['c'] = color
        cases [i + 19] [j + 60] ['s'] = life_status
        cases [i + 19] [j + 60] ['c'] = color
        cases [i + 19] [j + 61] ['s'] = life_status
        cases [i + 19] [j + 61] ['c'] = color
        
        cases [i + 18] [j + 57] ['s'] = life_status
        cases [i + 18] [j + 57] ['c'] = color
        cases [i + 18] [j + 58] ['s'] = life_status
        cases [i + 18] [j + 58] ['c'] = color
        cases [i + 18] [j + 59] ['s'] = life_status
        cases [i + 18] [j + 59] ['c'] = color
        cases [i + 18] [j + 60] ['s'] = life_status
        cases [i + 18] [j + 60] ['c'] = color
        cases [i + 18] [j + 61] ['s'] = life_status
        cases [i + 18] [j + 61] ['c'] = color
        
        cases [i + 17] [j + 57] ['s'] = life_status
        cases [i + 17] [j + 57] ['c'] = color
        cases [i + 17] [j + 58] ['s'] = life_status
        cases [i + 17] [j + 58] ['c'] = color
        cases [i + 17] [j + 59] ['s'] = life_status
        cases [i + 17] [j + 59] ['c'] = color
        cases [i + 17] [j + 60] ['s'] = life_status
        cases [i + 17] [j + 60] ['c'] = color
        cases [i + 17] [j + 61] ['s'] = life_status
        cases [i + 17] [j + 61] ['c'] = color
        
        cases [i + 16] [j + 58] ['s'] = life_status
        cases [i + 16] [j + 58] ['c'] = color
        cases [i + 16] [j + 59] ['s'] = life_status
        cases [i + 16] [j + 59] ['c'] = color
        cases [i + 16] [j + 60] ['s'] = life_status
        cases [i + 16] [j + 60] ['c'] = color
        cases [i + 16] [j + 61] ['s'] = life_status
        cases [i + 16] [j + 61] ['c'] = color
        
        cases [i + 15] [j + 58] ['s'] = life_status
        cases [i + 15] [j + 58] ['c'] = color
        cases [i + 15] [j + 59] ['s'] = life_status
        cases [i + 15] [j + 59] ['c'] = color
        cases [i + 15] [j + 60] ['s'] = life_status
        cases [i + 15] [j + 60] ['c'] = color
        
        cases [i + 14] [j + 58] ['s'] = life_status
        cases [i + 14] [j + 58] ['c'] = color
        cases [i + 14] [j + 59] ['s'] = life_status
        cases [i + 14] [j + 59] ['c'] = color
        cases [i + 14] [j + 60] ['s'] = life_status
        cases [i + 14] [j + 60] ['c'] = color
        
        cases [i + 13] [j + 57] ['s'] = life_status
        cases [i + 13] [j + 57] ['c'] = color
        cases [i + 13] [j + 58] ['s'] = life_status
        cases [i + 13] [j + 58] ['c'] = color
        cases [i + 13] [j + 59] ['s'] = life_status
        cases [i + 13] [j + 59] ['c'] = color
        
        cases [i + 12] [j + 54] ['s'] = life_status
        cases [i + 12] [j + 54] ['c'] = color
        cases [i + 12] [j + 55] ['s'] = life_status
        cases [i + 12] [j + 55] ['c'] = color
        cases [i + 12] [j + 56] ['s'] = life_status
        cases [i + 12] [j + 56] ['c'] = color
        cases [i + 12] [j + 57] ['s'] = life_status
        cases [i + 12] [j + 57] ['c'] = color
        cases [i + 12] [j + 58] ['s'] = life_status
        cases [i + 12] [j + 58] ['c'] = color
        
        
        color = "peru"
        cases [i + 13] [j + 54] ['s'] = life_status
        cases [i + 13] [j + 54] ['c'] = color
        cases [i + 13] [j + 55] ['s'] = life_status
        cases [i + 13] [j + 55] ['c'] = color
        cases [i + 13] [j + 56] ['s'] = life_status
        cases [i + 13] [j + 56] ['c'] = color
        
        cases [i + 14] [j + 53] ['s'] = life_status
        cases [i + 14] [j + 53] ['c'] = color
        cases [i + 14] [j + 54] ['s'] = life_status
        cases [i + 14] [j + 54] ['c'] = color
        cases [i + 14] [j + 55] ['s'] = life_status
        cases [i + 14] [j + 55] ['c'] = color
        cases [i + 14] [j + 56] ['s'] = life_status
        cases [i + 14] [j + 56] ['c'] = color
        cases [i + 14] [j + 57] ['s'] = life_status
        cases [i + 14] [j + 57] ['c'] = color
        
        cases [i + 15] [j + 53] ['s'] = life_status
        cases [i + 15] [j + 53] ['c'] = color
        cases [i + 15] [j + 54] ['s'] = life_status
        cases [i + 15] [j + 54] ['c'] = color
        cases [i + 15] [j + 55] ['s'] = life_status
        cases [i + 15] [j + 55] ['c'] = color
        cases [i + 15] [j + 56] ['s'] = life_status
        cases [i + 15] [j + 56] ['c'] = color
        cases [i + 15] [j + 57] ['s'] = life_status
        cases [i + 15] [j + 57] ['c'] = color
        
        cases [i + 16] [j + 52] ['s'] = life_status
        cases [i + 16] [j + 52] ['c'] = color
        cases [i + 16] [j + 53] ['s'] = life_status
        cases [i + 16] [j + 53] ['c'] = color
        cases [i + 16] [j + 54] ['s'] = life_status
        cases [i + 16] [j + 54] ['c'] = color
        cases [i + 16] [j + 55] ['s'] = life_status
        cases [i + 16] [j + 55] ['c'] = color
        cases [i + 16] [j + 56] ['s'] = life_status
        cases [i + 16] [j + 56] ['c'] = color
        cases [i + 16] [j + 57] ['s'] = life_status
        cases [i + 16] [j + 57] ['c'] = color
        
        cases [i + 17] [j + 52] ['s'] = life_status
        cases [i + 17] [j + 52] ['c'] = color
        cases [i + 17] [j + 53] ['s'] = life_status
        cases [i + 17] [j + 53] ['c'] = color
        cases [i + 17] [j + 54] ['s'] = life_status
        cases [i + 17] [j + 54] ['c'] = color
        cases [i + 17] [j + 55] ['s'] = life_status
        cases [i + 17] [j + 55] ['c'] = color
        cases [i + 17] [j + 56] ['s'] = life_status
        cases [i + 17] [j + 56] ['c'] = color
        
        cases [i + 18] [j + 50] ['s'] = life_status
        cases [i + 18] [j + 50] ['c'] = color
        cases [i + 18] [j + 51] ['s'] = life_status
        cases [i + 18] [j + 51] ['c'] = color
        cases [i + 18] [j + 52] ['s'] = life_status
        cases [i + 18] [j + 52] ['c'] = color
        cases [i + 18] [j + 53] ['s'] = life_status
        cases [i + 18] [j + 53] ['c'] = color
        cases [i + 18] [j + 54] ['s'] = life_status
        cases [i + 18] [j + 54] ['c'] = color
        cases [i + 18] [j + 55] ['s'] = life_status
        cases [i + 18] [j + 55] ['c'] = color
        cases [i + 18] [j + 56] ['s'] = life_status
        cases [i + 18] [j + 56] ['c'] = color
        
        cases [i + 19] [j + 49] ['s'] = life_status
        cases [i + 19] [j + 49] ['c'] = color
        cases [i + 19] [j + 50] ['s'] = life_status
        cases [i + 19] [j + 50] ['c'] = color
        cases [i + 19] [j + 51] ['s'] = life_status
        cases [i + 19] [j + 51] ['c'] = color
        cases [i + 19] [j + 52] ['s'] = life_status
        cases [i + 19] [j + 52] ['c'] = color
        cases [i + 19] [j + 53] ['s'] = life_status
        cases [i + 19] [j + 53] ['c'] = color
        cases [i + 19] [j + 54] ['s'] = life_status
        cases [i + 19] [j + 54] ['c'] = color
        cases [i + 19] [j + 55] ['s'] = life_status
        cases [i + 19] [j + 55] ['c'] = color
        
        cases [i + 20] [j + 49] ['s'] = life_status
        cases [i + 20] [j + 49] ['c'] = color
        cases [i + 20] [j + 50] ['s'] = life_status
        cases [i + 20] [j + 50] ['c'] = color
        cases [i + 20] [j + 51] ['s'] = life_status
        cases [i + 20] [j + 51] ['c'] = color
        cases [i + 20] [j + 52] ['s'] = life_status
        cases [i + 20] [j + 52] ['c'] = color
        cases [i + 20] [j + 53] ['s'] = life_status
        cases [i + 20] [j + 53] ['c'] = color
        cases [i + 20] [j + 54] ['s'] = life_status
        cases [i + 20] [j + 54] ['c'] = color
        
        cases [i + 21] [j + 49] ['s'] = life_status
        cases [i + 21] [j + 49] ['c'] = color
        cases [i + 21] [j + 50] ['s'] = life_status
        cases [i + 21] [j + 50] ['c'] = color
        cases [i + 21] [j + 51] ['s'] = life_status
        cases [i + 21] [j + 51] ['c'] = color
        cases [i + 21] [j + 52] ['s'] = life_status
        cases [i + 21] [j + 52] ['c'] = color
        cases [i + 21] [j + 53] ['s'] = life_status
        cases [i + 21] [j + 53] ['c'] = color
        
        cases [i + 22] [j + 49] ['s'] = life_status
        cases [i + 22] [j + 49] ['c'] = color
        cases [i + 22] [j + 50] ['s'] = life_status
        cases [i + 22] [j + 50] ['c'] = color
        cases [i + 22] [j + 51] ['s'] = life_status
        cases [i + 22] [j + 51] ['c'] = color
        
        color = "gold"
        cases [i + 20] [j + 47] ['s'] = life_status
        cases [i + 20] [j + 47] ['c'] = color
        cases [i + 20] [j + 48] ['s'] = life_status
        cases [i + 20] [j + 48] ['c'] = color
        
        cases [i + 21] [j + 43] ['s'] = life_status
        cases [i + 21] [j + 43] ['c'] = color
        cases [i + 21] [j + 44] ['s'] = life_status
        cases [i + 21] [j + 44] ['c'] = color
        cases [i + 21] [j + 45] ['s'] = life_status
        cases [i + 21] [j + 45] ['c'] = color
        cases [i + 21] [j + 46] ['s'] = life_status
        cases [i + 21] [j + 46] ['c'] = color
        cases [i + 21] [j + 47] ['s'] = life_status
        cases [i + 21] [j + 47] ['c'] = color
        cases [i + 21] [j + 48] ['s'] = life_status
        cases [i + 21] [j + 48] ['c'] = color
        
        cases [i + 22] [j + 43] ['s'] = life_status
        cases [i + 22] [j + 43] ['c'] = color
        cases [i + 22] [j + 46] ['s'] = life_status
        cases [i + 22] [j + 46] ['c'] = color
        cases [i + 22] [j + 47] ['s'] = life_status
        cases [i + 22] [j + 47] ['c'] = color
        
        cases [i + 23] [j + 43] ['s'] = life_status
        cases [i + 23] [j + 43] ['c'] = color
        
        cases [i + 37] [j + 45] ['s'] = life_status
        cases [i + 37] [j + 45] ['c'] = color
        cases [i + 37] [j + 46] ['s'] = life_status
        cases [i + 37] [j + 46] ['c'] = color
        cases [i + 38] [j + 45] ['s'] = life_status
        cases [i + 38] [j + 45] ['c'] = color
        cases [i + 38] [j + 46] ['s'] = life_status
        cases [i + 38] [j + 46] ['c'] = color
        
        color = "red"
        cases [i + 35] [j + 35] ['s'] = life_status
        cases [i + 35] [j + 35] ['c'] = color
        cases [i + 35] [j + 36] ['s'] = life_status
        cases [i + 35] [j + 36] ['c'] = color
        cases [i + 35] [j + 37] ['s'] = life_status
        cases [i + 35] [j + 37] ['c'] = color
        
        cases [i + 34] [j + 34] ['s'] = life_status
        cases [i + 34] [j + 34] ['c'] = color
        cases [i + 34] [j + 35] ['s'] = life_status
        cases [i + 34] [j + 35] ['c'] = color
        cases [i + 34] [j + 36] ['s'] = life_status
        cases [i + 34] [j + 36] ['c'] = color
        cases [i + 34] [j + 37] ['s'] = life_status
        cases [i + 34] [j + 37] ['c'] = color
        
        cases [i + 33] [j + 34] ['s'] = life_status
        cases [i + 33] [j + 34] ['c'] = color
        cases [i + 33] [j + 35] ['s'] = life_status
        cases [i + 33] [j + 35] ['c'] = color
        cases [i + 33] [j + 36] ['s'] = life_status
        cases [i + 33] [j + 36] ['c'] = color
        cases [i + 33] [j + 37] ['s'] = life_status
        cases [i + 33] [j + 37] ['c'] = color
        cases [i + 33] [j + 38] ['s'] = life_status
        cases [i + 33] [j + 38] ['c'] = color
        
        cases [i + 32] [j + 35] ['s'] = life_status
        cases [i + 32] [j + 35] ['c'] = color
        cases [i + 32] [j + 36] ['s'] = life_status
        cases [i + 32] [j + 36] ['c'] = color
        cases [i + 32] [j + 37] ['s'] = life_status
        cases [i + 32] [j + 37] ['c'] = color
        cases [i + 32] [j + 38] ['s'] = life_status
        cases [i + 32] [j + 38] ['c'] = color
        
        cases [i + 31] [j + 35] ['s'] = life_status
        cases [i + 31] [j + 35] ['c'] = color
        cases [i + 31] [j + 36] ['s'] = life_status
        cases [i + 31] [j + 36] ['c'] = color
        cases [i + 31] [j + 37] ['s'] = life_status
        cases [i + 31] [j + 37] ['c'] = color
        cases [i + 31] [j + 38] ['s'] = life_status
        cases [i + 31] [j + 38] ['c'] = color
        
        cases [i + 30] [j + 35] ['s'] = life_status
        cases [i + 30] [j + 35] ['c'] = color
        cases [i + 30] [j + 36] ['s'] = life_status
        cases [i + 30] [j + 36] ['c'] = color
        cases [i + 30] [j + 37] ['s'] = life_status
        cases [i + 30] [j + 37] ['c'] = color
        cases [i + 30] [j + 38] ['s'] = life_status
        cases [i + 30] [j + 38] ['c'] = color
        
        cases [i + 29] [j + 35] ['s'] = life_status
        cases [i + 29] [j + 35] ['c'] = color
        cases [i + 29] [j + 36] ['s'] = life_status
        cases [i + 29] [j + 36] ['c'] = color
        cases [i + 29] [j + 37] ['s'] = life_status
        cases [i + 29] [j + 37] ['c'] = color
        cases [i + 29] [j + 38] ['s'] = life_status
        cases [i + 29] [j + 38] ['c'] = color
        
        cases [i + 28] [j + 36] ['s'] = life_status
        cases [i + 28] [j + 36] ['c'] = color
        cases [i + 28] [j + 37] ['s'] = life_status
        cases [i + 28] [j + 37] ['c'] = color
        cases [i + 28] [j + 38] ['s'] = life_status
        cases [i + 28] [j + 38] ['c'] = color
        
        cases [i + 27] [j + 38] ['s'] = life_status
        cases [i + 27] [j + 38] ['c'] = color
        cases [i + 27] [j + 39] ['s'] = life_status
        cases [i + 27] [j + 39] ['c'] = color
        
        cases [i + 26] [j + 38] ['s'] = life_status
        cases [i + 26] [j + 38] ['c'] = color
        cases [i + 26] [j + 39] ['s'] = life_status
        cases [i + 26] [j + 39] ['c'] = color
        
        cases [i + 25] [j + 37] ['s'] = life_status
        cases [i + 25] [j + 37] ['c'] = color
        cases [i + 25] [j + 38] ['s'] = life_status
        cases [i + 25] [j + 38] ['c'] = color
        cases [i + 25] [j + 39] ['s'] = life_status
        cases [i + 25] [j + 39] ['c'] = color
        
        cases [i + 24] [j + 38] ['s'] = life_status
        cases [i + 24] [j + 38] ['c'] = color
        cases [i + 24] [j + 39] ['s'] = life_status
        cases [i + 24] [j + 39] ['c'] = color
        cases [i + 24] [j + 40] ['s'] = life_status
        cases [i + 24] [j + 40] ['c'] = color
        cases [i + 24] [j + 41] ['s'] = life_status
        cases [i + 24] [j + 41] ['c'] = color
        cases [i + 24] [j + 42] ['s'] = life_status
        cases [i + 24] [j + 42] ['c'] = color
        cases [i + 24] [j + 43] ['s'] = life_status
        cases [i + 24] [j + 43] ['c'] = color
        
        cases [i + 23] [j + 39] ['s'] = life_status
        cases [i + 23] [j + 39] ['c'] = color
        cases [i + 23] [j + 40] ['s'] = life_status
        cases [i + 23] [j + 40] ['c'] = color
        cases [i + 23] [j + 41] ['s'] = life_status
        cases [i + 23] [j + 41] ['c'] = color
        cases [i + 23] [j + 42] ['s'] = life_status
        cases [i + 23] [j + 42] ['c'] = color
        
        color = "grey"
        cases [i + 27] [j + 37] ['s'] = life_status
        cases [i + 27] [j + 37] ['c'] = color
        
        cases [i + 26] [j + 35] ['s'] = life_status
        cases [i + 26] [j + 35] ['c'] = color
        cases [i + 26] [j + 37] ['s'] = life_status
        cases [i + 26] [j + 37] ['c'] = color
        
        
        cases [i + 25] [j + 35] ['s'] = life_status
        cases [i + 25] [j + 35] ['c'] = color
        cases [i + 25] [j + 36] ['s'] = life_status
        cases [i + 25] [j + 36] ['c'] = color
    
        cases [i + 24] [j + 35] ['s'] = life_status
        cases [i + 24] [j + 35] ['c'] = color
        cases [i + 24] [j + 36] ['s'] = life_status
        cases [i + 24] [j + 36] ['c'] = color
        cases [i + 24] [j + 37] ['s'] = life_status
        cases [i + 24] [j + 37] ['c'] = color
        
        cases [i + 23] [j + 35] ['s'] = life_status
        cases [i + 23] [j + 35] ['c'] = color
        cases [i + 23] [j + 36] ['s'] = life_status
        cases [i + 23] [j + 36] ['c'] = color
        cases [i + 23] [j + 37] ['s'] = life_status
        cases [i + 23] [j + 37] ['c'] = color
        cases [i + 23] [j + 38] ['s'] = life_status
        cases [i + 23] [j + 38] ['c'] = color
        
        cases [i + 22] [j + 39] ['s'] = life_status
        cases [i + 22] [j + 39] ['c'] = color
        
        cases [i + 22] [j + 41] ['s'] = life_status
        cases [i + 22] [j + 41] ['c'] = color
        cases [i + 21] [j + 41] ['s'] = life_status
        cases [i + 21] [j + 41] ['c'] = color
        cases [i + 20] [j + 41] ['s'] = life_status
        cases [i + 20] [j + 41] ['c'] = color
        cases [i + 19] [j + 41] ['s'] = life_status
        cases [i + 19] [j + 41] ['c'] = color
        cases [i + 19] [j + 42] ['s'] = life_status
        cases [i + 19] [j + 42] ['c'] = color
        cases [i + 18] [j + 42] ['s'] = life_status
        cases [i + 18] [j + 42] ['c'] = color
        cases [i + 17] [j + 42] ['s'] = life_status
        cases [i + 17] [j + 42] ['c'] = color
        
        
        color = "red"
        
        cases [i + 39] [j + 43] ['s'] = life_status
        cases [i + 39] [j + 43] ['c'] = color
        cases [i + 39] [j + 44] ['s'] = life_status
        cases [i + 39] [j + 44] ['c'] = color
        cases [i + 39] [j + 45] ['s'] = life_status
        cases [i + 39] [j + 45] ['c'] = color
        cases [i + 39] [j + 46] ['s'] = life_status
        cases [i + 39] [j + 46] ['c'] = color
        
        
        cases [i + 40] [j + 41] ['s'] = life_status
        cases [i + 40] [j + 41] ['c'] = color
        cases [i + 40] [j + 42] ['s'] = life_status
        cases [i + 40] [j + 42] ['c'] = color
        cases [i + 40] [j + 43] ['s'] = life_status
        cases [i + 40] [j + 43] ['c'] = color
        cases [i + 40] [j + 44] ['s'] = life_status
        cases [i + 40] [j + 44] ['c'] = color
        cases [i + 40] [j + 45] ['s'] = life_status
        cases [i + 40] [j + 45] ['c'] = color
        cases [i + 40] [j + 46] ['s'] = life_status
        cases [i + 40] [j + 46] ['c'] = color
        
        color = "yellow"
        cases [i + 27] [j + 36] ['s'] = life_status
        cases [i + 27] [j + 36] ['c'] = color
        
        cases [i + 26] [j + 36] ['s'] = life_status
        cases [i + 26] [j + 36] ['c'] = color
        
        cases [i + 36] [j + 70] ['s'] = life_status
        cases [i + 36] [j + 70] ['c'] = color
        
        cases [i + 35] [j + 70] ['s'] = life_status
        cases [i + 35] [j + 70] ['c'] = color
        
        color = "grey"
        cases [i + 36] [j + 69] ['s'] = life_status
        cases [i + 36] [j + 69] ['c'] = color
        
        cases [i + 35] [j + 68] ['s'] = life_status
        cases [i + 35] [j + 68] ['c'] = color
        cases [i + 35] [j + 69] ['s'] = life_status
        cases [i + 35] [j + 69] ['c'] = color
        
        
        color = "black"
        cases [i + 11] [j + 53] ['s'] = life_status
        cases [i + 11] [j + 53] ['c'] = color
        cases [i + 11] [j + 54] ['s'] = life_status
        cases [i + 11] [j + 54] ['c'] = color
        cases [i + 11] [j + 55] ['s'] = life_status
        cases [i + 11] [j + 55] ['c'] = color
        cases [i + 11] [j + 56] ['s'] = life_status
        cases [i + 11] [j + 56] ['c'] = color
        cases [i + 11] [j + 57] ['s'] = life_status
        cases [i + 11] [j + 57] ['c'] = color
        
        cases [i + 10] [j + 53] ['s'] = life_status
        cases [i + 10] [j + 53] ['c'] = color
        
        cases [i + 9] [j + 53] ['s'] = life_status
        cases [i + 9] [j + 53] ['c'] = color
        cases [i + 9] [j + 54] ['s'] = life_status
        cases [i + 9] [j + 54] ['c'] = color
        
        cases [i + 8] [j + 54] ['s'] = life_status
        cases [i + 8] [j + 54] ['c'] = color
        
        cases [i + 7] [j + 54] ['s'] = life_status
        cases [i + 7] [j + 54] ['c'] = color
        
        cases [i + 6] [j + 53] ['s'] = life_status
        cases [i + 6] [j + 53] ['c'] = color
        
        cases [i + 5] [j + 52] ['s'] = life_status
        cases [i + 5] [j + 52] ['c'] = color
        
        color = "peru"
        cases [i + 10] [j + 54] ['s'] = life_status
        cases [i + 10] [j + 54] ['c'] = color
        cases [i + 10] [j + 55] ['s'] = life_status
        cases [i + 10] [j + 55] ['c'] = color
        cases [i + 10] [j + 56] ['s'] = life_status
        cases [i + 10] [j + 56] ['c'] = color
        cases [i + 10] [j + 57] ['s'] = life_status
        cases [i + 10] [j + 57] ['c'] = color
        cases [i + 10] [j + 58] ['s'] = life_status
        cases [i + 10] [j + 58] ['c'] = color
        
        
        cases [i + 9] [j + 55] ['s'] = life_status
        cases [i + 9] [j + 55] ['c'] = color
        cases [i + 9] [j + 56] ['s'] = life_status
        cases [i + 9] [j + 56] ['c'] = color
        cases [i + 9] [j + 57] ['s'] = life_status
        cases [i + 9] [j + 57] ['c'] = color
        cases [i + 9] [j + 58] ['s'] = life_status
        cases [i + 9] [j + 58] ['c'] = color
        
        
        cases [i + 8] [j + 55] ['s'] = life_status
        cases [i + 8] [j + 55] ['c'] = color
        cases [i + 8] [j + 56] ['s'] = life_status
        cases [i + 8] [j + 56] ['c'] = color
        cases [i + 8] [j + 57] ['s'] = life_status
        cases [i + 8] [j + 57] ['c'] = color
        cases [i + 8] [j + 58] ['s'] = life_status
        cases [i + 8] [j + 58] ['c'] = color
        

        cases [i + 7] [j + 55] ['s'] = life_status
        cases [i + 7] [j + 55] ['c'] = color
        cases [i + 7] [j + 56] ['s'] = life_status
        cases [i + 7] [j + 56] ['c'] = color
        cases [i + 7] [j + 57] ['s'] = life_status
        cases [i + 7] [j + 57] ['c'] = color
        cases [i + 7] [j + 58] ['s'] = life_status
        cases [i + 7] [j + 58] ['c'] = color
        
        cases [i + 6] [j + 54] ['s'] = life_status
        cases [i + 6] [j + 54] ['c'] = color
        cases [i + 6] [j + 55] ['s'] = life_status
        cases [i + 6] [j + 55] ['c'] = color
        cases [i + 6] [j + 56] ['s'] = life_status
        cases [i + 6] [j + 56] ['c'] = color
        cases [i + 6] [j + 57] ['s'] = life_status
        cases [i + 6] [j + 57] ['c'] = color
        cases [i + 6] [j + 58] ['s'] = life_status
        cases [i + 6] [j + 58] ['c'] = color
        
        cases [i + 5] [j + 53] ['s'] = life_status
        cases [i + 5] [j + 53] ['c'] = color
        cases [i + 5] [j + 54] ['s'] = life_status
        cases [i + 5] [j + 54] ['c'] = color
        cases [i + 5] [j + 55] ['s'] = life_status
        cases [i + 5] [j + 55] ['c'] = color
        cases [i + 5] [j + 56] ['s'] = life_status
        cases [i + 5] [j + 56] ['c'] = color
        cases [i + 5] [j + 57] ['s'] = life_status
        cases [i + 5] [j + 57] ['c'] = color
        
        cases [i + 4] [j + 53] ['s'] = life_status
        cases [i + 4] [j + 53] ['c'] = color
        cases [i + 4] [j + 54] ['s'] = life_status
        cases [i + 4] [j + 54] ['c'] = color
        cases [i + 4] [j + 55] ['s'] = life_status
        cases [i + 4] [j + 55] ['c'] = color
        cases [i + 4] [j + 56] ['s'] = life_status
        cases [i + 4] [j + 56] ['c'] = color
        
        
        color = "brown"
        cases [i + 11] [j + 52] ['s'] = life_status
        cases [i + 11] [j + 52] ['c'] = color
        
        cases [i + 10] [j + 51] ['s'] = life_status
        cases [i + 10] [j + 51] ['c'] = color
        cases [i + 10] [j + 52] ['s'] = life_status
        cases [i + 10] [j + 52] ['c'] = color
        
        cases [i + 9] [j + 51] ['s'] = life_status
        cases [i + 9] [j + 51] ['c'] = color
        cases [i + 9] [j + 52] ['s'] = life_status
        cases [i + 9] [j + 52] ['c'] = color
        
        cases [i + 8] [j + 51] ['s'] = life_status
        cases [i + 8] [j + 51] ['c'] = color
        cases [i + 8] [j + 52] ['s'] = life_status
        cases [i + 8] [j + 52] ['c'] = color
        cases [i + 8] [j + 53] ['s'] = life_status
        cases [i + 8] [j + 53] ['c'] = color
        
        cases [i + 7] [j + 51] ['s'] = life_status
        cases [i + 7] [j + 51] ['c'] = color
        cases [i + 7] [j + 52] ['s'] = life_status
        cases [i + 7] [j + 52] ['c'] = color
        cases [i + 7] [j + 53] ['s'] = life_status
        cases [i + 7] [j + 53] ['c'] = color
        
        cases [i + 6] [j + 51] ['s'] = life_status
        cases [i + 6] [j + 51] ['c'] = color
        cases [i + 6] [j + 52] ['s'] = life_status
        cases [i + 6] [j + 52] ['c'] = color
    
        cases [i + 22] [j + 44] ['s'] = life_status
        cases [i + 22] [j + 44] ['c'] = color
        cases [i + 22] [j + 45] ['s'] = life_status
        cases [i + 22] [j + 45] ['c'] = color
        
        cases [i + 23] [j + 44] ['s'] = life_status
        cases [i + 23] [j + 44] ['c'] = color
        cases [i + 23] [j + 45] ['s'] = life_status
        cases [i + 23] [j + 45] ['c'] = color
           
    except:
        pass
    return grid