import cv2
import os.path

frame_path = '/Users/user/Desktop/008a013s00L'
video = cv2.VideoWriter('/Users/user/Desktop/flow.avi', 20, (720, 576))

for i in xrange (2, 73):
	frameName = os.path.join(frame_path, str(i)+'.png')
	print frameName
	img = cv2.imread(frameName)
	video.write(img)


video.release()
cv2.destroyAllWindows()