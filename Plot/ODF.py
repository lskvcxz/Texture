#!/usr/bin/python
# -* - coding:UTF-8 -*-
import sys
sys.path.append('..')
from Tools import tools
import numpy as np
import matplotlib.pyplot as plt

def odf(lines, PHI2 = [], ODF = []):
    a = tools.tool()
    a.Read_file (1, 6859, lines, PHI2, 1)
    a.Read_file (1, 6859, lines, ODF,  3)

    plt.figure (1, figsize = (10, 8))
    U = a.Create_Z(PHI2, ODF)

    for y in range (19):
        angle = np.linspace (0,90,19)
        [X, Y] = np.meshgrid (angle, angle)
        ax = plt.subplot (4, 5, y+1)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.contour (X, -Y, U[y])
    plt.show ()