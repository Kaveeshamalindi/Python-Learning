#-----------------------Method-----------------------------------------------------------

pets = "Cats & Dogs"

pets.index("&")
print(pets.index("&"))

pets.index("C")
print(pets.index("C"))

pets.index("Dog")
print(pets.index("Dog"))

pets.index("s")
print(pets.index("s"))

#pets.index("x")
#print(pets.index("x"))  #Value error

Dragons = "Dragons" in pets
print(Dragons)

Cats = "Cats" in pets
print(Cats)

#-------------------------------------------------------------------------------------

up="Moutains".upper()
print(up)

lower="Mountains".lower()
print(lower)

#-----------------------------------------------------------------------

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

#------------------ strip method -----------------------------------------------

Space =" yes ".strip() # white space
print(Space)

Space1 =" yes ".lstrip() # white space
print(Space1)

Space2 =" yes ".rstrip() # white space
print(Space2)

#---------------------------- count ------------------------------------
#How many times sub-string appears

count = "The number of times e occurs in this string is 4".count("e")
print(count)

#-------------------------- endwith -------------------------------
#whether the string ends withs a certain sub-string

endwith = "Forest".endswith("rest")
print(endwith)

#----------------------------- isnumeric ------------------------------------------------
#wehether the strings made up of just numbers

input1 = "Forest".isnumeric()
input2 = "12345".isnumeric()

print(input1)
print(input2)

#----------------------------- Adding ---------------------------------------------

out6666 = int("12345") + int ("54321")
print(out6666)

#---------------------------------------- join ---------------------------------------

join1 = " ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
join2 = "...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])

print(join1)
print(join2)

#--------------------------------------------- split -------------------------------------

split = "This is another example".split()
print(split)

