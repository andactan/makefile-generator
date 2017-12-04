CC=gcc

all: hello

hellomake.o:  hellomake.c
	$(CC) -c /Users/andac/PycharmProjects/mc-makefile/src/hellomake.c

hellofunc.o:  hellofunc.c
	$(CC) -c /Users/andac/PycharmProjects/mc-makefile/src/hellofunc.c

hello: hellomake.o hellofunc.o 
	$(CC) hellomake.o hellofunc.o -o hello