#modify list------------------------------------------------------

fruits = ["Pineapple", "Banana", "Apple", "Melon"]

#----------------- append ---------------------------------

fruits.append("Kiwi") #add to end of the list
print(fruits)

#-------------------- insert --------------------------

fruits.insert(0, "Orange") #change the item
print(fruits)

fruits.insert(25, "Peach")
print(fruits)

#------------------------ remove-------------------------

fruits.remove("Melon") #remove the item
print(fruits)

#fruits.remove("Pear")
#print(fruits)              #Value Error

#------------------ pop --------------------------------

fruits.pop(3) #remove the previous item
print(fruits)

#-------------------------change item -----------------

fruits[2] = "Strawberry"
print(fruits)

#---------------------------reverse-------------------------

fruits.reverse() 
print(fruits)

#--------------------------------- copy ----------------------------

Fruits=fruits.copy()
print(Fruits)

#--------------------------- clear ------------------------------


F=fruits.clear()
print(F)            #None

#------------------------------replace----------------------------------

#-------------------- example ----------------------------

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.


new_filenames = []
for filename in filenames:
    if filename.endswith("hpp"):
        new_filenames.append(filename.replace("hpp", "h"))
    else:
        new_filenames.append(filename)



print(new_filenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#---------------------------------------------------- sort ----------------------------

numbers = [4, 6, 2, 7, 1]
numbers.sort()
print (numbers)

#---------------------------------------------- sorted -----------------------------------------------

names = ["Ray", "Alex", "Kelly"]

print(names)
#['Ray', 'Alex', 'Kelly']

print(sorted(names))
#['Alex', 'Kelly', 'Ray']

print(names) 
##['Ray', 'Alex', 'Kelly']      #Do not change the original list


#---------------------- sort + len ----------------------------------------------------

print(sorted(names, key = len))

 