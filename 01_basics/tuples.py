tea_types = ("Black", "Green", "Oolong")
"""A tuple of tea types."""
print(tea_types)

# Last element of the tuple
print(tea_types[-1])

# Tuples are immutable
# tea_types[0] = "Masala" # tuple object does not support item assignment

# Length of the tuple
print(len(tea_types))

more_tea = ("Herbal", "Ginger")
"""More tea types."""
all_tea = tea_types + more_tea
print(all_tea)

# Check if Green tea is available
if "Green" in all_tea:
    print("Green tea is available.")

more_tea = ("Herbal", "Earl Gray", "Herbal")
print(more_tea)

# Count the number of "Herbal" in the tuple
print(more_tea.count("Herbal"))

# Unpack the tuple into 3 variables
(black, green, oolong) = tea_types
print(black, green, oolong)

# Type of the tuple, which is a tuple.
print(type(tea_types))