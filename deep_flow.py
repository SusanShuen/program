import numpy as np
from PIL import Image
import scipy.misc
# import pdb


def df(im1, im2):
	import sys
	sys.path.append('/Python/DeepFlow_release2.0')
	sys.path.append('/Python/deepmatching_1.2.2_c++')
	from deepmatching import deepmatching
	from deepflow2 import deepflow2

	# pdb.set_trace()

	matches = deepmatching(im1, im2)
	flow = deepflow2(im1, im2, matches, '-sintel')
	u = flow[:,:,0]
	v = flow[:,:,1]
	return u, v


def drawflow(flow_im, u, v, step):
	for x in range (0, col-1, step):
		for y in range(0, row-1, step):
			dx = int(round(u[y,x]))
			dy = int(round(v[y,x]))
			if (abs(dx) > 2 or abs(dy) > 2):
				cv2.line(flow_im, (x,y), (x+dx, y+dy),
					(255, 0, 0), 1, cv2.CV_AA, 0)
	return flow_im


def main():
	im1 = np.array(Image.open(
		'/Volumes/2TB/dataset/gait/SOTON/rmBG/008a013s00L/75.png'))
	im2 = np.array(Image.open(
		'/Volumes/2TB/dataset/gait/SOTON/rmBG/008a013s00L/76.png'))

	u, v = df(im1, im2)

	uName = '/Users/user/Desktop/deepflow_u.png'
	vName = '/Users/user/Desktop/deepflow_v.png'

	# u = Image.fromarray((u*u_factor).astype(np.uint8))
	# v = Image.fromarray((v*v_factor).astype(np.uint8))
	# u.save(uName)
	# v.save(vName)

	scipy.misc.toimage(u, cmin=0.0, cmax=np.max(u)).save(uName)
	scipy.misc.toimage(v, cmin=0.0, cmax=np.max(v)).save(vName)


if __name__ == '__main__':
	main()