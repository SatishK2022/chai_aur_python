chai = "Masala Chai"
first_char = chai[0]
print(first_char) #output: M

slice_chai = chai[0:6]
print(slice_chai) #output: Masala

print(chai.upper()) #output:MASALA_CHAI
hello = "   hello    "
print(hello.strip()) #output:hello 

tea = "Ginger Tea"
print(tea.replace("Ginger", "Lemon")) #output:Lemon Tea 

animal = "satish, piyush, upendra, ravi"
print(animal.split(", "))  #output: ['satish', 'piyush', 'upendra', 'ravi']

chaiCount = "chai chai chai chai"
print(chaiCount.count("chai")) #output: 4 if output is -1 means the finding string is not present.

chai_type = "Masala"
quantity = 2
order = "i ordered {} cups of {} chai"

print(order.format(quantity, chai_type))  #output: i ordered 2 cups of Masala chai

#list to string
chai_variety = ["Lemon", "Masala", "Ginger"]
print(" ".join(chai_variety))    #output: Lemon Masala Ginger   

coffee = r"colf\ncoffee"  #output: colf\ncoffee   diplays the row string presented in r"".