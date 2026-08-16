my_dict = {
    "name": "Piyush",
    "roll_no": "1024170406",
    "branch": "CSE",
    "age": 20,
    "city": "Patiala"
}

#Rename "city" to "location" using pop()
my_dict["location"] = my_dict.pop("city")
print("After renaming city:", my_dict)

#Add CGPA
my_dict["cgpa"] = 9.10
print("After adding CGPA:", my_dict)

#Increase age by 1
my_dict["age"] += 1
print("After updating age:", my_dict)

#Delete "branch" using pop() and del in separate copies
dict_pop = my_dict.copy()
removed_value = dict_pop.pop("branch")

dict_del = my_dict.copy()
del dict_del["branch"]

print("Using pop():", dict_pop)
print("Value returned by pop():", removed_value)
print("Using del:", dict_del)

# pop() removes and returns the value, while del removes the key-value pair
# without returning the removed value.

#Iterate using .items()
for key, value in my_dict.items():
    print(f"{key} → {value}")

#Safely check for "email"
if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email not found.")

#Create friend's dictionary
friend_dict = {
    "name": "Rahul",
    "roll_no": "FRIEND_ROLL_NUMBER",
    "branch": "ECE",
    "age": 19,
    "city": "Delhi"
}

merged_dict = {**my_dict, **friend_dict}
print("Merged dictionary:", merged_dict)

# When both dictionaries have the same key, values from the second dictionary win.

#  Dictionary comprehension for string values only
string_values_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("Dictionary containing only string values:", string_values_dict)