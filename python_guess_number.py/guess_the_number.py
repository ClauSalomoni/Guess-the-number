# print some art
import random

print("""
$$\   $$\                         $$\                                  $$$$$$\                                          $$\                            $$$$$$\                                    
$$$\  $$ |                        $$ |                                $$  __$$\                                         \__|                          $$  __$$\                                   
$$$$\ $$ |$$\   $$\ $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\        $$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ $$\ $$$$$$$\   $$$$$$\        $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ $$\$$ |$$ |  $$ |$$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$ |$$  __$$\ $$  __$$\       $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$ \$$$$ |$$ |  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|      $$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |      $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
$$ |\$$$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |            $$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
$$ | \$$ |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |            \$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |      \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
\__|  \__| \______/ \__| \__| \__|\_______/  \_______|\__|             \______/  \______/  \_______|\_______/ \_______/ \__|\__|  \__| \____$$ |       \______/  \_______|\__| \__| \__| \_______|
                                                                                                                                      $$\   $$ |                                                  
                                                                                                                                      \$$$$$$  |                                                  
                                                                                                                                       \______/                                                   
""")
print("Welcome to the guess a number game")

level_choice = input("Please choose the level typing: hard, ou easy: ").lower()
number = random.randint(1, 100)


def compare_easy():
    number_attempts = 10
    while number_attempts > 0:

        number_guessed = int(input("Please guess a number between 1 and 100: "))

        if number_guessed > number:
            number_attempts -= 1
            print(f"Too high\nYou have {number_attempts} left\nGuess again")
        elif number_guessed < number:
            number_attempts -= 1
            print(f"Too low\nYou have {number_attempts} left\nGuess again")
        else:
            print(f"The number is {number}. You win!!")
            return

    print(f"The number is {number}. Sorry, you loose.")


def compare_hard():
    number_attempts = 5

    while number_attempts > 0:

        try:
            number_guessed = int(input("Please guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid number ;): ")
            continue
        if number_guessed > number:
            number_attempts -= 1
            print(f"Too high\nYou have {number_attempts} left\nGuess again")
        elif number_guessed < number:
            number_attempts -= 1
            print(f"Too low\nYou have {number_attempts} left\nGuess again")

        else:
            print(f"The number is {number}. You win!!")
            return
    print(f"The number is {number}. Sorry, you loose.")


while True:
    if level_choice == "easy":
        compare_easy()
        break
    elif level_choice == "hard":
        compare_hard()
        break
    else:
        print("Invalid choice. Please choose 'easy' or 'hard")
        level_choice = input("Please choose the level typing: hard, ou easy: ").lower()
        continue




