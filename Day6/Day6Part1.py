#im going to try and use the equation
#charge_time(Total_time-charge_time) = distance
#to do some quirky stuff
import math

split_data = {}
with open("input.txt", "r") as input_file:
  for line in input_file:
    line = line.rstrip()
    d_type, data = line.split(":")
    finding_num = False
    data = data.strip()
    new_data = []
    current_num = ""
    for ch in data:

      if ch.isdigit() and finding_num:
        current_num += ch
      elif ch.isdigit() and finding_num is False:
        current_num = ch
        finding_num = True
      if ch == " " and finding_num:
        finding_num = False
        new_data.append(int(current_num))
    new_data.append(int(current_num))
    print(new_data)
    split_data[d_type] = new_data
print(split_data)
#doing a bit of rearanging i should get the equatiipn
#ct = (Tt/2) +or- sqrt((Tt/2)**2-d)
#where ct = charge_time Tt = Total_time d = distance
#so lets try it out
range_sum = 1
for i in range(0,len(split_data["Time"])):
  print("==new race==")
  Tt = float(split_data["Time"][i])
  d = float(split_data["Distance"][i])
  
  ct1 = (Tt / 2) + math.sqrt((Tt/2)**2 - d)
  ct2 = (Tt / 2) - math.sqrt((Tt/2)**2 - d)
  if ct1.is_integer():
    ct1 -= 1
  if ct2.is_integer():
    ct2 += 1
  max_charge_time = math.floor(ct1)
  min_charge_time = math.ceil(ct2)
  range_sum *= (max_charge_time+1-min_charge_time)
  new_range = range(min_charge_time,max_charge_time+1)
  print(f"values of {new_range}")
  print(f"there are {max_charge_time+1-min_charge_time} values")
print("==output==")
print(range_sum)