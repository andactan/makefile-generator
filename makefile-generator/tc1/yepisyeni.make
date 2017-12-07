CC=gcc

addTwoInt.o: ./src1/addTwoInt.c 
	$(CC) -I ./headers1 -c ./src1/addTwoInt.c

multTwoInt.o: ./src1/multTwoInt.c
	$(CC) -I ./headers1 -c ./src1/multTwoInt.c

main1.o: ./main1.c
	$(CC) -I ./headers1 -c ./main1.c

all: main1.o addTwoInt.o multTwoInt.o
	$(CC) main1.o addTwoInt.o multTwoInt.o -o hello
