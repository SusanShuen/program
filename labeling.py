import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label
from skimage.morphology import closing, square
from skimage.measure import regionprops
from skimage.color import label2rgb

obj = '008a013s00L'

im_path = '/Users/user/dataSet/gait/' + obj + '/background_subtracted/binary'
save_path = '/Users/user/dataSet/gait/' + obj + '/background_subtracted/sil-'
num = 120
blur_radius = 2.0
row = 480
col = 640

for n in range (36, num):
	# print n
	im = cv2.imread(im_path + str(n) + '.png', 0)
	# print im.shape
	# print row,col
	new = np.zeros((row,col), dtype = np.uint8)
	

# smooth the image (to remove small objects)
	image = ndimage.gaussian_filter(im, blur_radius)

# find connected components
# 	labeled, nr_objects = ndimage.label(imf > threshold)

# apply threshold
	thresh = threshold_otsu(image)
	# print thresh
	bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
	cleared = bw.copy()
	clear_border(cleared)

# label image regions
	label_image = label(cleared)
	borders = np.logical_xor(bw, cleared)
	label_image[borders] = -1
	# image_label_overlay = label2rgb(label_image, image=image)

	# fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
	# ax.imshow(image_label_overlay)

	area = []
	for region in regionprops(label_image):
		area.append(region.area)
	# print area

	sorted_area = list(area)
	sorted_area.sort(reverse=True)
	# print sorted_area

	# print 'len area', len(area)
	if len(area) > 1:
		total_labels = 2
	else:
		total_labels = 1

	# print "total_labels", total_labels
	for obj in range (total_labels):
		obj_pixels = sorted_area[obj]
		obj_label = area.index(obj_pixels)
			# print obj_label
		coords = np.where(label_image == (obj_label + 1))
		obj_row = coords[0]
		obj_col = coords[1]

		obj_pixels = int(obj_pixels)
		for i in range (obj_pixels):
			r = obj_row[i]
			c = obj_col[i]
			new[r, c] = 255

	# for label_num in range (total_labels):
	# 	if area[label_num] < 4000:
	# 		continue
	# 	print 'label_num', area[label_num]

# draw rectangle around segmented coins
    # minr, minc, maxr, maxc = region.bbox
    # rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
    #                           fill=False, edgecolor='red', linewidth=2)
    # ax.add_patch(rect)

	# plt.show()
	cv2.imwrite(save_path + str(n) + '.png', new[])