# Print Hello User!
import random
print("heloo user!")
z="y"
# Take in User Input
while (z=="y") :
   x=input("please tell me your name!")
# Respond Back with User Input


# Take in the User Favorite Number
   l=int(input("tell me your fovarite number!"))
   k=int(random.choice(range(1,5)))
   if (l==k) :
# Respond Back with a statement based on your favorite number
      print("your name is"+ x +"and your fvarite number is"+str(l))
      z=input(print("do you want to continue:y/n?"))
   else : 
      print("bad") 
      z=input(print("do you want to continue:y/n?"))
print("goodbye")