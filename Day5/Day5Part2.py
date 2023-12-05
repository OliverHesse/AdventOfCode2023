#setting up all the maps that will be used
source_nums = []
destination_nums = []


def range_intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


with open("input.txt", "r") as input_file:
    seeds_found = False
    new_conversion_reached = False

    for line in input_file:
        line = line.rstrip()
        remove_from_source = []
        add_to_source = []
        if line == "":
            print("--------------------------------------------------------------------")
            print("entering new conversion block")
            seeds_found = True
            if source_nums != []:
                for source in source_nums:
                    destination_nums.append(source)
            source_nums = destination_nums
            destination_nums = []
            new_conversion_reached = True
            print(source_nums)
            continue
        if seeds_found != True:
            data = line.split(":")[1].strip().split(" ")
            #now i need to pair up the data
            for i in range(0, len(data), 2):
                source_nums.append({
                    "start": int(data[i]),
                    "end": int(data[i]) + int(data[i + 1]) - 1
                })
            print(source_nums)
        if new_conversion_reached:
            new_conversion_reached = False
            continue
        elif new_conversion_reached == False and seeds_found == True:
            mapped_destination_start, mapped_source_start, mapped_range = line.split(
                " ")
            mapped_destination_start = int(mapped_destination_start)
            mapped_source_start = int(mapped_source_start)
            mapped_range = int(mapped_range)
            mapped_destination_end = mapped_destination_start + mapped_range - 1
            mapped_source_end = mapped_source_start + mapped_range - 1
            #print(
        #         f"source start {mapped_source_start}, source end {mapped_source_end}"
        #     )
            #print(
        #       f"destination start {mapped_destination_start},dest end {mapped_destination_end}"
        #    )
            for source in source_nums:
                new_range = range_intersect(
                range(mapped_source_start, mapped_source_end + 1),
                range(source["start"], source["end"] + 1))
                if new_range is not None:
                    #i have a valid overlap
                    if new_range.start > source["start"]:
                        new_source = {"start": source["start"], "end": new_range.start - 1}
                        add_to_source.append(new_source)
                    elif new_range.stop - 1 < source["end"]:
                        new_source = {"start": new_range.stop, "end": source["end"]}
                        add_to_source.append(new_source)
                    
                    dest_start = (new_range.start - mapped_source_start) + mapped_destination_start
                    dest_end = (new_range.stop-new_range.start) + dest_start -1
                    destination_nums.append({"start": dest_start, "end": dest_end})
                    print("__")
                    print(f"four a source of {source} against a mapping of {mapped_source_start},{mapped_source_end} a range of new range  of 'start': {new_range.start}, 'end': {new_range.stop - 1}")
                    print(f"after mapping against destination start of {mapped_destination_start} i get 'start' : {dest_start},'end' : {dest_end}")
                    print("__")
                    remove_from_source.append(source)
                    
            for old_source in remove_from_source:
                
                source_nums.remove(old_source)
            for new_source in add_to_source:
                source_nums.append(new_source)
print("final output")
print(source_nums)
running_lowest = 0

for i in range(0,len(source_nums)):
    if i == 0:
        running_lowest = source_nums[i]["start"]
    else: 
        if source_nums[i]["start"] < running_lowest:
            running_lowest = source_nums[i]["start"]
print(running_lowest)
    
