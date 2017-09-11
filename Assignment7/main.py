#!/usr/bin/env python3

nodes=None
G=[[None]]

def Graph(f):
    try:
        file=open(f,'r')
    except IOError:
        print("Could not find file. Exiting.")
        exit(-1)
    else:
        global G
        global nodes
        node_count=int(file.readline())
    G=[[float("inf") for i in range(0, node_count)] for j in range(0, node_count)]
    nodes=[i for i in range(0, node_count)]
    edge=file.readline()
    while edge != "":
        nums=edge.split(" ", edge.count(" "))
        G[int(nums[0])][int(nums[1])]=float(nums[2])
        edge=file.readline()
    file.close()

def prim(G, start_node):
    global nodes
    dist=[float("inf") for i in range(0,len(G))]
    dist[start_node]=0
    node_list=nodes
    node_list.remove(start_node)
    node_count=len(node_list);
    end=start_node
    while len(node_list) > 0:
        min_weight=float("inf")
        add_node=-1
        smallI=-1
        smallJ=-1
        for i in range(0,len(G)):
            for j in range(0,len(G)):
                if i not in node_list or j in node_list:
                    continue
                if G[j][i] < min_weight:
                    min_weight=G[j][i]
                    add_node=i
                    min_i=j
                    min_j=i
                if G[i][j] < min_weight:
                    min_weight=G[i][j]
                    add_node=i
                    min_i=i
                    min_j=j
        if min_weight == float("inf"):
            break
        G[min_i][min_j]=float("inf")
        G[min_j][min_i]=float("inf")
        print("Added " + str(add_node))
        print("Using Edge ["+str(min_i)+","+str(min_j)+","+str(min_weight)+"]")
        node_list.remove(add_node)
        end=min_i

def kruskal(G):
    global nodes
    dist=[float("inf") for i in range(0, len(G))]
    node_list=nodes
    node_count=len(node_list);
    edge_list=None
    while len(node_list) > 0:
        min_weight=float("inf")
        add_node=-1
        smallI=-1
        smallJ=-1
        for i in range(0, node_count):
            for j in range(0, node_count):
                if j not in node_list and i not in node_list:
                    continue
                if G[j][i] < min_weight:
                    min_weight=G[j][i]
                    add_node=i
                    min_i=j
                    min_j=i
                if G[i][j] < min_weight:
                    min_weight=G[i][j]
                    add_node=i
                    min_i=i
                    min_j=j
        if min_weight == float("inf"):
            break
        G[min_i][min_j]=float("inf")
        G[min_j][min_i]=float("inf")
        if edge_list is None or not (min_i in edge_list[0] and min_j in edge_list[0]):
            print("Select Edge ["+str(min_i)+","+str(min_j)+","+str(min_weight)+"]")

        if edge_list is None:
            edge_list=[[min_i, min_j]]
        else:
            edge_list.append([min_i, min_j])

        end=len(edge_list) - 1
        for i in range(len(edge_list) - 1, 0, -1):
            if (min_i in edge_list[i - 1] or min_j in edge_list[i - 1]) and (
                    min_i in edge_list[end] or min_j in edge_list[end]):
                for node in edge_list[end]:
                    edge_list[i - 1].append(node)
                edge_list.remove(edge_list[end])
                end=i - 1
        count=0
        for i in range(0, node_count):
            if i in edge_list[0]:
                count += 1
        if len(edge_list) == 1 and count >= node_count:
            break

def help():
	print("Commands:")
	print("exit or ctrl-d - quits the program")
	print("help - prints this menu")
	print("prim <integer_value> - runs Prim's algorithm starting at node given")
	print("kruskal - runs Kruskal's algorithm")

if __name__=='__main__':
	print("Welcome to Minimum Spanning Tree Finder")
	f=input("Give the file name graph is in: ")
	help()
	entry=""
	while entry!="exit":
		Graph(f)
		entry=input("Enter command: ")
		if entry.find("prim")!=-1:
			start_node=int(entry.split(" ", 2)[1])
			prim(G, start_node)
		elif entry.find("kruskal")!=-1:
			print("Running Kruskal's Algorithm")
			kruskal(G)
		elif entry=="help":
			help()
		elif entry=="exit":
			break
		else:
			print("Invalid input, please review list of commands below.")
			help()
	print("Bye")
