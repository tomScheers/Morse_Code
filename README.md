# Morse Code Translator
A basic translator in python that translates a string into Morse code. The program outputs the Morse code as text and plays beep to represent the dots and dashes.

# Requirements
- Python 3.x
- `vlc` for Python
To install `vlc` for python, run:
`pip3 install python-vlc`
or, on Debian-based systems:
`sudo apt install python3-vlc`

# Usage
1. Clone the repository and navigate to it:
`git clone https://github.com/tomScheers/Morse_Code`
`cd Morse_Code`

2. Run the program
`python3 main.py`

3. Provide your input:
- When prompted, type the string you want translated to Morse code (e.g., `"Hello, World!"`).
- The program will ignore any non-alphanumeric characters and convert uppercase letters to lowercase.
- You'll then see the Morse code representation printed, and you'll hear short and long beep for dots and dashes
