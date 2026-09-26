#---------------------------for loop------------------------------------------------------------------

even_numbers = []
for x in range(1,11):
    even_numbers.append(x*2)
print(even_numbers)

#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

#--------------------------List Comprehension --------------------------------------------------------------

even_numbers = [x*2 for x in range(1, 11)]
print(even_numbers)

#[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



