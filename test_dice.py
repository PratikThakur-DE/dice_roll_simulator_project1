import unittest
from main import Dice

class TestDiceRoller(unittest.TestCase):
    def setUp(self):
        self.dice_roller = Dice(2, 6)  
        # Initialize with 2 dice and 6 sides each

    def test_roll_dice(self):
        # Test roll_dice method
        roll_number, rolls, total = self.dice_roller.roll_dice()
        self.assertEqual(roll_number, 1)  
        self.assertEqual(len(rolls), 2)
        for roll in rolls:
            self.assertTrue(1 <= roll <= 6)
        self.assertEqual(total, sum(rolls))

    def test_roll_history(self):
        # Test roll history
        for i in range(105):
            self.dice_roller.roll_dice()
        self.assertEqual(len(self.dice_roller.roll_history), 100)

    def test_rolling_multiple_times(self):
        # Test rolling the dice multiple times
        for i in range(10):
            self.dice_roller.roll_dice()
        self.assertEqual(len(self.dice_roller.roll_history), 10)

if __name__ == '__main__':
    unittest.main()