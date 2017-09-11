#!/usr/bin/python3
from math import sqrt
global counter
counter=0
memory={}

def add(a,b):
	global counter
	counter+=1
	added = a+b
	return added

def fib_closed(n):
	#return int((((1+sqrt(5))/2)**(n+1)-((1-sqrt(5))/2)**(n+1))/sqrt(5))
	return ((1+sqrt(5))**n-(1-sqrt(5))**n)//(2**n*sqrt(5))

def fib_classic(n):
	global counter
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		classic = add(fib_classic(n-1),fib_classic(n-2))
		return classic

def fib_loop(n):
	global counter
	a=0
	b=1
	if n==1:
		return 0
	elif n==2:
		return 1
	else:
		for i in range(0,n):
			t=a
			a=b
			if i < n-1:
				b=add(t,b)
		return a

def fib_mem(num):
	if num==0:
		memory[num]=0
		return memory[num]
	elif num==1:
		memory[num]=1
		return memory[num]
	else:
		if num not in memory.keys():
			calc = add(fib_mem(num-1),fib_mem(num-2))
			memory[num] = calc
		return (memory[num])

if __name__ == "__main__":
	print("Welcome to the Fibonacci Test Program\nTo exit, enter a negative number.\n")
	n = int(input("Enter a fibonacci Number to compute:\n"))
	while n >= 0:
		print("--------------------\nComputing the " + str(n) + "th Fibonacci Number:")
		global counter
		counter = 0
		closed = fib_closed(n)
		print("The closed form finds: %.0f"% closed)
		classic = fib_classic(n)
		print("The recursive definition finds: " + str(classic))
		print("Additions needed for recursive definition: " + str(counter))
		counter = 0
		loop = fib_loop(n)
		print("The loop definition finds: " + str(loop))
		print("Additions needed for loop definition: " + str(counter))
		counter = 0
		memoization = fib_mem(n)
		print("The memoizaion definition finds: " + str(memoization))
		print("Additions needed for memoization definition: " + str(counter))
		n = int(input("Enter a fibonacci Number to compute:\n"))
	#end
