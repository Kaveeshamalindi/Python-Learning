#Example 1 ---------------------------------------------------------------------

def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)

sum = area_a + area_b

print ("The sum of both areas is " + str(sum))

#Example 2 ---------------------------------------------------------------------

def convert_second(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) //60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_second(5000)
print (hours, minutes, seconds)

#Example 3 -------------------------------------------------------------------------

def greeting(name):
    print("welcome, " + name)

result = greeting("Kaveesha")
 
print(result)   #Output ----> None ----> Empty or Nothing

#Code Reuse

def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")
