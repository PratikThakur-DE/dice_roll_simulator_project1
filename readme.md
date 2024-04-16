# Dice Roll Simulator
My first project in Python, implementing a dice roll simulator using basic Python concepts.

## Features
- Supports rolling from 1 to 5 dice.
- Each die can have from 1 to 100 sides.
- Simulates throwing the dice one or more times.
- Stores the information about the last 100 throws.

## Getting Started  
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites  
Before running this program, ensure you have the following installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)

### Installing
To install and run the program, follow below steps: 
```
$ git clone https://github.com/PratikThakur-DE/dice_roll_simulator_project1.git   
$ cd dice_roll_simulator_project1  
$ python main.py
```
## Usage
1. When prompted, enter the number of dice to roll (1-5) and the number of sides for each die (1-100).
2. The program will simulate throwing the dice and display the results.
3. You can choose to roll the dice again or exit the program.

## Example
```
$ python .\main.py
Total number of dice to roll ( 1-5 ):4
Total number of sides of each dice ( 1-100 ):44
Roll Number: 1

Result of rolling 4 dice with 44 sides each:
Individual Dice: [6, 8, 13, 29]
Total of this Roll: 56

Roll History (Upto 100 records):
Roll Number: 1, Individual Rolls: [6, 8, 13, 29], Total: 56

Roll the dice again? y/n:
```

## Testing
### Test Class
The TestDiceRoller class in the test_dice.py file contains unit tests for the Dice Roller functionality. It tests various scenarios, including edge cases and error scenarios, to ensure the correctness of the code.


## Authors
* **Pratik Thakur** 


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)][def]

[def]: https://opensource.org/licenses/MIT