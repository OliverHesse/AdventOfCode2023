#setting up all the maps that will be used
current_ids = []
new_ids = []
with open("test_input.txt", "r") as input_file:
  on_seed = True
  current_map_found = True
  for line in input_file:
    line = line.rstrip()

    if line == "":
      if on_seed:
        on_seed = False
      current_map_found = False

      print("enterd a new cpnversion")
      if current_ids != []:
        for id in current_ids:
          new_ids.append(id)

      current_ids = new_ids

      new_ids = []
      #new thingy encoutnerd
      continue
    if on_seed:
      ids = line.split(":")[1].strip().split(" ")
      current_ids = ids

      continue
    if current_map_found is False:
      current_map_found = True
      continue
    else:

      new_id_start, current_id_start, range_start = line.split(" ")
      current_id_start = int(current_id_start)
      new_id_start = int(new_id_start)
      range_start = int(range_start)
      print(current_ids)
      ids_to_remove = []
      for id in current_ids:
        curr_id = int(id)
        print(
            f"id {curr_id} in range {current_id_start} to {current_id_start+range_start} is { current_id_start <= curr_id and curr_id < current_id_start+range_start}"
        )
        if current_id_start <= curr_id and curr_id < current_id_start + range_start:
          print(id)
          ids_to_remove.append(id)
          new_ids.append(str(new_id_start + (curr_id - current_id_start)))
      for id in ids_to_remove:
        current_ids.remove(id)
new_ids += current_ids
print(new_ids)

for i in range(0, len(new_ids)):
  new_ids[i] = int(new_ids[i])
print(min(new_ids))
