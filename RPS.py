import random

option = ["rock","paper","scissors"]
user = "abcdefgdh"
comp = "bksjasnwld"
player = 0
computer = 0

def response(user):
    user = user.lower()

    if user in option:
        comp = random.choice(option)
        print("computer: ", comp)
        return comp
    else:
        return "Invalid choice"

def win(user, comp):
    global player,computer
    if (user == "rock" and comp == "scissors") or (user == "scissors" and comp == "paper") or (user == "paper" and comp == "rock"):
        print("User won")
        player += 1
    
    elif (user == "scissors" and comp == "rock") or (user == "paper" and comp == "scissors") or (user == "rock" and comp == "paper"):
        print("Computer won")
        computer += 1

    elif (user == comp):
        print("It's a tie!")

def score():
    print("\nScoreboard:\nPlayer: ", player, "\nComputer: ", computer)

def main():
    print("Let's play!")

    game = True
    while game == True:
        user = input("Enter your choice(rock, paper, or scissors): ")
        comp = response(user)
        print(comp)
        win(user, comp)
        score()
        cont = input("\nDo u want to comtinue? y/n ").lower()
        if cont != "y":
            print("The end")
            game = False

if __name__ == "__main__":
    main()

