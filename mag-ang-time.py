import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

mag = np.load('/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq/008a013s00L-normalized-mag-acc-rad-48.npy')
# ang = np.load('/Volumes/2TB/dataset/gait/SOTON/flow-normCrosSeq/008a013s00L-normalized-ang-acc-rad-48.npy')
# ang is in radians
plot = ax.plot_surface()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.show()