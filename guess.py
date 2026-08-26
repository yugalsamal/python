print("Hey!Wanna play a game???")
if input("yes/no\n").lower()=='yes':
    print("It's a guessing game.\nI think of number between 1 and 100 you just have to guess it with the minimum number of tries possible.")
    import random
    a=random.randint(1,100)
    i=0
    while i<=10:
        guess=int(input("Enter your guess:"))
        if(guess>a):
            print("Too high!!!Try again")
        elif(guess<a):
            print("Too low!!!Try again")
        else:
            print("Bingo!!!\nYou guessed the number in",i,"tries")
        i=i+1
        if(i==10):
            print('Your number of tries has been depletedy.\n\t!Bettter luck next time!')



        

     

 
