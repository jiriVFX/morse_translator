# Morse code converter
from morse import MorseTranslator

translator = MorseTranslator()

print("""  __  __                       _______                  _       _             
 |  \/  |                     |__   __|                | |     | |            
 | \  / | ___  _ __ ___  ___     | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __ 
 | |\/| |/ _ \| '__/ __|/ _ \    | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
 | |  | | (_) | |  \__ \  __/    | | | | (_| | | | \__ \ | (_| | || (_) | |   
 |_|  |_|\___/|_|  |___/\___|    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|   """)
while True:
    choice = input("\nType 'e' for text-to-Morse encoding, 'd' for Morse-to-text decoding or 'q' to quit: \n")

    if choice == "e":
        print("\nYour text can include:\n1. Letters from english alphabet,\n2. Numbers from 0 to 9"
              "\n3. Selected special characters: & " "' " '"' " @ ( ) : , = ! . - % + ? /")
        text_to_translate = input("\nText to be translated: \n")
        print("Encoded result:\n" + translator.to_morse(text_to_translate))
    elif choice == "d":
        print("\nYour morse code may include only dots(.), spaces( ), dashes(-) and slashes(/)")
        morse_to_decode = input("Morse code to be decoded: \n")
        print("Decoded result:\n" + translator.to_text(morse_to_decode))
    elif choice == "q":
        print("Bye bye!")
        break
    else:
        print("Wrong input, type only 'e', 'd' or 'q', please.")
