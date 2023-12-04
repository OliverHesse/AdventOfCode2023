#first im going to open the file an loop through each card
#i will read the winning numbers into a hashmap. then check if the other numbers are in the hashmap
total = 0
card_data = {}
with open("inputDay4.txt") as input_file:
    for line in input_file:
        
        current_found = 0
        
        #get all the needed inputs
        card,inputs = line.rstrip().split(":")
        card_id = card.split(" ")[-1]
        if int(card_id) not in card_data:
            card_data[int(card_id)] = 1
        match_debug = ""
        winning_nums,my_nums = inputs.split("|")
        winning_nums = winning_nums.strip().replace("  ",",").replace(" ",",").split(",")
        my_nums = my_nums.strip().replace("  ",",").replace(" ",",").split(",")
        winning_map = {}
        for item in winning_nums:
            winning_map[item] = True
        for item in my_nums:
            if item in winning_map:
                #the number of copies i will need to make
                current_found += 1
                match_debug += item+","

        
        for i in range(1,current_found+1):
            if int(card_id)+i not in card_data:
                #two because i know i will encounter the card again
                card_data[int(card_id)+i] = 1+1*card_data[int(card_id)]
            else:
                card_data[int(card_id)+i] += card_data[int(card_id)]
        total += card_data[int(card_id)]
        print(f"card {int(card_id)} had {card_data[int(card_id)]} copies and has generated {current_found} new_cards these are {match_debug}")

output_file = open("outputPart2.txt","w")
output_file.write(str(total))
output_file.close()