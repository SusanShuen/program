import numpy as np
from os import listdir
from os.path import join, isfile, splitext
import math


def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


u_path = '/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq/008a013s00L-normalized-acc-rad_u-48.npy'
v_path = '/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq/008a013s00L-normalized-acc-rad_v-48.npy'
# save_path = '/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq-img/008a013s00L'
# flowseq = [f for f in listdir(data_path) if isfile(join(data_path, f))]
# flowseq = filter(lambda x: x.lower().endswith(('.npy')), flowseq)

u = np.load(u_path)
# print "u shape", u.shape
total_fram_num = u.shape[2]
v = np.load(v_path)

flow_name = u_path.split('/')
flow_name = splitext(flow_name[-1])[0]
flow_name = flow_name.split('-')
print flow_name

if len(flow_name)==4:
	obj, fltype, fldir, start_num = flow_name

elif len(flow_name)==5:
	obj, _normalize, fltype, fldir, start_num = flow_name
	fldir = fldir.split('_')

# print "start from", start_num

mag = np.zeros_like(u)
ang = np.zeros_like(u)
for i in xrange(total_fram_num):
	print i
	u_i = u[:,:,i]
	v_i = v[:,:,i]
	
	# print u_i.shape
	# idx = abs(u_i)>0.0001
	# print u_i[idx]

	# idx = (u_i==0 & v_i==0)
	# # print idx
	# u_i[idx] = np.nan
	# v_i[idx] = np.nan
	for y in xrange(u_i.shape[0]):
		for x in xrange(u_i.shape[1]):
			mag[y,x,i] = math.sqrt(u_i[y,x]**2 + v_i[y,x]**2)
			v_y = [y, y+v_i[y,x]]
			v_x = [x, x+u_i[y,x]]
			ang[y,x,i] = angle_between(v_x, v_y)

mag_save_name = '/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq/008a013s00L-normalized-mag-acc-rad-48.npy'
ang_save_name = '/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq/008a013s00L-normalized-ang-acc-rad-48.npy'
np.save(mag_save_name, mag)
np.save(ang_save_name, ang)
