animals = ["lions", "zebra","dolphin","monkey"]
chars =0
for animal in animals :
    chars +=len(animal)

print("total character: {},average length: {}".format(chars,chars/len(animals)))

#-----what is emnumarate function -------###

winners = ["ashley","dylan","reese"]
for index,person in enumerate(winners):
    print("{},<{}>".format(index,person))

#-----real world problem #-----------
def full_emails(people):
    result = []
    for email,name in people:
        result.append("{},<{}>".format(name,email))
    return result

print(full_emails([("alex@example.com","alex diago"),("shey@example.com","shay")]))
