#!/usr/bin/python3
from queue import *
from node import *
from sys import argv

def josephus(people, nth):
	number = int(people)
	multiple = int(nth)
	Q = Queue()
	numb = number+1
	i=0
	tot = 0
	num = int(number)-1
	for i in range(0,number):
		tot += multiple
		if tot > number:
			tot = (tot % number)
			if tot < 0:
				tot+=1
		Q.enqueue(tot-1)
		i += 1
	print(str(Q))

if __name__ == "__main__":
	people = argv[1]
	nth = argv[2]
	josephus(people, nth)

