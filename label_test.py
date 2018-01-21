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

import cv2

im_path = '/Users/user/dataSet/gait/6000104/background_subtracted/binary'
save_path = '/Users/user/dataSet/gait/6000104/background_subtracted/labeled'
num = 139

for n in range (36, num):
	image = cv2.imread(im_path + str(n) + '.png', 0)

# apply threshold
	thresh = threshold_otsu(image)
	bw = closing(image > thresh, square(3))

# remove artifacts connected to image border
	cleared = bw.copy()
	clear_border(cleared)

# label image regions
	label_image = label(cleared)
	borders = np.logical_xor(bw, cleared)
	label_image[borders] = -1
	image_label_overlay = label2rgb(label_image, image=image)

	fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 6))
	# ax.imshow(image_label_overlay)
	label_num = 0
	for region in regionprops(label_image):
		if region.area < 4000:
			continue
		# print n
		# print region.area

# draw rectangle around segmented coins
		label_num = label_num + 1
    	print label_num
    	minr, minc, maxr, maxc = region.bbox
    	print minr, minc, maxr, maxc
    	rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    	ax.add_patch(rect)

	# plt.show()