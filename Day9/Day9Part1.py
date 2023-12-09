with open("inputDay9.txt","r") as input_file:
    all_thing = []
    for line in input_file:
        numbers = line.strip().split(" ")
        end_found = False
        diff = []
        diff.append(numbers)
        print(f"==for line {numbers} i have found these") 
        while end_found == False:
            new_list= []
            zero_found = 0
            for i in range(1,len(diff[-1])):
                difference = int(diff[-1][i])-int(diff[-1][i-1])
                if difference == 0:
                    zero_found += 1
                new_list.append(difference)
            if zero_found == len(diff[-1])-1:
                end_found = True
           
            diff.append(new_list)
        print(diff)
        all_thing.append(diff)
    total = 0
    for diff in all_thing:
        new_item = 0
        for item in diff:
            new_item += int(item[-1])
        total += new_item
    print(total)
                