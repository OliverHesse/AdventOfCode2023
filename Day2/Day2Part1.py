# first i want to properly parse the data
#i will parse it into a multilayer dictionary
#first key will be The game and contain an array of rounds. each round contains a hash of the color and the occurance amount of it
sorting_dic = {}


max_of_each = {
    "green":13,
    "red":12,
    "blue":14
}

with open("inputDay2.txt","r") as input_file:
    for line in input_file:
        #first i want to find the id of the game
        game_id,game_data = line.split(":")
        #this can be further refined by  removing Game# where # is whitespace and then converting to an int
        game_id = int(game_id.replace("Game ",""))
        #create a new array in dic with key game id
        sorting_dic[game_id] = []

        #now we want to seperate the game into individual rounds. this can be done by splitting by ;
        rounds = game_data.split(";")
        for round in rounds:
            curr_round_colour_count = {
                "red":0,
                "green":0,
                "blue":0
            }
            #here we need to find a way to split it into red blue and green
            #from looking at the input data it seems they are split by commas with integer first followed by whitespace and then the colour
            #so first i seperate colours by , and then each color by whitespace
            colours = round.split(",")
            for each in colours:
                number,colour = each.strip().split(" ")
                curr_round_colour_count[colour] += int(number)
            sorting_dic[game_id].append(curr_round_colour_count)
        #this should give me all the colours split
#now i can check if each game is valid or not
#here i will have a game id total
game_id_total = 0
#it will only be increased if by the end of the current game, valid_game is still true
for game in sorting_dic:
    valid_game = True
    for round in sorting_dic[game]:
        for colour in max_of_each:
            #checks the amount of that colour in the round against the max in the bag
            if round[colour] > max_of_each[colour]:
                valid_game = False
                break
        if valid_game == False:
            #so i dont pointlesly loop. could have used a while loop instead but meh dont care enough
            break
    if valid_game !=False:
        #game is still valid so add id to total
        game_id_total += game      
#creates an output file to store the data   
output_file = open("outputPart1.txt","w")
output_file.write(str(game_id_total))
output_file.close()