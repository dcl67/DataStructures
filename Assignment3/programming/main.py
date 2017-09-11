#!/usr/bin/python3
import math
global counter

def bubblesort(list):
    counter = 0
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                counter += 1
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    return list, counter

def insertion(list):
    counter = 0
    for i in range(1,len(list)):
        current=list[i]
        pos = i
        while pos>0 and list[pos-1]>current:
            counter+=1
            list[pos]=list[pos-1]
            pos-=1
        list[pos]=current
    print("Comparisons: " + str(counter))
    print("Approx Min: " + str(math.ceil(math.log(math.factorial(len(list)),2))))
    return list

def mergesort(list):
    counter = 0
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                counter += 1
                list[k]=left[i]
                i+=1
            else:
                counter += 1
                list[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            list[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            list[k]=right[j]
            j+=1
            k+=1
    return list, counter

def partition(mylist, first, last):
    count = 0
    pos = first
    for i in range(first, last):
        count += 1
        if mylist[i] < mylist[last]:
            mylist[i], mylist[pos] = mylist[pos], mylist[i]
            pos += 1
    mylist[pos], mylist[last] = mylist[last], mylist[pos]
    return pos, count

def qsort(mylist, first, last):
    count = 0
    if first < last:
        pos, count = partition(mylist, first, last)        
        count += qsort(mylist, first, pos - 1)
        count += qsort(mylist, pos + 1, last)
    return count

def quicksort(mylist, first=None, last=None):
    if first is None:
        first = 0
    if last is None:
        last = len(mylist) - 1
    return qsort(mylist, first, last)

def help():
	print("Commands:")
	print(
	"help - Prints this menu\nexit or CTRL-D - Exits the program\nsort_method int_list - Enter a sort method followed by a list of space separated integers to sort them")
	print("Possible Sort Methods: bublesort insertion mergesort quicksort")
	print("Example: bubblesort 76 68 77 86 75")

if __name__ == "__main__":
	method = ""
	print("Welcome to the sorting thunderdome\nThis program is used to compare sorting methods")
	print("Commands:")
	print("help - Prints this menu\nexit or CTRL-D - Exits the program\nsort_method int_list - Enter a sort method followed by a list of space separated integers to sort them")
	print("Possible Sort Methods: bublesort insertion mergesort quicksort")
	print("Example: bubblesort 76 68 77 86 75")
	while (method != "exit"): # (method != "exit" or method != "Exit" or method or "EXIT"):
		array = []
		entry = input("Command: ").split(" ")
		method = str(entry[0])
		for i in range(1, len(entry)):
			array.append(int(entry[i]))
		if str(method) == "help" or str(method) == "Help":
			help()
		elif str(method) == "bubblesort":
			print("Using Bubble Sort")
			final, counter = bubblesort(array)
			print(final)
			print("Comparisons: " + str(counter))
			print("Approx Min: " + str(math.ceil(math.log(math.factorial(len(final)),2))))
		elif str(method) == "quicksort":
			print("Using Quick Sort")
			counter = quicksort(array)
			print(array)
			print("Comparisons: " + str(counter))
			print("Approx Min: " + str(math.ceil(math.log(math.factorial(len(array)),2))))
		elif str(method) == "insertion":
			print("Using Insertion Sort")
			final = insertion(array)
			print(final)
		elif str(method) == "mergesort":
			print("Using Merge Sort")
			final, counter = mergesort(array)
			print(final)
			print("Comparisons: " + str(counter))
			print("Approx Min: " + str(math.ceil(math.log(math.factorial(len(final)), 2))))
		elif str(method) == "exit" or str(method) == "Exit":
			method = "exit"
		else:
			print("Invalid input. Enter ""help"" if you need to review the options.")

	print("Bye")
