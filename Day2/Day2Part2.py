#this one looks like it will be a bit different but i can refactor the code in a way that works.
#instead of each game storing all the rounds it will only store the max of each colour
sorting_dic = {}
total_power = 0
with open("inputDay2.txt","r") as input_file:
    for line in input_file:
        #first i want to find the id of the game
        game_id,game_data = line.split(":")
        #this can be further refined by  removing Game# where # is whitespace and then converting to an int
        game_id = int(game_id.replace("Game ",""))
        #create a new array in dic with key game id
        sorting_dic[game_id] = []
        curr_game_max_colour = {
                    "red":0,
                    "green":0,
                    "blue":0,
                    "Power":0
                }
        #now we want to seperate the game into individual rounds. this can be done by splitting by ;
        rounds = game_data.split(";")
        for round in rounds:
            #here we need to find a way to split it into red blue and green
            #from looking at the input data it seems they are split by commas with integer first followed by whitespace and then the colour
            #so first i seperate colours by , and then each color by whitespace
            colours = round.split(",")
            for each in colours:
                number,colour = each.strip().split(" ")
                #here i will compare the value of the colour to the one stored in the curr_game_max_colour.
                #which ever is bigger goes into the dic
                
                if int(number) > curr_game_max_colour[colour]:
                    curr_game_max_colour[colour] = int(number)
        #here i will quickly calculate the power
        #might cause an issue if on of them is zero
        curr_game_max_colour["Power"] = curr_game_max_colour["red"]*curr_game_max_colour["green"]*curr_game_max_colour["blue"]
        total_power += curr_game_max_colour["Power"]
        sorting_dic[game_id].append(curr_game_max_colour)
        #this should give me all the colours split
output_file = open("outputPart2.txt","w")
output_file.write(str(total_power))
output_file.close()