#!/usr/bin/python3
from node import *

class Queue():
	def __init__(self):
		self.queue = []
	def __str__(self):
		if len(self.queue) == 0:
			return "Queue Empty" 
		else:
			front = Node(1,None)
			result=""
			while(front != None):
				result+=str(front)
				front = front.getNext()
			return str(result)
	def front(self):
		return self.queue[0]
	def empty(self):
			if len(self.queue) == 0:
				return True
			else:
				return False
	def enqueue(self,x):
		return self.queue.append(x)
	def dequeue(self):
		to_delete=self.queue[0]
		del self.queue[0]
		return to_delete
