#!/usr/bin/env python3
Nodes=None
Graph=[[None]]

def dijkstra(G,start_node):
    global Nodes
    dist=[float("inf") for i in range(0,len(G))]
    prev=[None for i in range(0,len(G))]
    dist[start_node]=float(0)
    dNodes=Nodes
    while len(dNodes) > 0:
        smallest=[-1,-1,float("inf")]
        for i in range(0,len(dNodes)):
            for j in range(0,len(dNodes)):
                Di=dNodes[i]
                Dj=dNodes[j]
                if G[Di][Dj] < smallest[2]:
                    smallest=[Di, Dj, float(G[Di][Dj])]
        minNode=smallest[0]

        if minNode < 0:
            break
        dNodes.remove(minNode)
        for j in range(0,len(G)):
            alt=float(dist[minNode] + G[minNode][j])
            if alt < dist[j]:
                dist[j]=alt
                prev[j]=minNode
    return dist

def floyd(G):
    G=G
    for i in range(0,len(G)):
        G[i][i]=float(0)
    for i in range(0,len(G)):
        for j in range(0,len(G)):
            for k in range(0,len(G)):
                if G[i][j] > (G[i][k] + G[k][j]):
                    G[i][j]=G[i][k] + G[k][j]
    return G

def printHelp():
    print("Possible Commands are:")
    print("dijkstra x - Runs Dijkstra starting at node X. X must be an integer")
    print("floyd - Runs Floyd's algorithm")
    print("help - prints this menu")
    print("exit or ctrl-D - Exits the program")

def myGraph(f):
    try:
        graphFile=open(f,'r')
    except IOError:
        print("Invalid file name.\nExiting\n")
        exit(-1)
    else:
        global Graph
        global DistinctNodes
        numNodes=int(graphFile.readline())
        Graph=[[float("inf") for i in range(0, numNodes)] for j in range(0, numNodes)]
        DistinctNodes=[i for i in range(0, numNodes)]
        line=graphFile.readline()
        while line != "":
            fields=line.split(" ", line.count(" "))
            Graph[int(fields[0])][int(fields[1])]=float(fields[2])
            line=graphFile.readline()
    graphFile.close()

if __name__ == '__main__':
	f=""
	f=input("File containing graph: ")
	myGraph(f)
	printHelp()
	entry=""
	while entry!="exit":
		myGraph(f)
		entry=input("Enter command: ")
		if entry.find("floyd") != -1:
			myGraph(f)
			distances=floyd(Graph)
			for i in range(0, len(distances)):
				print(distances[i])
		elif entry.find("dijkstra") != -1:
			param=int(entry.split(" ", 2)[1])
			result=dijkstra(Graph, param)
			print(result)
		elif entry=="help":
			printHelp()
		elif entry=="exit":
			break
	print("Bye")
