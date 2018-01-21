import os, sys

fileDir = '/Volumes/2TB/IET_CV/HSdata/CASIA-A/frame/0/wl'

for parent, dirnames, data in os.walk(fileDir):

	if len(parent.split('/')) == 8:
		data = filter(lambda x: x.endswith('.png'), data)

		for file in data:
			filename = os.path.splitext(file)[0]

			# [obj, num] = filename.split('-')
			# [ang, seq] = cont.split('_')
			num = int(filename)

			if num < 10:
				num = '00'+str(num)
			elif num < 100:
				num = '0'+str(num)
			else:
				num = str(num)

			org_file = os.path.join(parent, file)
			new_file = os.path.join(parent, num+'.png')
			os.rename(org_file, new_file)