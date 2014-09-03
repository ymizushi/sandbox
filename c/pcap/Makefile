# Program Name
PROG = cappac
# SDL Options
SDL_OPTS = `sdl-config --cflags --libs ` -g
# Linked Libraries
#
UNAME := $(shell uname)

ifeq ($(UNAME), Darwin)
	LL = -framework GLUT -framework OpenGL 
endif
ifeq ($(UNAME), Linux)
	LL = -lGL -lGLU
endif

all: $(PROG)

clean:
	rm $(PROG)

$(PROG):  main.c 
	gcc -o $(PROG) -lpcap main.c $(SDL_OPTS) $(LL) 
