from flask import Flask, jsonify
from main import Dice

app = Flask(__name__)
dice_roller = None

@app.route('/roll', methods=['GET'])
def roll_dice():
    global dice_roller
    if not dice_roller:
        # Initialize the dice roller with default values
        dice_roller = Dice(1, 1)
        return 'Dice roller initialized with default values'
    
    roll_data = dice_roller.roll_dice()
    return jsonify({'roll_data': roll_data})

if __name__ == '__main__':
    app.run(debug=True)