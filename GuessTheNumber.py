import random
a=input("Please enter your name : ")
print("Hello!",a)
print("You have 10 chances guess the number that computer generates randomly from 0 to 100")
b=None
c=random.randint(0,100)
i=0
while b!=c and i<10 :
   b=int(input("Please enter a number from 0 to 100 : "))
   i=i+1
   if b>100 or b<0:
      print("Please enter a number between 0 to 100")
   if b>c :
      print("you guessed number greater than computer's.. try again")
   if b<c :
      print("you guessed number less than computer's... try again")
if b==c:
   print("Hurray!!! ",a," you guessed the right number")
else:
   print("you've lost",a,".","Better luck next time :-(")