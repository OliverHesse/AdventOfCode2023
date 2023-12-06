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
    data = data.strip().replace(" ","")
    new_data = []
    current_num = ""
    split_data[d_type] = int(data)
print(split_data)
#doing a bit of rearanging i should get the equatiipn
#ct = (Tt/2) +or- sqrt((Tt/2)**2-d)
#where ct = charge_time Tt = Total_time d = distance
#so lets try it out
range_sum = 1

print("==new race==")
Tt = float(split_data["Time"])
d = float(split_data["Distance"])

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