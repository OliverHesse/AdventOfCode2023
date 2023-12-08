with open("test_input3.txt","r") as input_file:
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
    nodes_traveled = 0
    while reached_end == False:
        for direction in directions:
            z_found = 0
            for i in range(0,len(current_nodes)):
                current_nodes[i] = nodes[current_nodes[i]][direction]
                if current_nodes[i][-1] == "Z":
                    z_found += 1
            nodes_traveled +=1
            if z_found == len(current_nodes):
                break
            

    print("==Finished Traveling==")
    print(f"arrived at node {current_node}")
    print(f"it took {nodes_traveled}")