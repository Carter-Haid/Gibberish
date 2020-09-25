from Keylogger import logresult

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%', '!', '^', '&', '*', '(', ')']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

    # Main method


def main():
    passwd = input("Please Enter a test password:")

    if password_check(passwd):
        print("Password is valid")
        print("Here is what the keylogger saw:" + logresult)
    else:
        print("Invalid Password!")



# Driver Code
if __name__ == '__main__':
    main()

