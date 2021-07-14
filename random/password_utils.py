import string
import random

class passwordUtils():
    
    LETTERS = string.ascii_letters
    NUMBER = string.digits
    PUNCTUATION = string.punctuation

    @classmethod
    def passwordGenerator(self, length=8):
        printable = f'{self.LETTERS}{self.NUMBER}{self.PUNCTUATION}'
        printable = list(string.printable.strip())
        random.shuffle(printable)
        random_passwords = random.choices(printable, k = length)
        random_passwords = ''.join(random_passwords)
        return random_passwords

def main():
    pass_generator = passwordUtils()
    print(f'Passwords: {pass_generator.passwordGenerator(16)}')

if __name__ =="__main__":
    main()