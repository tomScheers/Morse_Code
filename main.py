import os
import vlc
import time
import re


# This function will play all of the beeps that you pass down
def play_beeps(beeps) -> None:
    instance = vlc.Instance()
    player = instance.media_player_new()

    for beep in beeps:
        if not beep:
            print(" / ", end="", flush=True)
            time.sleep(1.5)
            continue

        print(('-' if re.match(r'.*long\.wav$', beep) else '.'),
              end='',
              flush=True)
        media = instance.media_new(beep)
        player.set_media(media)
        player.play()
        while player.get_state() not in [vlc.State.Ended, vlc.State.Error]:
            time.sleep(0.1)

    instance.release()

    # Print an \n character
    print("")


# Translate all of the morse codes to its corresponding file path and play it
def morse_to_sound(morse) -> None:
    beep_dir = os.path.join(os.path.dirname(__file__), "beeps")
    beeps = [
        os.path.join(beep_dir, 'short.wav' if char == '.' else 'long.wav')
        if char in '.-' else '' for char in morse
    ]
    play_beeps(beeps)


# Translate a string into morse code
def text_to_morse(text) -> str:
    morse_code_dict = str.maketrans({
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
    })
    text_in_morse = text.lower()
    text_in_morse = text.translate(morse_code_dict)
    filtered_text = [char for char in text_in_morse if char in ".- "]
    text_in_morse = ''.join(
        filtered_text
    )  # Check if any unexpected chars are found inside of the str, if so, remove them
    return text_in_morse


if __name__ == "__main__":
    your_morse = input(
        "What's the text that you want to translate to morse code: ")
    morse = text_to_morse(your_morse)
    morse_to_sound(morse)
