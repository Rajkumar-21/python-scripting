# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

lovescore = int(str(first_digit) + str(second_digit))

if lovescore < 10 or lovescore > 90:
    print(f"Your score is {lovescore}, you go together like coke and mentos.")
elif (lovescore >=40) and (lovescore <= 50):
    print(f"Your score is {lovescore}, you are alright together.")
else:
    print(f"Your score is {lovescore}.")

