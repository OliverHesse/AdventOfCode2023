#first im going to open the file and quickly read all the lines into an array. since im not sure how python opens files
file = []
with open("inputDay3.txt","r") as input_file:
    for line in input_file:
        file.append(line.rstrip())
#if a coordinate already has already been found out then it will be added to this
already_found_cords = {}


def get_num(line,current_x_pos,current_y_pos):
    start_found = False
    end_found = False
    current_num = line[current_x_pos]
    already_found_cords[f"{current_x_pos},{current_y_pos}"] = True
    start_pointer = current_x_pos - 1
    
    end_pointer = current_x_pos + 1
    
    print(f"{current_x_pos},{current_y_pos}")
    while start_found == False or end_found == False:
        
        if start_pointer < 0:
            #start of file reached
            start_found = True
        else:
            if line[start_pointer].isdigit() and  start_found == False:
            
                #current character is a digit. add it to start of current_num string
                current_num = line[start_pointer] + current_num
                already_found_cords[f"{start_pointer},{current_y_pos}"] = True
            else:
                #character is not a num. this means i have reached the start of the number
                start_found = True

        if end_pointer >= len(line):
            #end of file reached
            end_found = True
        else:
            if line[end_pointer].isdigit() and end_found == False:
                current_num += line[end_pointer]
                already_found_cords[f"{end_pointer},{current_y_pos}"] = True 
            else:
                end_found = True

        if start_found == False:
            start_pointer -=1
        if end_found == False:
            end_pointer +=1
    #now i should have the final number in string form
    #so an int cast should properly convert it.
    return int(current_num)

total = 0
for line_i in range(0,len(file)):
    for column_i in range(0,len(file[line_i])):
        #this loops through every character in the line.
        #i  want to check for any character that is not a . or a digit
        if file[line_i][column_i] != "." and file[line_i][column_i].isdigit() == False:
            #it is a special character
            #check all the indexes around this character
            #this double loop allows me to check all positions
            for x in range(-1,2):
                for y in range(-1,2):
                    #do some quick bound checks
                    if line_i+y > len(file) and line_i+y < 0:
                        #invalid coordinate move on
                        continue
                    if column_i+x > len(file[line_i]) and column_i+x <0:
                        #invalid coordinate move on
                        continue
                    #now i know that this will be a valid coordinate
                    # i just need to check if this coordinate is a valid coordinte
                    if file[line_i+y][column_i+x].isdigit() and f"{column_i+x},{line_i+y}" not in already_found_cords:
                        new_num = get_num(file[line_i+y],column_i+x,line_i+y)
                        total+=new_num

output_file = open("outputPar1.txt","w")
output_file.write(str(total))
output_file.close()             