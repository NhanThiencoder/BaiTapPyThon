import random
def level():
    print("Level 1: You have 9 chances to guess a number.")
    print("Level 2: You have 6 chances to guess a number.")
    print("Level 3: You have 4 chances to guess a number.")
    level = 1
    while True:
        level = int(input("Enter your level: "))
        if 0 < level <= 3:
            chance = 9 if level == 1 else 6 if level == 2 else 4
            print(f"You choose level {level}: You have {chance} chances to guess a number.")
            return chance
def game_engine(chance):
    is_win = False
    ran_number = random.randint(1,100)
    for i in range(0,chance):
        guess_number = int(input("Guess a number: "))
        if ran_number == guess_number:
            print("You got it!")
            is_win = True
            break
        if ran_number > guess_number:
            print("your choice was lower than right number.")
        if ran_number < guess_number:
            print("your choice was higher than right number.")

if __name__ == '__main__':
    plays= 0
    win=0
    while True:
        plays +=1
        choose_level = level()
        if game_engine(choose_level):
            win+=1
        reponse = input("Would you like to play again? (y/n): ")
        if reponse == "n":
            break
    print(f"{plays}")
    print(f"{win}")


