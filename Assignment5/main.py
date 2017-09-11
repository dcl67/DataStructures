#!/usr/bin/env python3
from heap import heap

def help():
	print('help - Prints this list')
	print('makenull - Clears the heap')
	print('insert <integer> - Inserts the number into the heap')
	print('min - Prints the current min on the heap')
	print('inorder - Prints heap in inorder')
	print('preorder - Prints heap in preorder')
	print('postorder - Prints heap in postorder')
	print('deletemin - Removes min from the heap')
	print('sort - Calls deletemin repeatedly to print out sorted numbers')
	print('exit - Exits the program (also Crtl-D exits')

if __name__ == '__main__':
	queue = heap()
	print('Welcome to the Heap\nThe List of Commands is below, type help to see them again.')
	help()
	method=''
	enter=''
	while method != 'exit':
		enter = input('>').split(" ")
		if len(enter) == 0:
			print('Bad Command - type help for commands')
		elif len(enter) == 1:
			method = str(enter[0])
		elif len(enter) == 2:
			method = str(enter[0])
			integer = int(enter[1])
		else:
			print('Bad Command - type help for commands')
		if method == 'makenull':
			queue = heap()
		elif method == 'insert':
			queue.insert(integer)
		elif method == 'min':
			queue.min()
		elif method == 'inorder':
			queue.inorder(0)
			print('')
		elif method == 'preorder':
			queue.preorder(0)
			print('')
		elif method == 'postorder':
			queue.postorder(0)
			print('')
		elif method == 'deletemin':
			queue.deletemin()
		elif method == 'sort':
			while len(queue.__str__()) != 0:
				queue.min()
				queue.deletemin()
		elif method == 'help':
			help()
		elif method == 'exit':
			method = 'exit'
			break
		else:
			print('Bad Command - type help for commands')
