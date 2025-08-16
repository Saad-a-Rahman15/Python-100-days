
    
names = []
grades = []
    
records = [
    ['prashant', 32], ['palavvi', 36], ['dheeraj', 39], ['shivan', 40]
    ]
for lists in records:
    names.append(lists[0])
    grades = (grades)
    grades.append(lists[1])
    

grades.sort()

smallest_numbers = []

smallest_numbers.append(grades[0])

print(grades)
for e in grades:
    print(f'24:', e)
    print(f'This is {grades}')
    if smallest_numbers[0] in grades:
       grades.remove(e)
       print(grades)
grades.remove(grades[1])
print(f'grades' , grades)
smallest_numbers.append(grades[1])

print(f'smallest numbers', smallest_numbers)

# if smallest_numbers[1] in grades:
#     smallest_numbers.append(grades[0])
    
# smallest_numbers.remove(smallest_numbers[0])
        
# second_last = []   

# smallest_numbers[0] = str(smallest_numbers[0])
   
# person = []        
# for item in records:
#     if smallest_numbers[0] in str(item[1]):
#         person.append(item[0])

# person.sort()        

# for name in person:
#     print(name)
