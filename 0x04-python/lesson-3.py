# Python lists
# 1. A list is an ordered collection of items
# 2. square brackets [] used to enclose items
# 3. and comma (,) is used to separate items in a list
# print("\n")

lab1 = ["Peter", "Ruto", "Riggy G", "Weta", "Joho 001"]
# print("List: ", lab1)

#  size of list
size = len(lab1)
# print(lab1[-1])

print(size)
# print("\n")

# Access each item in the list
#  using index (start counting from ZERO (0) index)
print(lab1[0])
print(lab1[1])
print(lab1[2])
print(lab1[3])
print(lab1[4])

# print("\n")
# print(lab1[-1])
# print(lab1[2:4])

# Append items in the list (add new)
print("\n")
lab1.append("steven")

# add johnson at index 3
lab1.insert(3, "Johnson")
print(lab1)

# print items from index 4
print(lab1[4:])

# items from index 4 and below
# NB:- There is a minus one (1)
print(lab1[:5])
print("\n")

# Slicing
# items from index 2 to 5
# NB:- it does not include the last index (5)
print(lab1[2:5])

