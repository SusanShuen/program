import tangential_radial as tr
import numpy as np

row = col = 50

i = 25
j = 20

degree = -np.pi/2
# print degree

x,y = tr.im2Cartesian(j,i,(row,col))
print x,y

x1, y1 = tr.rotate((x, y), degree)
print x1,y1

x2, y2 = tr.rotate((x, y), 2*degree)
print x2,y2

j1, i1 = tr.Cartesian2im(x1, y1, (row,col))
print i1,j1

j2, i2 = tr.Cartesian2im(x2, y2, (row,col))
print i2,j2

ref_u1 = (j-j1)
ref_v1 = (i-i1)
print ref_u1, ref_v1

ref_u2 = j2-j1
ref_v2 = i2-i1
print ref_u2, ref_v2

RADi, RADj, TANi, TANj, Oi, Oj = tr.tan_rad(row, col, (i1,j1), (ref_u1,ref_v1), (ref_u2,ref_v2))
print RADi, RADj, TANi, TANj, Oi, Oj