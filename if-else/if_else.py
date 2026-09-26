#Example 1 -------------------------------------------------------------------------------

def hint_username(username):
    if len(username) < 3:
        print ("Invalid username. Must be at a least 3 characters long")
    else:
        print ("Invalid username")

#hint_username(KaveeshaMalindi) -----> Error 
hint_username("KaveeshaMalindi")

#Example 2 ------------------------------------------------------------------------------------

def is_even(number):
    if number % 2 == 0:
        return True
    return False 

#elseif ------------------------------------------------------------------------------------------


def hint_username(username): # if and else
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    else:
        if len(username) > 15:
            print("Invalid username. Must be at most 15 characters long")
        else:
            print("Valid username")

hint_username("KaveeshaMalindi")



def hint_username(username):    #if, elif and else
    if len(username) < 3:
        print("Invalid username. Must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")

hint_username("KaveeshaMalindi")