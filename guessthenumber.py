print("Hey! Wanna play a game???")
if input("Yes or No: ").lower() == "yes":
    print("Great! Let's play guess the number game.")
    print("\n\tI'll think a random number between 1 and 100.\n\tYou gotta guess it in 10 tries")
    print("You can type 'Quit' if you wanna give up. ")
  import random
  num=random.randint(1,100)
  i=1
  while i<=10:
    n=i+1
    guess=int(input("Enter your guess:"))
     if guess<num:
        print("Too low...\n\tTry again!!!")
     elif guess>num:
        print("Too high...\n\tTry again!!!")
     else:
        print("Bingo!\n\tYou guessed the number in",n,"tries.")
    
else:
    print("Well maybe next time.")
    