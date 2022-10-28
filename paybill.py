import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


#Write your code below this line 👇
l= len(names)
randnum = random.randint(0,l-1)
pay_bill = names[randnum]
print(f'{pay_bill} is going to buy the meal today!')
