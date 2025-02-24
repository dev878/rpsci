import random
comp=random.choice([1,2,3])
you = input("Enter the choice (s/p/sci): ")  
d = {'s': 1, 'p': 2, 'sci': 3}
num = d[you]

if num is None:
    print("Invalid input. Please enter one of 's', 'p', or 'sci'.")
else:
    if comp == num:
        print("It's a draw")
    else:
        if comp == 1 and num == 2:
            print("You win")
        elif comp == 2 and num == 1:
            print("Computer wins")
        elif comp == 1 and num == 3:
            print("Computer wins")
        elif comp == 2 and num == 3:
            print("You win")
        elif comp == 3 and num == 2:
            print("Computer wins")
        elif comp == 3 and num == 1:
            print("You win")

