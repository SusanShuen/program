CC=gcc-6

CFLAGS=-Wall -g -O3 -msse4 -fPIC
LDFLAGS=-g -Wall -O3 -msse4 -fPIC
LIBFLAGS=-lm -ljpeg -lpng
LIBAFLAGS=-static /home/lear/douze/tmp/jpeg-6b/libjpeg.a /usr/lib64/libpng.a /usr/lib64/libz.a /usr/lib64/libm.a
CPYTHONFLAGS=-I/usr/local//Cellar/python/2.7.9/Frameworks/Python.framework/Headers -I/usr/local//lib/python2.7/site-packages/numpy/core/include/

SOURCES := $(shell find . -name '*.c' ! -name 'deepflow2_wrap.c')
OBJ := $(SOURCES:%.c=%.o) 
HEADERS := $(shell find . -name '*.h')

all: deepflow2

deepflow2: $(OBJ)
	$(CC) $(LDFLAGS) $(LIBFLAGS) -o $@ $^

deepflow2-static: $(OBJ)
	$(CC) -o $@ $^ $(LIBAFLAGS)

%.o: %.c
	$(CC) -o $@ $(CFLAGS) -c $+ 

python: all
	swig -python $(CPYTHONFLAGS) deepflow2.i
	gcc $(CFLAGS) -c deepflow2_wrap.c $(CPYTHONFLAGS)
	gcc -shared $(LDFLAGS)  -L /usr/local//Cellar/python/2.7.9/Frameworks/Python.framework/Versions/Current/lib/ -lpython2.7 deepflow2_wrap.o $(OBJ) -o _deepflow2.so $(LIBFLAGS)


clean:
	rm -f *.o deepflow2 _deepflow2.so deepflow2.pyc deepflow2.mex???
