# alphabet to morse code converter
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}
loop_on = True


def encrypt(message):
    morse_lst = []
    for letter in message.upper():
        morse_letter = MORSE_CODE_DICT[letter]
        morse_lst.append(morse_letter)
    word = " ".join(morse_lst)
    print(word)


def decrypt(message):
    word_lst = []
    for letter in message.split():
        word_letter = REVERSE_DICT[letter]
        word_lst.append(word_letter)
    morse = "".join(word_lst)
    print(morse)


while loop_on:
    print("---------------xxx------------")
    print("choose a option:")
    print("1.word to morse code\n"
          "2.morse code to word\n"
          "3.exit\n")

    num = int(input("enter the number:"))

    if num == 1:
        encrypt(input("enter the word:"))
    elif num == 2:
        decrypt(input("enter the code:"))
    elif num == 3:
        loop_on = False
