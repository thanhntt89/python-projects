from string_utils import stringUtils

class program():
    def main():
        print("This is program class\n")
        utils = stringUtils()
        email = input("Please input email address:").strip()
        user_name, domain_name = utils.getUserAndDomain(email)
        utils.printMsg(user_name, domain_name)

    if __name__ == "__main__":
        main()
