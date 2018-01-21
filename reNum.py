def reNum(in_num):
	if in_num < 10:
		num = '00'+str(in_num)

	elif in_num < 100:
		num = '0'+str(in_num)

	else:
		num = str(in_num)

	return num
