#--------------------------------------------- format --------------------------------

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))

#---------------------------------------------------------------------------------------

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

#----------------------------------------------------------------------------------

price = 7.5
with_tax = price * 1.09
print(price, with_tax)          #7.5 8.175
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax)) # Base price: $7.50. With Tax: $8.18 #use two decimal numbers # 2f---> 2 digits, float

#------------------------------------------------------------------------------------

def convert_distance(miles):
    km = miles * 1.6 
    result = "{x:.1f} miles equals {y:.1f} km".format(x=miles,y=km) 
    return result


print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

#--------------------------------------------------------------------------------------   

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))


