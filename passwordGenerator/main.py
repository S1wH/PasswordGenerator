import secrets
from math import log2
import passwordStrength


ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_symbols = '!#$%&*+-=?@^'


def setPossibleCharacters(uppercase: bool, digits: bool, punctuations: bool):
    characters = ascii_lowercase
    if uppercase is True:
        characters += ascii_uppercase
    if digits is True:
        characters += numbers
    if punctuations is True:
        characters += special_symbols
    return characters


def generatePassword(length: int, characters: str):
    return ''.join(secrets.choice(characters) for i in range(length))


def getBoolAnswer(answer: str):
    if answer == 'y':
        return True
    return False


def getEntropy(password_length: int, characters_length: int):
    entropy = password_length * log2(characters_length)
    return round(entropy, 1)


def getPasswordStrength(entropy: float):
    p_strength = ''
    for strength in passwordStrength.StrengthOfPassword:
        if entropy >= strength.value:
            p_strength = strength.name
        else:
            return p_strength


def main():
    try:
        length = int(input('Enter password length(max length 30): '))
        if length <= 0 or length > 30:
            raise ValueError
        uppercase = input('Include uppercase symbols (yes = y, no = n): ')
        if uppercase != 'y' and uppercase != 'n':
            raise ValueError
        digits = input('Include numbers (yes = y, no = n): ')
        if digits != 'y' and digits != 'n':
            raise ValueError
        punctuations = input('Include special symbols (yes = y, no = n): ')
        if punctuations != 'y' and punctuations != 'n':
            raise ValueError
    except ValueError:
        print('Invalid input')
        return -1
    characters = setPossibleCharacters(getBoolAnswer(uppercase), getBoolAnswer(digits), getBoolAnswer(punctuations))
    password = generatePassword(length, characters)
    entropy = getEntropy(length, len(characters))
    strength = getPasswordStrength(entropy)
    print(f'Generated password " {password} " has entropy {entropy}')
    print(f'This password is {strength}')


if __name__ == '__main__':
    main()
