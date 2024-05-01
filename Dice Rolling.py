import random
import re
import math


#Rolls x dice and returns values and how many meet a specific value
def dice_rolls_target():
    print("Hello, I can calculate dice rolls for you!")
    while True:
        successes = []
        failures = []
        print("I can recognize dice in 4, 6, 8, 10, 12, 20, 30, and 100 sided dice")
        while True:
            list_of_dice = [4, 6, 8, 10, 12, 20, 30, 100]
            type_of_dice = input("What kind of sided dice do you want to roll?")
            if re.search("\\D", type_of_dice):
                print("Error: Must provide a whole number")
                continue
            elif int(type_of_dice) not in list_of_dice:
                print("Error: The types of dice are d4, d6, d8, d10, d12, d20, d30, and d100")
                continue
            else: type_of_dice = int(type_of_dice)
            break
    
# define number of dice rolled
        while True:
            number_of_dice = input("How many of these dice are you rolling? I can handle up to 200 at once!")
            if re.search("\\D", number_of_dice):
                print("Error: Must provide a whole number")
                continue
            elif int(number_of_dice)>200:
                print("That's too many dice! I can do up to 200 at once.")
                continue
            else: number_of_dice = int(number_of_dice)
            break

#define the modifier
        penalty = 0
        while True:
            positive_or_negative = input("Is there a bonus or penalty to the roll? (Bonus, penalty, or none)")
            if positive_or_negative.lower() == "bonus":
                break
            elif positive_or_negative.lower() == "penalty":
                penalty = -1
                break
            elif positive_or_negative.lower() == "none":
                penalty = "none"
                break
            else: print ("Error: Please say 'bonus', 'penalty', or 'none'")
            continue

        while True:    
            if penalty != "none":  
                modifier = input("What number is the roll modified by?")
                if re.search("\\D", modifier):
                    print("Error: Must provide a whole number")
                    continue
                elif penalty == -1:
                    modifier = penalty*int(modifier)
                else: modifier = int(modifier)
                break
            else: modifier = 0
            break

#get the target number
        print("What does a successful roll value look like?")
        while True:
            target_number = input("What's the target number?")
            if re.search("None", target_number):
                break
            elif re.search("\\D", target_number):
                print("Error: Must provide a whole number")
                continue
            elif int(target_number) > type_of_dice+modifier:
                print("Your dice can't reach that number!")
                continue
            else: target_number = int(target_number)
            break

# roll dice and number of x sided dice
        for number in range(int(number_of_dice)):
            dice_outcome = random.randint(1,type_of_dice) + modifier
            if dice_outcome >= target_number:
                    if dice_outcome > type_of_dice:
                            dice_outcome = type_of_dice
                            successes.append(dice_outcome)
                    else:
                            successes.append(dice_outcome)
            else: failures.append(dice_outcome)

        print("successes", len(successes), successes.sort())
        print("failures", len(failures), failures.sort())
        again = input("Do you want to count again?")
        if again.lower() == "yes":
            
            continue
        elif again.lower() == "no":
            print("Goodbye")
            break

dice_rolls_target()
