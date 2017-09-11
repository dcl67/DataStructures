#!/usr/bin/python3
from queue import *
from node import *
from sys import argv
"""
def josephus(people,nth):
	number = int(people) + 1
	multiple = int(nth)
	Q = []
	todel = []
	final = []
	i=number
	j=number-1
	l=0
	m=0
	iterto = number-2
	for i in range(1,number):
		Q.append(i)
	total = 0
	while l < j:
		total = (total + multiple)
		if total >= j:
			total %= j
		todel.append(total-1)
		l += 1
	#print(todel)
	for m in range(len(todel)):
		final.append(Q[todel[m]])
	print(final)
"""		
def josephus(people, nth):
	number = int(people)
	multiple = int(nth)
	Q = Queue()
	Q.enqueue(multiple)
	i=0
	tot = 0
	num = int(number)-1
	for i in range(0,number):
		str(Q)
		Q.enqueue(tot)
		tot += multiple
		if tot >= num:
			tot = tot % number
		print(tot)
		Q.enqueue(tot)
		i += 1
	print(Q)
	str(Q)


if __name__ == "__main__":
	people = argv[1]
	nth = argv[2]
	josephus(people, nth)

