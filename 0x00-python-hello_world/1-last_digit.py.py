
import random
number = random.randint(-10000, 10000)
num = abs(number) % 10
# if num > 5:
#     print(f"Last digit of {number} is {num} and is greater than 5")
# elif num == 0:
#     print(f"Last digit of {number} is {num} and is 0")
# elif num < 6 & num != 0:
#     print(f"Last digit of {number} is {num} and is less than 6 and not 0")

print(f"Last digit of {number} is {num} and",end=" ")
if num > 5:
    print("is greater than 5")
elif num == 0:
    print("is 0")    
else:
    print("is less than 6 and not 0") 