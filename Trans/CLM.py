#!/usr/bin/python
# -* - coding:UTF-8 -*-
import sys
sys.path.append('..')
from Tools import tools

def clm(O_path, W_path, lines, L = [], Mu = [], Nu = [], Re = []):
    a = tools.tool()
    a.Read_file (1, 179, lines, L,  1)
    a.Read_file (1, 179, lines, Mu, 2)
    a.Read_file (1, 179, lines, Nu, 3)
    a.Read_file (1, 179, lines, Re, 4)

    L  = [int(i) for i in L]
    Mu = [int(i) for i in Mu]
    Nu = [int(i) for i in Nu]

    k = open(O_path+'/Results/'+W_path+'.CLM', 'w')
    k.write ('TEXEVAL'+'\n'+'Analysis started on xx-xxx-xx xx:xx:xx')
    k.write ('\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n')
    k.write (' CUBI ORTHO'+'\n'+' LMAXE=22'+'\n')
    a.Write_clm (k, L, Mu, Nu, Re)

    k.close()