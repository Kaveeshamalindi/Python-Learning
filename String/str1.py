Name = "Kaveesha"

print(Name[1])

print(Name[-1])

#print(Name[10]) #Error --------> Ther have not 10th character

print(Name[0:5]) #Slicing

print(Name[:3])

print(Name[1:])

#---------------------------------------------------------------------

#Name[0]=M #Name Error --------> Immutable

#message = "A kong string with a silly typo"
#message[2] = "l"
#This will throw an error

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)

#-----------------------------------------------------------------------

message = "This is a new message"
print(message)
message = "And another one"
print(message)










