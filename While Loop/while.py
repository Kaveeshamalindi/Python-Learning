#Example 1 -----------------------------------------------------------------------------------

x=0
while x<5:
    print ("Not there yet, x=" + str(x))
    x=x+1
print("x="+str(x))

#Example 2 -----------------------------------------------------------------------------------

def attempts(n):
    x=1
    while x<=n:
        print("Attempt " + str(x))
        x+=1
    print("Done")

attempts(5)

#Example 3 ----------------------------------------------------------------------------------

#while my_variable < 10:
#    print ("Hello")
#    my_variable+=1

#Name Error --------------> Variable should be initialize before the while loop (Using it)

my_variable=5
while my_variable < 10:
    print ("Hello")
    my_variable+=1


    