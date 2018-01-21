import os

def checkDir(dir):
    check_res = os.path.exists(dir)
    if check_res == False:
        # print "true"
        os.mkdir(dir)