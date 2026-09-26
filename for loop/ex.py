
num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

#-------------------------------------------------------------------

for sum in range(5):
    sum += sum
    print(sum)

#-----------------------------------------------------------

def even_numbers(n):
    count = 0
    current_number = 0
    while current_number<=n: # Complete the while loop condition
        if current_number % 2 == 0:
            count +=1 # Increment the appropriate variable
        current_number += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

#------------------------------------------------------------------------------

