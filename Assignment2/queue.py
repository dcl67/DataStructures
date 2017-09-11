#!/usr/bin/python3
from node import *

class Queue():
	def __init__(self):
		self.incr = 0
		self.begin = None
		self.end = None
	def __str__(self):
		if self.incr == 0:
			return "Queue Empty" 
		else:
			result = "[ " + str(self.begin.getValue()) + " ]"
			iteration = self.begin.getNext()
			while iteration != None:
				result += "[ " + str(iteration.getValue()) + " ]"
				iteration = iteration.getNext()
			return result 
	def front(self):
		return self.begin.getValue()
	def empty(self):
		if self.incr == 0:
			return True
		else:
			return False
	def dequeue(self):
		if self.incr != 0:
			toDel = self.begin.getValue()
			self.begin = self.begin.getNext()
			if self.incr == 1:
				self.end = None
			self.incr -= 1
			return toDel
	def enqueue(self, element):
		if self.incr == 0:
			self.begin = Node(element, None)
			self.end = self.begin
		else:
			toAdd = Node(element, None)
			self.end.setNext(toAdd)
			self.end = toAdd
		self.incr += 1
