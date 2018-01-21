#!/usr/bin/env python

"""
./HornSchunck.py data/box/box
./HornSchunck.py data/office/office
./HornSchunck.py data/rubic/rubic
./HornSchunck.py data/sphere/sphere
"""

from scipy.ndimage import imread
from matplotlib.pyplot import show
import numpy as np
from pyoptflow import HornSchunck
from pyoptflow.plots import compareGraphs
from deep_flow import df, drawflow

FILTER = 7


def magnitude(x,y):
    return np.sqrt((x**2 + y**2))


def HS(fn1, fn2):
	im1 = imread(fn1, flatten=True)
	im2 = imread(fn2, flatten=True)

	U,V = HornSchunck(im1, im2, 1, 100)
	compareGraphs(U, V, im2)

	return U,V


def acc_dong(fn1, fn2, fn3):
	im1 = imread(fn1, flatten=True)
	im2 = imread(fn2, flatten=True)
	im3 = imread(fn3, flatten=True)
	
	U1,V1 = HornSchunck(im1, im2, 1, 100)
	U2,V2 = HornSchunck(im2, im3, 1, 100)

	u_x, u_y = HornSchunck(U1, U2, 1, 100)
	v_x, v_y = HornSchunck(V1, V2, 1, 100)

	U = magnitude(u_x, u_y)
	V = magnitude(v_x, v_y)

	compareGraphs(U, V, im2)


	return U, V


def acc_df(fn1, fn2, fn3):
	im1 = imread(fn1)
	im2 = imread(fn2)
	im3 = imread(fn3)

	if len(im1.shape) == 2:
		im1 = np.dstack((im1,im1,im1))
		im2 = np.dstack((im2,im2,im2))
		im3 = np.dstack((im3,im3,im3))

	U1, V1 = df(im2, im1)
	U2, V2 = df(im2, im3)

	U = U1 + U2
	V = V1 + V2

	compareGraphs(U, V, im2)

	return U, V


if __name__ == '__main__':
	fn1 = "/Users/user/jon/pendulum+circle/frame_0.png"
	fn2 = "/Users/user/jon/pendulum+circle/frame_1.png"
	fn3 = "/Users/user/jon/pendulum+circle/frame_3.png"

	# U, V = HS(fn1, fn2)
	acc_u, acc_v = acc_dong(fn1, fn2, fn3)
	# acc_u, acc_v = acc_df(fn1, fn2, fn3)
	show()
