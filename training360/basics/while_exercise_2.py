tipp = None
import random
num = random.randint(1,100)
print(num)
while True:
 tipp = int(input("Tipp a number between 1 and 100: "))
 if tipp == num:
  break
 elif tipp > num:
  print("Number is less than you think!")
 else:
  print("Number is more than you think!")
print("Well done, you nailed it!")
 