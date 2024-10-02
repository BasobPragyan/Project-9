print("Manchester United Youth Football Team Age Selection")
name=input("Enter your name : ")
age=int(input("Enter your age : "))
if age<10:
    print(name,"Sorry you are not allowed.Try next time")
elif age>10:
    print(name,"You are allowed to play to the Manchester United Youth Team")
elif age<20:
    print("Congrats you are allowed to play")
else:
    print("Try next time maybe to senior team")