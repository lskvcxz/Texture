#!/usr/bin/python
# -* - coding:UTF-8 -*-
import numpy as np

class tool:

    @staticmethod
    def Read_file (Min, Max, lines, Variable, split):
        for x in range (Min, Max+1):
            Variable.append (float(lines[x].split()[split]))

    @staticmethod
    def Create_array (Eular_angle, ODF):
        Z = []
        for y in range (19):
            for x in range (6859):
                if Eular_angle[x] == 5*y:
                    Z.append (ODF[x])
        First = Z[0: 6856]
        Last  = Z[6856: 6859]
        First, Last = np.array (First).reshape (857, 8), [Last]
        return First, Last

    @staticmethod
    def Write_fgt (file, row, column, Variable):
        for i in range (row):
            for j in range(column):
                N = Variable[i][j]
                file.write(str(N).rjust(14))
            file.write ('\n')

    @staticmethod
    def Create_Z (Eular_angle, ODF):
        U = []
        for y in range (19):
            Z = []
            for x in range (6859):
                if Eular_angle[x] == 5*y:
                    Z.append (ODF[x])
            Z = np.array (Z).reshape (19,19)
            U.append(Z)
        return U

    @staticmethod
    def Write_hodf (file, U):
        for y in range(19):
            file.write (str(5*y) + '\n')
            for i in range (19):
                for j in range (19):
                    N = U[y][i][j]
                    if N > 10:
                        file.write (str('%-8.3f'%N))
                    else:
                        file.write (str('%-8.4f'%N))
                file.write ('\n')

    @staticmethod
    def Write_clm (file, L, Mu, Nu, Re):
        for i in range (23):
            if i % 2 == 0:
                for j in range (179):
                    if L[j] == i:
                        a, b = [], []
                        for x in range (179):
                            if Mu[x] == 2 and L[x] == i:
                                a.append (x)
                                b = a[-1]-a[0]+1
                        if b == []:
                            file.write (' L='+str(L[j]).rjust(2)+'NU='+str(Nu[j]).rjust(2)+str('%15.7E'%Re[j])+'\n')
                        else:
                            if Mu[j] == 1:
                                file.write (' L='+str(L[j])+'NU='+str(Nu[j]).rjust(2)+str('%15.7E'%Re[j])+str('%15.7E'%Re[j+b])+'\n')