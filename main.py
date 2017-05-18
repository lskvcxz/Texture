#!/usr/bin/python
# -* - coding:UTF-8 -*-
import os
import sys
from Trans import *
from Plot import ODF

if __name__ == '__main__':
    O_path = sys.path[0]
    for root, dirs, files in os.walk(O_path+'/Demos/'):
        for file in files:
            W_path = file.split('.')[0]

            f = open(O_path+'/Demos/'+file, 'r')
            lines = f.readlines()
            f.close()

            for index, line in enumerate(lines):
                pass

            if index>6000 and index<7000:
                FGT.fgt(O_path, W_path, lines)
                HODF.hodf(O_path, W_path, lines)
                ODF.odf(lines)

            elif index>100 and index<200:
                CLM.clm(O_path, W_path, lines)


    for root, dirs, files in os.walk(O_path):
        for file in files:
            rm = file.split('.')[-1]
            if rm == 'pyc' or rm == 'DS_Store':
                os.remove(os.path.join(root, file))