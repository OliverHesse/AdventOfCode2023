#map that contains all of a pipes moves
#cords are in the format [x,y]
#remember up is -
pipe_to_move = {
    "-" : [[-1,0],[1,0]],
    "|" : [[0,1],[0,-1]],
    "7" : [[0,1],[-1,0]],
    "L" : [[0,-1],[1,0]],
    "J" : [[0,-1],[-1,0]],
    "F" : [[0,1],[1,0]],
    "." : [[0,0]]
}
#if i were to move into the pipe what would my direction be
move_to_pipe = {
    "0,1" : {"|":None,"L":None,"J":None},
    "0,-1": {"|":None,"7":None,"F":None},
    "-1,0":{"-":None,"L":None,"F":None},
    "1,0":{"-":None,"7":None,"J":None}
}

def get_next(pos):
    
    current_pipe = pipe_map[pos["y"]][pos["x"]]

    for move in pipe_to_move[current_pipe]:
        new_x = pos["x"] + move[0]
        new_y = pos["y"] + move[1]
       
        if str(new_x)+","+str(new_y) not in already_traveled:
            #have not visited this node before.
            new_pos = {"x":new_x,"y":new_y}
            
            return new_pos
    
    print("oop")


with open("inputDay10.txt","r") as input_file:
    pipe_map = []
    start_position = {"x":None,"y":None}
    #read it into an array so i can jump between lines easily
    #also look for S pos
    line_count = 0
    for line in input_file:
        pipe_map.append(line.strip())
        s_pos = line.strip().find("S")
        if s_pos != -1:
            start_position = {"x":s_pos,"y":line_count}
        line_count += 1
    print(start_position)
    pos1 = {}
    pos2 = {}
    new_directions = []
    already_traveled = {}
    already_traveled[str(start_position["x"])+","+str(start_position["y"])] = None
    #find the 2 starting directions
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    for dir in directions:
        #some bounds check
        if start_position["x"] + dir[0] > len(pipe_map[0])-1 or start_position["x"] +dir[0] < 0:
            continue
        if start_position["y"] + dir[1] > len(pipe_map)-1 or start_position["y"] +dir[1] < 0:
            continue
        ch = pipe_map[start_position["y"]+dir[1]][start_position["x"]+dir[0]]
        
        if ch in move_to_pipe[str(dir[0])+","+str(dir[1])]:
            #valid pipe
            new_directions.append({"x":start_position["x"]+dir[0],"y":start_position["y"]+dir[1]})
    pos1 = new_directions[0]
    pos2 = new_directions[1]
    distance = 1    
    
    while pos1 != pos2:
        #first do pos1
        already_traveled[str(pos1["x"])+","+str(pos1["y"])] = None
        already_traveled[str(pos2["x"])+","+str(pos2["y"])] = None
        pos1 = get_next(pos1)
        pos2 = get_next(pos2)
        distance += 1
        #print("==new_iteration==")
        #print(f"pos1 traveled to {pos1}")
        #print(f"pos2 traveled to {pos2}")
        
        #print(already_traveled)
        #then pos2
    print("not an endless loop")
    print(distance)