from random import *
print("1.Rock\n2.Paper\n3.Scissor")
list=[1,2,3]
a=int(input("Choose your option"))
if a not in list:
    print("Enter valid option:")
else:
    b=choice(list)
    print(f"Computer chose: {b}") 
    if (a==b):
        print("Match is tie")
    elif (a==1 and b==2) or (a==3 and b==1) or (a==2 and b==3):
        print("You lose the match")
    else:
        print("You won the match")
