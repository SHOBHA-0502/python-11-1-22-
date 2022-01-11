 #dictionary....
 #the data inside the dictionaries take the form of pairs of keys and values .
 # x = { }
 # print(type())
file_counts = {"jpg":10 ,"txt":14, "csv":2 ,"py":23}
print(file_counts)
 #==== dictionaries are mutable ++++++;;;;
file_counts["cfg"]=8
print(file_counts)
file_counts["cvc"]=17
print(file_counts)
 #---------------------------------------------
 #how to delete elements from a string 
del file_counts["cfg"]
print(file_counts)
 # ###++++++++++++++++++++++++++++++++
 # #itration over contents of dictionaries .
file_counts = {"jpg": 10 , "txt":14 , "csv":2 , "py":23}
for extentions in file_counts:
     print(extentions) # it will only return the keys 


#for finding the key and value pair like a tuples 
for ext,amount in file_counts.items():
     print("there are {}files with the .{} extention".format(amount , ext))
 #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print(file_counts.keys())
print(file_counts.values())
 #++++++++++++++++++++++++++++++++++++++++++++++++++
for value in file_counts.values():
     print(value)
 #++++++++++++++++++++++++++++++++++++++++++++++++++
 #------------HOW TO FIND THE FREQUENCY OF EZCH LETTERS IN A STRING --------------------------------
def count_letters(text):
     result = {}
     for letter in text:
         if letter not in result:
             result[letter]=0
         result[letter]+=1
     return result 
print(count_letters("my name is shobha kumari "))
# #=============================================================
# # you want to use dictionaries when you plan on searching for a specific element .
# #dictionary keys can be numbers, boolean,string , tuples



