filename = '/Users/user/Desktop/test.txt'
# script, filename = argv
target = open(filename, 'w')
target.write("34")
target.write("\n")
target.write("345")

target.close()