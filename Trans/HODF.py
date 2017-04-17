#!/usr/bin/python
# -* - coding:UTF-8 -*-
import sys
sys.path.append('..')
from Tools import tools

def hodf(O_path, W_path, lines, PHI2 = [], ODF = []):
    a = tools.tool()
    a.Read_file (1, 6859, lines, PHI2, 1)
    a.Read_file (1, 6859, lines, ODF,  3)

    k = open(O_path+'/Results/'+W_path+'.HODF', 'w')
    k.write (k.name+'\n'+'19  19  19'+'\n'+'0'+'\n')
    k.write ('1.00    1.00    1.00    90.00    90.00    90.00'+'\n')
    k.write ('3'+'\n'+'\n'+'\n'+'\n')
    k.write ('0    0    0    '+'\n'+'0    0    0    '+'\n'+'0    0    0    '+'\n')
    k.write ('0'+'\n'+'5.00'+'\n'+'1'+'\n'+'0'+'\n'+'2'+'\n'+'15  6'+'\n')
    k.write ('0.0100  0.0872'+'\n')
    U = a.Create_Z(PHI2, ODF)
    a.Write_hodf (k, U)

    k.close()