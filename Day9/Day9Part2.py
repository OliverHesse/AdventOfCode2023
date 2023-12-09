#was ill today so no comments and bad variable names
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
    print("==Extrapolating Data==")
    for diff in all_thing:
        print("==Current Extrapolation==")
        reversed_diff = diff[::-1]
        print(reversed_diff)
        for i in range(0,len(reversed_diff)-1):
            if i == 0:
                reversed_diff[i].insert(0,0)
            else:
                
                reversed_diff[i].insert(0,reversed_diff[i][0]-reversed_diff[i-1][0])
        new_val = int(reversed_diff[-1][0])-(reversed_diff[-2][0])
        total += new_val
        print(f"extrapolated val = {new_val}")
    print(total)
                