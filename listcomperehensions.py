multiples =[]
for x  in range(1,11):
    multiples.append(x*7)
print(multiples)
#-------------------------------------------------
multiples = [x*7 for x in range(1,11)]
print(multiples)
# list comprehensions let us creat new list based on sequences or rnges 
languages = ["python", "perl","ruby","go","java","c"]
length = [ len(language) for language in languages]
print(length)
z =[x for x in range (0,101) if x%3 ==0]
print(z)
