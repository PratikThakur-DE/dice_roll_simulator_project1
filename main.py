import random

from collections import deque

class Dice:
    """
    Class rolling dice simulation
    """
    def __init__(self, total_dice, total_sides) :
        """Initialize rolling dice

        Args:
            total_dice (int): number of dice to roll
            total_sides (int): number of sides for each dice
        """
        self.total_dice = total_dice
        self.total_sides = total_sides
        self.roll_number = 1 
        
        self.roll_history = deque(maxlen=100)
        # Store the last 100 rolls  
    
    def roll_dice(self):
        rolls = [random.randint(1, self.total_sides) for _ in range(self.total_dice)]
        total = sum(rolls)
        roll_data = (self.roll_number, rolls, total)
        self.roll_number += 1
        self.roll_history.append(roll_data)
        return roll_data
    
def main():
    def get_total_dice():
        while True:
            total_dice = input("Total number of dice to roll ( 1-5 ):")
            #Validation to check total number of dice per roll
            if total_dice.isdigit() and 1 <= int(total_dice) <= 5:
                return int(total_dice)
            else:
                print("Please enter a valid number between 1 - 5")
    
    def get_total_sides():
        while True:
            total_sides = input("Total number of sides of each dice ( 1-100 ):")
            #Validation to check total number of dice per roll
            if total_sides.isdigit() and 1 <= int(total_sides) <= 100:
                return int(total_sides)
            else:
                print("Please enter a valid number between 1 - 100")

    total_dice = get_total_dice()
    total_sides = get_total_sides()
    dice_roller = Dice(total_dice, total_sides)
   
    roll_again = True
    while roll_again:
        roll_number, rolls, total = dice_roller.roll_dice()
        print("Roll Number: {}".format(roll_number))
        print("\nResult of rolling {} dice with {} sides each:".format(total_dice, total_sides))
        print("Individual Dice: {}".format(rolls))
        print("Total of this Roll: {}".format(total))

        print("\nRoll History (Upto 100 records): ")
        for roll_data in dice_roller.roll_history:
            print("Roll Number: {}, Individual Rolls: {}, Total: {}".format(*roll_data))
        
        roll_again = input("\nRoll the dice again? y/n: ")
        if roll_again.lower() == "y":
            continue
        else:
            break

if __name__ == "__main__":
    main()