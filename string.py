name = "sneha"
color = "red"
place = "cambridge"
pet = ""#called empty string 
print("name:" + name +",favourit color :" + color)
print("examples"*3)
print(len(name))
#---------string indexing------
name = "sneha"
name = "jaylen"
print(name[1])
#-------negative ndexing------
text = "random string with a lot of character "
print(text[-1])
print(text[-5])
#slice of a string : the slice of a striing thst can contain more than one character ; also sometimes called a substring.
color = "orange"
print(color[1:4])
print(color[0:4])
# string in python are imutable ---- 
# we can not change individaul character because string in python 
#it means it can not be modified 
message = "a kong string with a silly typo"
# message[2] = "l"--- it give us error because string are imutable

new_message = message[0:2]+"l"+message[3:]
print(new_message)
message = "i an a good girl"#now the message is this 
print(message)

##------ how to get index of certain character---
pets = "cats & dogs"
print(pets.index("&"))
print(pets.index("d"))
print(pets.index("s"))

#-- how can we know if a substring is contained in a string ti avod error----
print("dragons" in pets )
print("cats" in pets )
#real world program ---we want to write  a program that replaces this old domain with the new one in any out dated email address----
#domain name:An email domain is the part of an email address that comes after the @ symbol. For personal emails, it is most often gmail.com, outlook.com or yahoo.com.
 
def replace_domain(email,old_domain,new_domain):
    if "@"+ old_domain in email:
        index = email.index("@"+ old_domain)
        new_email = email[0:index]+"@"+new_domain
        return new_email
#---more string method-----
f ="Mountains".upper()
g ="Mountains".lower()
s = " yes ".strip()#strps removes spaces ,tabes and new line character 
print(s)
message="the number of times e occurs in this string is known"
print(message.count("e"))
print(message.endswith("known"))
print(message.isnumeric())
s =" ".join(["this","is","a","phase","joined","by","spaces"])
print(s)
t ="...".join(["this","is","a","phase","joined","by","spaces"])
print(t)
#------hoe format method works ----
name = "shobha"
number = len(name)*3
print("hello {} , your luckey number is {}".format(name,number))

#----------------------------
price = 7.5
with_tax = price*1.09
print(price,with_tax)
print("base price :${:.2f} .with tax :{:.2f}".format(price,with_tax))
#{:>3}  {:>6.2f}



