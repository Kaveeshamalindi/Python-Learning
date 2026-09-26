animals = ["lion", "Zebra", "Dolphin", "Monkey"]
chars=0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
#Total characters: 22, Average length: 5.5

#------------------------------------------------------------------------------------

winners = ["Ashley", "Dylan", "Reese"]
for index,person in enumerate(winners):                 #enumerate
    print ("{} - {} ".format(index + 1, person))

#------------------------------------------------------------------------------------------- 

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("senarathnemalindi@gmail.com", "Kaveesha"), ("kaveeshamalindi@gmail.com", "malindi")]))

#----------------------------------------------------------------------------------------

multiples=[]
for x in range(1, 11):
    multiples.append(x*7)

print(multiples)
print(type(multiples))      #<class 'list'>

#---------------------- List comprehension ---------------------------

more=[x*2 for x in range(1,11)]
print(more)

More=[x*2 for x in range(1,5)]
print(More)

#------------------------------------------------------------

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range(0, 101) if x%3 == 0]
print(z)





