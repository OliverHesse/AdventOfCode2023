
with open("input.txt","r") as input_file:
    file_total = 0
    for line in input_file:
        first_digit = 0
        second_digit = 0

        start_found = False
        end_found = False

        start_pointer = 0
        end_pointer = len(line)-1
        while start_found == False or end_found == False:
            
            #some basic error checking
            if start_pointer > len(line):
                raise Exception("reached end of file without finding an int error encounterd")
            if end_pointer < 0:
                raise Exception("reached start of line without finding an int error encounterd")
            if line[start_pointer].isdigit() and start_found == False:
                
                first_digit = int(line[start_pointer])
                start_found = True
            else:
                start_pointer += 1
            if line[end_pointer].isdigit() and end_found == False:
                second_digit = int(line[end_pointer])
                
                end_found = True
            else:
                end_pointer -= 1
        
        print(first_digit*10+second_digit)
        file_total+=(first_digit*10+second_digit)
    #create an output file
    output = open("outputDay1Part1.txt","w")
    output.write(str(file_total))