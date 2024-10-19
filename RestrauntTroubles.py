total_bill = input("What is the total bill? \n")
adult_numbers = input("How many adults are there? \n")
children = input("How many children's age is under 10? \n")

total_bill = int(total_bill)
adult_numbers = int(adult_numbers)
children = int(children)

adult_numbers += round(children / 3)


adult_share = total_bill / adult_numbers


adult_share = round(adult_share)

print("Each adult will pay £" + str(adult_share) + ". :)")
print("By the way, you aren't allowed to come to this place anymore. YOU NEED TO LEAVE")
print("Or you could work for Temu for the rest of your life. XD")