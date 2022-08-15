print("Welcome to the Tech Quiz")

playing = input("do you want to play? (yes/no):   ")

if playing.lower()  != "yes":
     quit()
print("okay lets play :)")
score = 0
name = input("enter your name:   ")

ans = input("1.What does CPU stand for?")
if ans.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")
        
ans = input("2.What does GUI stand for?")
if ans.lower() == "graphical user interface":
    print("correct!")
    score += 1
else:
    print("incorrect!")

ans = input("3.What device is keyboard, input or output?")
if ans.lower()  == "output":
    print("correct!")
    score += 1
else:
    print("incorrect!")

ans = input("4.What is 15 to the power of 2?")
if ans.lower()  == "225":
    print("correct!")
    score += 1
else:
    print("incorrect!")

ans = input("5.What is the file extension of word?")
if ans.lower()  == "docx":
    print("correct!")
    score += 1
else:
    print("incorrect!")


    print("You got   " +   str(score)   + "questions correct")
    


        
