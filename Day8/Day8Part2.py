import time
with open("InputDay8.txt","r") as input_file:
    count = 0
    directions = ""
    nodes = {}
    start_directions = []
    for line in input_file:
        line = line.strip()
        if count == 0:
            #read in the direction instructions
            directions = line
            print(directions)
        if line != "" and count > 0:
            #this is a node 
            node,children = line.split(" = ")
            if node[-1] == "A":
                start_directions.append(node)
            children = children[1:len(children)-1].split(", ")
            
            print("==New Node==")
            print(f"parent node of {node}")
            print(f"left node of {children[0]}, right node of {children[1]}")
            print("==End of Node==")
            nodes[node] = {"L":children[0],"R":children[1]}
        count += 1
    reached_end = False
    current_nodes = start_directions
    print(current_nodes)
    print("==Now Searching==")
    nodes_traveled = 0
    listt = []
    for node in current_nodes:
        c_node = node
        nodes_traveled = 0
        reached_end = False
        while reached_end == False:

            for direction in directions:
                nodes_traveled += 1
                c_node = nodes[c_node][direction]
                if c_node[-1] == "Z":
                    reached_end = True
                    break
        listt.append(nodes_traveled)
        print(nodes_traveled)
    nodes_traveled = 0
    print(listt)

    print("==Finished Traveling==")
    print(f"arrived at node {current_nodes}")
    print(f"it took {nodes_traveled}")