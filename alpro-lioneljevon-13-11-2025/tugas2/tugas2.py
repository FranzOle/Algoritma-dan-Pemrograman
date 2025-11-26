list1 = [1, 2, 2, 3, 4]
set2 = {10, 20, 20, 30}
tuple1 = ("L", "i", "o", "n", "e", "l")
set1 = {7, 8, 9}

print("List :", list1)
list_to_set = set(list1)

print("List -> Set :", list_to_set)

print("Set :", set2)
set_to_list = list(set2)
print("Set -> List :", set_to_list)

print("Tuple :", tuple1)
tuple_to_set = set(tuple1)

print("Tuple -> Set :", tuple_to_set)

print("Set:", set1)

set_to_tuple = tuple(set1)
print("Set -> Tuple :", set_to_tuple)
