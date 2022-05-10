import random

NUM_DIGITS = 3  # can be change from 1 to 9
MAX_GUESSES = 10  # can be change


def main():
    print(f'''
		I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
		Try to guess what it is. Here are some clues:
		When I say:    That means:
    		Pico         One digit is correct but in the wrong position.
			Fermi        One digit is correct and in the right position.
			Bagels       No digit is correct.

		For example, if the secret number was 248 and your guess was 843, the
		clues would be Fermi Pico.''')

    while True:
        secretBagel = secretBagel()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} to get it.')
        numGuesses = 1
        while numGuesses <= MAX_GUESSES or not guess.isdecimal():
            guess = ''
            while len(guess) != len(NUM_DIGITS):
                print(f'#{numGuesses} guess :')
                guess = input('>>')
            clues = getClues(guess, secretBagel)
            print(clues)
            numGuesses += 1

            if guess == secretBagel:
                break
            if numGuesses > MAX_GUESSES:
                print(
                    f'You have exhausted all your attempts, sorry :(, the answer was {secretBagel}')

        print("Do you want to play again ? (yes/no)")
        res = input('>>')
        if not res.lower().startswith('y'):
            break
    print("Thanks for playing")


def secretBagel():
    numbers = list('0123456789')
    random.shuffle(numbers)
    bagels = ''
    for i in range(NUM_DIGITS):
        bagels += str(numbers[i])
    return bagels


def getClues(guess, bagels):
    if guess == bagels:
        return 'you find it !'

    clues = []

    for i in range(len(guess)):
        if guess[i] == bagels[i]:
            clues.append('Fermi')
        elif guess[i] in bagels:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
