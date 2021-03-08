class MorseTranslator:
    text_to_morse = {
        "a": ".- ",
        "b": "-... ",
        "c": "-.-. ",
        "d": "-.. ",
        "e": ". ",
        "f": "..-. ",
        "g": "--. ",
        "h": ".... ",
        "i": ".. ",
        "j": ".--- ",
        "k": "-.- ",
        "l": ".-.. ",
        "m": "-- ",
        "n": "-. ",
        "o": "--- ",
        "p": ".--. ",
        "q": "--.- ",
        "r": ".-. ",
        "s": "... ",
        "t": "- ",
        "u": "..- ",
        "v": "...- ",
        "w": ".-- ",
        "x": "-..- ",
        "y": "-.-- ",
        "z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- ",
        "&": ".-... ",
        "'": ".----. ",
        "@": ".--.-. ",
        ")": "-.--.- ",
        "(": "-.--. ",
        ":": "---... ",
        ",": "--..-- ",
        "=": "-...- ",
        "!": "-.-.-- ",
        ".": ".-.-.- ",
        "-": "-....- ",
        "%": "----- -..-. ----- ",
        "+": ".-.-. ",
        '"': ".-..-. ",
        "?": "..--.. ",
        "/": "-..-. "
    }

    morse_to_text = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        ".----": "1",
        "..---": "2",
        "...--": "3",
        "....-": "4",
        ".....": "5",
        "-....": "6",
        "--...": "7",
        "---..": "8",
        "----.": "9",
        "-----": "0",
        ".-...": "&",
        ".----.": "'",
        ".--.-.": "@",
        "-.--.-": ")",
        "-.--.": "(",
        "---...": ":",
        "--..--": ",",
        "-...-": "=",
        "-.-.--": "!",
        ".-.-.-": ".",
        "-....-": "-",
        ".-.-.": "+",
        ".-..-.": '"',
        "..--..": "?",
        "-..-.": "/"
    }

    def to_morse(self, text):
        """Takes a plain text string as an argument and returns its translation into Morse code."""
        translation = ""
        text = text.lower()
        # If text parameter is not a string
        if type(text) is not str:
            return f"{text} is not a string value. Please enter only a string as an argument."
        # If text is a string, continue with the rest of the method
        if len(text) > 0:
            for i in range(0, len(text)):
                if text[i] == " ":
                    translation += "/ "
                else:
                    if text[i] in self.text_to_morse:
                        translation += self.text_to_morse[text[i]]
                    else:
                        translation += "# "
                        print(f"Character'{text[i]}' is not supported.")

            return translation

    def to_text(self, morse_code):
        """Takes Morse code string as an argument and returns a string with plain text translation."""
        translation = ""
        current_letter = ""
        # If morse_code parameter is not a string
        if type(morse_code) is not str:
            return f"{morse_code} is not a string value. Please enter only a string as an argument."
        # If morse_code is a string, continue with the rest of the method
        if len(morse_code) > 0:
            for i in range(0, len(morse_code)):
                # Space is recognized as the end of the letter
                if morse_code[i] == " " and len(current_letter) > 0:
                    if current_letter in self.morse_to_text:
                        translation += self.morse_to_text[current_letter]
                        # Clear current_letter
                        current_letter = ""
                    else:
                        translation += "#"
                        current_letter = ""
                        print(f"Character'{current_letter}' not recognized.")
                # Slash is recognized as the end of the word and space
                elif morse_code[i] == "/":
                    translation += " "
                # If the current character is the space after slash / or space at the end
                elif morse_code[i] == " " and len(current_letter) == 0:
                    pass
                elif morse_code[i] == "." or morse_code[i] == "-":
                    # In this case add "." or "-" to the current_letter
                    current_letter += morse_code[i]
                else:
                    # If we encounter invalid character, we first try to write current letter
                    if current_letter in self.morse_to_text:
                        translation += self.morse_to_text[current_letter]
                        current_letter = ""
                    # Then add the invalid character to the translation
                    translation += morse_code[i]
                    print(f"Ignoring invalid character '{morse_code[i]}'")

            # We have looped through morse_code, but have to write the last character if there was no space at the end
            # Add the last character
            if current_letter in self.morse_to_text:
                translation += self.morse_to_text[current_letter]
            else:
                # If current_letter is not empty but can't be translated
                if current_letter != "":
                    translation += "#"
                    print(f"Character '{current_letter}' not recognized NOT SPACE NOT /.")
                else:
                    translation += current_letter
            return translation
