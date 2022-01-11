animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
#=================================================================================
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
#=================================================================================
host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())
#=================================================================================
def format_address(address_string):
  t = address_string.split()
  k = " ".join(t[1:])
  
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(t[0],k)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
#======================================================================================
def squares(start, end):
	t =[n*n for n in range(start ,end+1)]
	return t

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#=======================================================================================
def car_listing(car_prices):
  result = ""
  for element in car_prices:
    
    result += ("{} costs {} dollars").format(element,car_prices[element]) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
#========================================================================================================================
def count_letters(text):
  text = text.lower()
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter not in result:
      
        result[letter]=0
        result[letter]+=1

  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
#=======================================================================================
def combine_lists(list1, list2):
    list1 = list1[::-1]
    list2 = list2 +list1
    return list2


   
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#=================================================================================================
