# Python dictionary
# - Is a unordered collection of key-value pairs

'''Key Characteristics of Dictionaries
Unordered: The items stored in a dictionary do not have a specific order. This means that when you iterate through a dictionary, the order of elements may not be the same as the order in which they were added.

Key-Value Pairs: Each entry in a dictionary consists of a key and its corresponding value. You can think of a dictionary as a collection of "lookups" where you can retrieve values based on their keys.

Mutable: Dictionaries can be changed after they are created. You can add, remove, or modify key-value pairs.
'''

# Example
person = {
    "firstName" : "Super",
    "lastName" : "Metro",
    "age" : 10,
    "model" : "PSV",
    "weight" : 1500
}
print(person)

# print('\n')
# k = person.get("firstName")
# n = person.get("age")
# j = person.get("model")
# print(k, n, j)

print('\n')
# print name
print(person["firstName"])

# print age
print(person["age"])
# print("age: ", person["age"])

# print model
print(person["model"])

# change age = 100
person["age"] = 100
print(person["age"])

# change fist name = Student
person["firstName"] = "Student"
print(person["firstName"])

print("\n")

# Mkenya dictionary
mkenya = {
    "firstname" : "John",
    "lastname" : "Doe",
    "age" : 21,
    "gender" : "male",
    "religion" :  "Muslim"
}
print(mkenya)