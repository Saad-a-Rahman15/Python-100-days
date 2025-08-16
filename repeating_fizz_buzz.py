 #Repeating Fizz Buzz


print('>>> Test Number 1 >>>')


def fizz_buzz():
    fizz_buzz_amount = int(input("How many times do you want 'Fizz Buzz' to print? \n"))
    print(" ")

    for i in range(1, (fizz_buzz_amount * 15) + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 ==  0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

    print('''           FFFFFFFF  IIIIIII  ZZZZZZZ  ZZZZZZZ      BBBBBBB   U     U  ZZZZZZZ  ZZZZZZZ 
                F         I            Z        Z        B     B  U     U       Z        Z   
                F         I           Z        Z         B     B  U     U      Z        Z    
                FFFFF     I          Z        Z          BBBBBBB  U     U     Z        Z     
                F         I         Z        Z           B     B  U     U    Z        Z      
                F         I        Z        Z            B     B  U     U   Z        Z       
                F      IIIIIII  ZZZZZZZ  ZZZZZZZ         BBBBBBB   UUUUU   ZZZZZZZ  ZZZZZZZ ''')
    

j = '   '


j = input("Do you want to run the Fizz Buzz program? (yes/no) \n")
    
while j != 'no':
    fizz_buzz()

#Success!