# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter the pet species: ").lower()
age = int(input("Enter the pet age: "))

if species == "dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"
elif species == "cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Cat food"
else:
    food = "No information available"

print(food)