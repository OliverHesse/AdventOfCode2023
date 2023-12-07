end_dic = {
"five_of_a_kind" : [],
"four_of_a_kind" : [],
"full_house" :[],
"three_of_a_kind": [],
"two_pair" : [],
"one_pair": [],
"high_card" : []
}
#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
card_power_map = {
  "A":13,
  "K":12,
  "Q":11,
  "J":1,
  "T":10,
  "9":9,
  "8":8,
  "7":7,
  "6":6,
  "5":5,
  "4":4,
  "3":3,
  "2":2,
}
def insert_into_dic(active_array,hand,bid):
  print(f"==inserting {hand}==")

  for i in range(0,len(end_dic[active_array])):
    item = end_dic[active_array][i][0]
    print(f"--against {item}--")

    for x in range(0,5):

      if card_power_map[hand[x]] > card_power_map[item[x]]:

        end_dic[active_array].insert(i,[hand,bid])

        return
      if card_power_map[hand[x]] < card_power_map[item[x]]:
        break
  end_dic[active_array].append([hand,bid])


with open("input.txt", "r") as input_file:
  hands_and_bids_orderd = []
  #going to use insertion sort since i can order the inputs as i receive them
  for line in input_file:

    line = line.strip()
    hand, bid = line.split(" ")
    bid = int(bid)
    hand_card_map = {}
    wild_cards = 0
    for ch in hand:
      if ch =="J":
        wild_cards+=1
        continue
      if ch in hand_card_map:
        hand_card_map[ch] += 1
      else:
        hand_card_map[ch] = 1

    #convert hand to an orderd array
    orderd_composition_array = []
    for key, val in hand_card_map.items():

      orderd_composition_array.append(val)

    orderd_composition_array.sort()
    print(hand)
    print(orderd_composition_array)
    
    if orderd_composition_array != []:
      orderd_composition_array[-1]+= wild_cards
    else:
      orderd_composition_array = [wild_cards]
  
    key_string = ''.join(str(x) for x in orderd_composition_array[::-1])

    #lower score is better. the idea is to read all the cards into an array, order then abd then conver tot a string
    orderd_composition_map = {
        "5": 0,
        "41": 1,
        "32": 2,
        "311": 3,
        "221": 4,
        "2111": 5,
        "11111": 6,
    }

    active_array = ""
    match orderd_composition_map[key_string]:
      case 0:
        active_array = "five_of_a_kind"
      case 1:
        active_array = "four_of_a_kind"
      case 2:
        active_array = "full_house"
      case 3:
        active_array = "three_of_a_kind"
      case 4:
        active_array = "two_pair"
      case 5:
        active_array = "one_pair"
      case 6:
        active_array = "high_card"
    if end_dic[active_array] != []:
      insert_into_dic(active_array,hand,bid)


    else:
      end_dic[active_array].append([hand,bid])
new_array = end_dic["five_of_a_kind"]+end_dic["four_of_a_kind"]+end_dic["full_house"]+end_dic["three_of_a_kind"]+end_dic["two_pair"]+end_dic["one_pair"]+end_dic["high_card"]
power = 0
print(new_array)
for i in range(0,len(new_array)):
  print(f"a hand of {new_array[i][0]} with a bid of {new_array[i][1]} got a rank of {len(new_array)-i}")
  print(power)
  power += new_array[i][1]*(len(new_array)-i)
print(power)