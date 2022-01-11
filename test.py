# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = [files.replace(".hpp",".hp") for files in filenames ]

# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# def pig_latin(text):
#   say = "ay"
#   text = text.split()
#   # Separate the text into words
#   new_text=[word[1:]+word[0]+ say  for word in text]
#   s = " ".join(new_text)
#     # Create the pig latin word and add it to the list
#   return s
#     # Turn the list back into a phrase
  
		
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# 

# def group_list(group, users):
#   s = ", ".join(users)

    

#   members = group+ ":"+ s
#   return members

# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# 

def guest_list(guests):
	for elements in guests:
		
		print("{} is {} years old and work as a {} ".format(elements[0],elements[1],elements[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""