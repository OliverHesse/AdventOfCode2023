#stores the first character and len of word
character_len_map ={
    "o":[3],
    "t":[3,5],
    "f":[4,4],
    "s":[3,5],
    "e":[5],
    "n":[4]

}
#second one stores the last character and len of word
character_len_map2 = {
    "e":[3,4,4,5],
    "o":[3],
    "r":[4],
    "x":[3],
    "t":[5],
    "n":[5]
}

#word -> num recognition map
rec_map = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}
#that is all the setup i need

with open("input.txt","r") as input_file:
    
    file_total = 0
    current_line = 0
    for active_line in input_file:
        current_line +=1
        line = active_line.rstrip()
        start_pointer = 0
        end_pointer = len(line)-1
        
        start_digit_found = False
        end_digit_found = False
        digit1 = 0
        digit2 = 0
        print(f"new line({current_line}) with length{len(line)}:")
        while start_digit_found == False or end_digit_found == False:
            
            if start_pointer > len(line)-1:
                raise Exception("end of line something went wrong")
            if end_pointer < 0:
                raise Exception("start of file reached something went wrong")
            
            #first ill check the character, make sure im not repeaing anything
            if line[start_pointer] in character_len_map and start_digit_found == False:
                #loop through all the lengths and check that one dont go out of bounds
                #and two if they exist in the
                for length in character_len_map[line[start_pointer]]:
                    
                    if start_pointer+length > len(line):
                        continue
                    
                    if line[start_pointer:start_pointer+length] in rec_map and start_digit_found == False:
                        
                        digit1 = rec_map[line[start_pointer:start_pointer+length]]
                        start_digit_found = True
                        break
                
            #now i will do the same for the end character
         
            if line[end_pointer] in character_len_map2 and end_digit_found == False:
                #near replica of previous loop
                
                for length in character_len_map2[line[end_pointer]]:
                    if end_pointer-length < 0:
                        continue
                    
                    if line[end_pointer-length+1:end_pointer+1] in rec_map and end_digit_found == False:
                        digit2 = rec_map[line[end_pointer-length+1:end_pointer+1]]
                        end_digit_found = True
                        break
            
            #rest of code is replica of previous part
            if line[start_pointer].isdigit() and start_digit_found == False:
                
                digit1 = int(line[start_pointer])
                start_digit_found = True
   
            if line[end_pointer].isdigit() and end_digit_found == False:
                digit2 = int(line[end_pointer])
                
                end_digit_found = True
 

            #slight alteration
            if end_digit_found != True:
                end_pointer -=1
            if start_digit_found != True:
                start_pointer +=1
        
        #now add to file_total
           
        print(f"final digits are: {digit1},{digit2}")
        file_total += digit1*10+digit2
      
    output_file = open("outputDay1Part2.txt","w")
    output_file.write(str(file_total))
