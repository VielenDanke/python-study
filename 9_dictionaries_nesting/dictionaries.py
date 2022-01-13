# create dictionary
programming_dictionary = {
    "Bug": "An error in program that prevents program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# create empty dictionary
empty_dictionary = {}

# all
print(programming_dictionary)

# retrieving value using key
print(programming_dictionary["Bug"])

# add/edit items
programming_dictionary["Loop"] = "The action of doing something over and over again"

# loop through a dictionary
for key in programming_dictionary:
    print(f"Key: {key}. Value: {programming_dictionary[key]}")

# wipe an existing dictionary
programming_dictionary = {}

print(programming_dictionary)
print(len(programming_dictionary))
