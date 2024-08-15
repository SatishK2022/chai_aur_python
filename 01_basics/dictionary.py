chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Refreshing"}

# Accessing values from dictionary
print(chai_types["Masala"])  # Spicy
print(chai_types.get("Masala"))  # Spicy
print(chai_types.get("Gingerr"))  # None
print(chai_types["Masala"])

# Updating values in dictionary
print(chai_types.get("Masala"))

print(chai_types.get("Gingerr")) # None
# print(chai_types["Gingerr"]) # KeyError: 'Gingerr'

chai_types["Green"] = "Fresh"
print(chai_types)

# Iterating over dictionary keys and values
for chai in chai_types:
    print(chai, chai_types[chai])

# Iterating over dictionary keys and values using items()
# Works only in dictionary
for key, value in chai_types.items():
    print(key, value)

# Checking if a key exists in dictionary
if "Masala" in chai_types:
    print("I have masala chai")

# Getting the length of dictionary
print(len(chai_types))

# Adding new key-value pair to dictionary
chai_types["Earl Gray"] = "Citrus"
print(chai_types)

# Removing a key-value pair from dictionary using pop()
chai_types.pop("Green")
print(chai_types)

# Removing the last key-value pair from dictionary using popitem()
chai_types.popitem()
print(chai_types)

# Removing a key-value pair from dictionary using del
del chai_types["Ginger"]
print(chai_types)

# Creating a copy of a dictionary
chai_types_copy = chai_types.copy()

# Creating a nested dictionary
tea_shop = {
    "chai": {
        "Masala": "Spicy",
        "Ginger": "Zesty"
    },
    "tea": {
        "Green": "Fresh",
        "Black": "Strong"
    }
}
print(tea_shop["chai"]["Ginger"])  # Zesty
print(tea_shop["chai"]["Ginger"])

# Creating a dictionary using dictionary comprehension

squared_num = {x: x**2 for x in range(6)}
print(squared_num)

# Clearing a dictionary
squared_num.clear()

# Creating a dictionary with default values for keys
keys = ["Masala", "Ginger", "lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)