#!/usr/bin/python
# -* - coding:UTF-8 -*-
import sys
sys.path.append('..')
from Tools import tools

def fgt(O_path, W_path, lines):
    PHI1, ODF = [], []
    a = tools.tool()
    a.Read_file (1, 6859, lines, PHI1, 0)
    a.Read_file (1, 6859, lines, ODF, 3)
    [First, Last] = a.Create_array (PHI1, ODF)

    k = open(O_path+'/Results/'+W_path+'.FGT', 'w')
    k.write (k.name+'\n'+'\n'+'LMAX =99 NPF =00'+'\n')
    k.write ('Cuts: '+'1'+'\n'+' 5 5 5'+'\n'+' 90 90 90'+'\n')
    a.Write_fgt (k, 857, 8, First)
    a.Write_fgt (k, 1, 3, Last)

    k.close()