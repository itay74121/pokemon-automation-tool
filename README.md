# Pokemon Auto-fighter & Auto-catcher Bot

A simple bot that automates playing Pokemon by using the 'pynput' and 'PIL' libraries. It can be used for both fighting and catching Pokemon.


## Features

- Automatically moves in-game to encounter Pokemon.
Can fight against encountered Pokemon, using moves based on user-defined parameters.
- Can also automatically catch encountered Pokemon, using Pokeballs and status moves like Sleep Powder.
- Uses 'pynput' and 'PIL' libraries to interact with the game.
- Includes a real-time status update feature to monitor the bot's progress.
### Requirements

- Python 3.x
- 'pynput' library
- 'PIL' (Python Imaging Library)
- 'pytesseract' library
- 'telegram-send' library (for sending notifications)
- Tesseract OCR engine (for reading in-game text)

## Usage

- Clone the repository and navigate to the directory in the terminal/command line.
- Install the required libraries by running pip install -r requirements.txt.
- Modify the 'poke-data.json' file to reflect your desired settings, including the moves you want to use in battle and the Pokemon you want to catch.
- Start the bot by running python main.py.


## License

This project is licensed under the MIT License - see the LICENSE file for details.

