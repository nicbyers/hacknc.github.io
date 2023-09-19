"""One Shot Wordle"""
__author__ = "930690385"

secret_word: str = "python"
secret_length: int = len(secret_word)
user_word: str = input(f"What is your {secret_length}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
user_index: int = 0
secret_index: int = 0
wordle_boxes: str = ""
letter_check: bool = False
secret_indice: int = 0

while len(user_word) != secret_length:
    new_word: str = input(f"That was not {secret_length} letters! Try Again: ")
    user_word = new_word

if user_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Try again soon!")

while user_index < secret_length:
    if user_word[user_index] == secret_word[secret_index]:
        wordle_boxes = wordle_boxes + GREEN_BOX
    else:
        while letter_check == False and secret_indice < secret_length:
            if secret_word[secret_indice] == user_word[user_index]:
                letter_check = True 
            else:
                secret_indice = secret_indice + 1
                letter_check = False
        if letter_check == True:
            wordle_boxes = wordle_boxes + YELLOW_BOX
        else:
            wordle_boxes = wordle_boxes + WHITE_BOX
    secret_index = secret_index + 1
    user_index = user_index + 1
print(wordle_boxes)