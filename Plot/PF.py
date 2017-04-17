#!/usr/bin/python
# -* - coding:UTF-8 -*-

from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
from math import *
from numpy import *

print '''Copyright (c) Nov.20th,2016 LSK
MSE,CSU,China
E-mail:lskvcxz@csu.edu.cn'''

while True:

# Input the orientation of a slip system
	[h, k, l] = input ("Enter HKL(interval with commas):")
	[u, v, w] = input ("Enter UVW(interval with commas):")
	F = input ("Enter pole-figure('1'refer to 100;'2'refer to 110;'3'refer to 111):")

# Draw a standard circle
	fig = plt.figure(dpi = 100)
	ax = fig.add_subplot(111)
	cir1 = Circle(xy = (0.0, 0.0), radius = 1, alpha = 0.15)
	ax.add_patch(cir1)
	plt.axis('scaled')
	ax.set_xlim(-1.5,1.5)
	ax.set_ylim(-1.5,1.5)
	ax.set_xticks([])
	ax.set_yticks([])
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_color('none')
	ax.spines['left'].set_color('none')

# Draw scatters on the background
	plt.scatter([0, ], [0, ], s = 70, color = 'blue', marker = '+')
	plt.scatter([0, ], [0.925, ], s = 175, color = 'black', marker = '|')
	plt.scatter([-0.925,], [0, ], s = 175, color = 'black', marker = '_')
	plt.annotate('RD', xy = (-0.13, 1.05), fontsize = 16)
	plt.annotate('TD', xy = (-1.25, -0.06), fontsize = 16)

# Create orientation matrix
	phi = acos(l/sqrt(h**2+k**2+l**2))
	phi1= asin((w/sqrt(u**2+v**2+w**2))*(sqrt(h**2+k**2+l**2)/sqrt(h**2+k**2)))
	phi2= acos(k/sqrt(h**2+k**2))
	A1 = array([[cos(phi2),sin(phi2),0],[-sin(phi2),cos(phi2),0],   [0,0,1]])
	A2 = array([[1,0,0],                [0,cos(phi),sin(phi)],      [0,-sin(phi),cos(phi)]])
	A3 = array([[cos(phi1),sin(phi1),0],[-sin(phi1),cos(phi1),0],   [0,0,1]])
	A = (mat(A1)*mat(A2)*mat(A3)).I
	print phi1*180/pi,phi*180/pi,phi2*180/pi

# Different planes in the same crystal plane family
	if F == 1:
		N = matrix('[1,0,0]; [-1,0,0]; [0,1,0]; [0,-1,0]; [0,0,1]; [0,0,-1]').T
		plt.annotate('{100}', xy = (-0.35,-1.3), fontsize = 20)
	elif F == 2:
		N = matrix('[1,1,0]; [-1,-1,0]; [-1,1,0]; [1,-1,0]; [1,0,1]; [-1,0,-1]; [1,0,-1]; [-1,0,1]; [0,1,1]; [0,-1,-1]; [0,1,-1]; [0,-1,1]').T
		plt.annotate('{110}', xy = (-0.35,-1.3), fontsize = 20)
	elif F == 3:
		N = matrix('[1,1,1]; [-1,-1,-1]; [-1,1,1]; [1,-1,-1]; [1,-1,1]; [-1,1,-1]; [1,1,-1]; [-1,-1,1]').T
		plt.annotate('{111}', xy = (-0.35,-1.3), fontsize = 20)

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