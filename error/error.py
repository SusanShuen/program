from __future__ import division
import numpy as np
from acc_deep_flow import acc_deep_flow
from PIL import Image
import os
import tangential_radial as tr
import matplotlib.pyplot as plt


def AE(Uest,Uref,Vest,Vref):
	A = Uest*Uref + Vest*Vref + 1
	B = np.sqrt(Uest**2 + Vest**2 + 1)
	C = np.sqrt(Uref**2 + Vref**2 + 1)

	error = np.arccos(A/(B*C))
	return error


def EPE(Uest,Vest,Uref,Vref):
	error = np.sqrt((Uest - Uref)**2 + (Vest - Vref)**2)

	return error


imDir = "/Users/user/Desktop/CVPR/testImg/8pixels-"

im1 = np.array(Image.open(imDir + "0.png"))
im2 = np.array(Image.open(imDir + "1.png"))
im3 = np.array(Image.open(imDir + "3.png"))

row, col, dim = im1.shape

res_Uref = np.zeros((row, col), dtype=np.float64)
res_Vref = np.zeros((row, col), dtype=np.float64)

rad_Uref = np.zeros((row, col), dtype=np.float64)
rad_Vref = np.zeros((row, col), dtype=np.float64)

tan_Uref = np.zeros((row, col), dtype=np.float64)
tan_Vref = np.zeros((row, col), dtype=np.float64)

vel_Uref = np.zeros((row, col), dtype=np.float64)
vel_Vref = np.zeros((row, col), dtype=np.float64)


# linear motion
res_Uref[36:266, 56:306] = 8
res_Vref[36:266, 56:306] = 8
tan_Uref[36:266, 56:306] = 8
tan_Vref[36:266, 56:306] = 8
vel_Uref[36:266, 56:306] = 16
vel_Vref[36:266, 56:306] = 16

# degree = np.pi/18

# for i in xrange(35,265):
# 	for j in xrange(55,305):

# 		x,y = tr.im2Cartesian(j,i,(row,col))
# 		x1, y1 = tr.rotate((x, y), degree)
# 		x2, y2 = tr.rotate((x, y), 3*degree)

# 		j1, i1 = tr.Cartesian2im(x1, y1, (row,col))
# 		j2, i2 = tr.Cartesian2im(x2, y2, (row,col))

# 		ref_u1 = (j-j1)
# 		ref_v1 = (i-i1)
# 		# print ref_u1, ref_v1

# 		ref_u2 = j2-j1
# 		ref_v2 = i2-i1

# 		if abs(ref_u2)>0.5 or abs(ref_v2)>0.5:
# 			vel_Uref[int(round(i1)), int(round(j1))] = ref_u2
# 			vel_Vref[int(round(i1)), int(round(j1))] = ref_v2

# 		RADi, RADj, TANi, TANj, Oi, Oj = tr.tan_rad(row, col, (i1,j1), (ref_u1,ref_v1), (ref_u2,ref_v2))

# 		# print Oi,Oj

# 		if abs(ref_u2 + ref_u1)>0.5 or abs(ref_v2 + ref_v1)>0.5:
# 			res_Uref[int(round(i1)), int(round(j1))] = ref_u2 + ref_u1
# 			res_Vref[int(round(i1)), int(round(j1))] = ref_v2 + ref_v1

# 		if abs(RADj - j1)>0.5 or abs(RADi - i1)>0.5:
# 			rad_Uref[int(round(i1)), int(round(j1))] = RADj - j1
# 			rad_Vref[int(round(i1)), int(round(j1))] = RADi - i1

# 		if abs(TANj - j1)>0.5 or abs(TANi - i1)>0.5:
# 			tan_Uref[int(round(i1)), int(round(j1))] = TANj - j1
# 			tan_Vref[int(round(i1)), int(round(j1))] = TANi - i1


u1, v1, u2, v2 = acc_deep_flow(im1, im2, im3)

res_error = 0
rad_error = 0
tan_error = 0
vel_error = 0

for i in xrange (row):
	for j in xrange (col):

		Ua = u1[i,j] + u2[i,j]
		Va = v1[i,j] + v2[i,j]

		if abs(u2[i,j])>0.5 or abs(v2[i,j])>0.5:
			print "true1"
			new_vel_error = EPE(u2[i,j], v2[i,j], vel_Uref[i,j], vel_Vref[i,j])
			vel_error = vel_error + new_vel_error
			# print vel_error
			# print u2[i,j], v2[i,j], vel_Uref[i,j], vel_Vref[i,j]
			

		if abs(Ua) > 0.5 or abs(Va) > 0.5:
			new_res_error = EPE(Ua, Va, res_Uref[i,j], res_Vref[i,j])
			res_error = res_error + new_res_error


			RADi, RADj, TANi, TANj, Oi, Oj = tr.tan_rad(row, col, (i,j), (u1[i,j],v1[i,j]), (u2[i,j],v2[i,j]))
				
			rad_u = RADj-j
			rad_v = RADi-i
			
			new_rad_error = EPE(rad_u, rad_v, rad_Uref[i,j], rad_Vref[i,j],)
			# if abs(new_rad_error)>0.5:
				# print new_rad_error
			rad_error = rad_error + new_rad_error

			tan_u = TANj-j
			tan_v = TANi-i

			new_tan_error = EPE(tan_u, tan_v, tan_Uref[i,j], tan_Vref[i,j],)
			tan_error = tan_error + new_tan_error


print "vel_error", vel_error
print "res_error", res_error
print "rad_error", rad_error
print "tan_error", tan_error
