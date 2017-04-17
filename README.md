Texture
===========================
该项目用于处理不同硬件系统下得到的FCC织构数据，将其转化成Texture Calc可识别的文件格式；同时，绘图模块可供绘制ODF、Polar-Figure
****
### Author:LSKVCXZ
### E-mail:lskvcxz@sina.com / lskvcxz@csu.edu.cn
****
## 目录
* [Demos](#demos)
* [Results](#results)
* [Tools](#tools)
    * tools.py
* [Trans](#trans)
    * FGT.py
    * HODF.py
    * CLM.py
* [Plot](#plot)
    * ODF
    * Polar-Figure
* [图片](#图片)
    * ODF
    * Polar-Figure
****
****
### Demos
------
主程序会根据源文件行数，自行判断执行哪些模块，并将生成的文件放入Results文件夹
#### Demo1.txt
XRD测出的取向分布函数原始数据

    PHI1    PHI2     PHI       ODF
    0.00    0.00    0.00   0.233003E+01
    5.00    0.00    0.00   0.211788E+01
    ......

#### Demo2.txt
EBSD测出的C参数数据

    i	L	Mu	Nu	Re	Im
    1	0	1	1	1.000	0.000
    2	4	1	1	0.565	0.000
    3	4	1	2	0.711	0.000
    ......

****
### Results
------
用于存放经Trans各模块转化后的文件
#### Demo1.txt
``
获得文件格式为：Demo1.FGT、Demo1.HODF
``

#### Demo2.txt
``
获得文件格式为：Demo2.CLM
``

****
### Tools
------
各模块所涉及到的方法，封装在tools.py的tool类中

```Python
......
class tool:
    @staticmethod
    def Read_file (Min, Max, lines, Variable, split):
        for x in range (Min, Max+1):
            Variable.append (float(lines[x].split()[split]))
    ......
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
    ......
```

****
### Trans
------
转化文件格式
#### FGT.py
XRD测出的取向分布函数原始数据

```Python
......
def fgt(O_path, W_path, lines, PHI1 = [], ODF = []):
    ......
    k = open(O_path+'/Results/'+W_path+'.FGT', 'w')
    k.write (k.name+'\n'+'\n'+'LMAX =99 NPF =00'+'\n')
    k.write ('Cuts: '+'1'+'\n'+' 5 5 5'+'\n'+' 90 90 90'+'\n')
    a.Write_fgt (k, 857, 8, First)
    a.Write_fgt (k, 1, 3, Last)
    k.close()
```

#### HODF.py
EBSD测出的C参数数据

```Python
......
def hodf(O_path, W_path, lines, PHI2 = [], ODF = []):
    ......
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
```

#### CLM.py
EBSD测出的C参数数据

```Python
......
def clm(O_path, W_path, lines, L = [], Mu = [], Nu = [], Re = []):
    ......
    k = open(O_path+'/Results/'+W_path+'.CLM', 'w')
    k.write ('TEXEVAL'+'\n'+'Analysis started on xx-xxx-xx xx:xx:xx')
    k.write ('\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n '+'\n')
    k.write (' CUBI ORTHO'+'\n'+' LMAXE=22'+'\n')
    a.Write_clm (k, L, Mu, Nu, Re)
    k.close()
```

****
### Plot
------
输出图片
#### ODF
```Python
......
def odf(lines, PHI2 = [], ODF = []):
......
    for y in range (19):
        angle = np.linspace (0,90,19)
        [X, Y] = np.meshgrid (angle, angle)
        ax = plt.subplot (4, 5, y+1)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.contour (X, -Y, U[y])
    plt.show ()
```

#### Polar-Figure
```Python
......
while True:
# Input the orientation of a slip system
	[h, k, l] = input ("Enter HKL(interval with commas):")
	[u, v, w] = input ("Enter UVW(interval with commas):")
	F = input ("Enter pole-figure('1'refer to 100;'2'refer to 110;'3'refer to 111):")

......

# Draw the scatter corresponding to the plane
	for i in range(0,shape(N)[1]):
		M = sqrt(N[:,1].T*N[:,1])
		C = mat(A)*N[:,i]
		X = -mat(C)[1,0]/float(1+mat(C)[2,0])/M
		Y =  mat(C)[0,0]/float(1+mat(C)[2,0])/M
		if C[2]<-0.001:
			continue
		plt.scatter([X, ], [Y, ], s=25, color = 'red')
		if i==shape(N)[1]-1:
			break
	if 0==0:
# Stop the loop
		break
# Whole body of the program

# plt.annotate('(111)[1-10]',xy = (-1.5,1.3),fontsize = 20)

plt.show()
```

****
### 图片
------
图片示例
#### ODF

* ![ODF](https://github.com/lskvcxz/Texture/raw/master/Demos/Demo1.png "ODF")
#### Polar-Figure

* ![Polar-Figure](https://github.com/lskvcxz/Texture/raw/master/Demos/Demo2.png "Polar-Figure")
