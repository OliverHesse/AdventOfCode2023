#first im going to open the file an loop through each card
#i will read the winning numbers into a hashmap. then check if the other numbers are in the hashmap
total = 0
with open("inputDay4.txt") as input_file:
    for line in input_file:
        current_total = 0
        current_found = 0
        #get all the needed inputs
        card,inputs = line.rstrip().split(":")
        winning_nums,my_nums = inputs.split("|")
        winning_nums = winning_nums.strip().replace("  ",",").replace(" ",",").split(",")
        my_nums = my_nums.strip().replace("  ",",").replace(" ",",").split(",")
        winning_map = {}
        for item in winning_nums:
            winning_map[item] = True
        for item in my_nums:
            if item in winning_map:
                current_found += 1

                #this way i can do some cheese
                current_total = 1
        #very cheesy lol
        print(winning_nums)
        card_total = current_total * 2**(current_found-1)
        print(f"found {current_found} matches with a total of {card_total}")
        total += card_total
output_file = open("outputPart1.txt","w")
output_file.write(str(total))
output_file.close()