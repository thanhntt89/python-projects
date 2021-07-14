from password_utils import passwordUtils

def main():
    pass_generator = passwordUtils()
    print(f'Passwords: {pass_generator.passwordGenerator(16)}')

if __name__ =="__main__":
    main()