chai_variety = ['Black', 'Oolong', 'Lemon', 'Herbal']

chai_variety[0] #output: 'black'

chai_variety[1:2] #output: ['Oolong']

#for loop on list
for tea in chai_variety:
    print(tea)

#if condition on list
if "Oolong" in chai_variety:
    print("I have Oolong Tea") 

#addition of Element in last of list
chai_variety.append("Masala")
print(chai_variety)        #output: ['Black', 'Oolong', 'Lemon', 'Herbal', 'Masala']


#deletion of last Element in list
chai_variety.pop()
print(chai_variety)     #output: ['Black', 'Oolong', 'Lemon', 'Herbal']

#remove any element from list
chai_variety.remove("Lemon")
print(chai_variety)     #output:['Black', 'Oolong', 'Herbal']

#insert element at any position in list
chai_variety.insert(0, "Lemon")
print(chai_variety)     #output: ['Lemon', 'Black', 'Oolong', 'Herbal']

#copy the list in another variable without refrence
chai_variety_copy = chai_variety.copy()
print(chai_variety_copy)    #output: ['Lemon', 'Black', 'Oolong', 'Herbal'] 

count = range(10)
print(count)    #output: range(0, 10)  

#square the no. from 0 to 10
squared_num = [x**2 for x in range(10)]  
print(squared_num)    #output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]