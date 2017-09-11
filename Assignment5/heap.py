#!/usr/bin/env python3

class heap:
	heap = []

	def __init__(self):
		self.heap=[]

	def __str__(self):
		string=" ".join(str(y) for y in self.heap)
		return string

	def makenull(self):
		self.heap=[]
  
	def insert(self, x):
		self.heap.append(x)
		self.upheap(len(self.heap)-1)

	def parent(self, i):
		return int (i-1)//2
  
	def left(self, i):
		return int ((i+1)*2-1)
  
	def right(self, i):
		return int ((i+1)*2)

	def swap(self, a, b):
		temp=self.heap[a]
		self.heap[a]=self.heap[b]
		self.heap[b]=temp

	def upheap(self, i):
		par=self.parent(i)
		if i>0 and (self.heap[i]<self.heap[par]):
			self.swap(i, par)
			self.upheap(par)

	def downheap(self, i):
		if(self.left(i)<len(self.heap)):
			left=self.left(i)
			child=left
			if self.right(i)<len(self.heap):
				right=self.right(i)
				if self.heap[right]<self.heap[left]:
					child=right
			if(self.heap[child]<self.heap[i]):
				self.swap(i, child)
				self.downheap(child)

	def inorder(self, i):
		if(i< len(self.heap)):
			self.inorder(self.left(i))
			print(str(self.heap[i])+" ",end='')
			self.inorder(self.right(i))

	def preorder(self, i):
		if(i< len(self.heap)):
			print(str(self.heap[i])+" ",end='')
			self.preorder(self.left(i))
			self.preorder(self.right(i))

	def postorder(self, i):
		if(i< len(self.heap)):
			self.postorder(self.left(i))
			self.postorder(self.right(i))
			print(str(self.heap[i])+" ",end='')

	def min(self):
		theMin = self.heap[0]
		print(theMin)
		return theMin

	def deletemin(self):
		if self.heap[0]==None:
			raise Empty("Heap is empty")
		self.swap(0, len(self.heap)-1)
		self.heap.pop()
		self.downheap(0)
		
