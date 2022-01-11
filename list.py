x = ["now", "we","are","friends"]
print(x)
print(len(x))#for how many elements are in the list
print("are"in x)
#----- slicing of list---------
print(x[1:3])
# list is different from the string because lists are mutable
#=== adding an element to list usng the append method 
fruits = ["pineapple", "banana","apple","melon"]
fruits.append("kivi")
print(fruits)

#-- the insert method takes index as the fiirst parameter and an elment as a second parameter 
#it adds the element at that index in the list

fruits.insert(0,"orange")
fruits.insert(35,"orange") #if we use an index higher than the current length,the element just get added to the end of rhe list
fruits.remove("melon")
fruits.pop(3)# the pop method returns the element that wasremoed at the index that was passed
fruits[2]="straberry"
print(fruits)

