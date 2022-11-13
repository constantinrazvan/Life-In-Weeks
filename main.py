# Life in weeks - Project
import time
import os

print(
    "Hello and welcome to the Life in Weeks - Project! I hope you are ready to use it! \n"
)

list1 = [1, 2, 3, 4, 5]

for i in reversed(list1):
    print(i)
    time.sleep(1)
  
os.system('clear')

user_age = int(input("How old are you? \n"))
age = 90

difference = 90 - user_age

days = difference * 365
weeks = difference * 52
months = difference * 12

print(f"If your age is {user_age} then you have {days} days, {months} months, {weeks} weeks untill you'll turn 90")
time.sleep(3)
os.system("clear")
print("I hope that you enjoyed it!")
