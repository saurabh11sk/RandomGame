def game():
    print("This is random game")
    import random
    global random_number
    random_number=random.randint(1,6)
    global guess
    guess=int(input("What could be the number?"))
    correct=False
    global score
    score=0
    print(random_number)
    while not correct :
        if guess==random_number:
            score=score+5
            print("Congrates you got it ")
            print("For each correct score is 5")
            print("your score is: ",score)
            break
        elif guess>random_number:
            score=0
            print("Too high")
            print("Your scoreis : ",score)
            break
        elif guess<random_number:
            score=0
            print("Too low")
            print("Your score is : ",score)
            break
        else:
            print("Try something else")
            break
    score=score+score
game()
a=input("do you want to play again(yes/y to replay): ")
if a=='yes':
    while a=='yes':
        game()
        a=input("do you want to play again(yes/y to replay): ")
        if a!='yes':
            print("thank you for playing . have a nice day")
            
else:
    print("thank you for playing . have a nice day")