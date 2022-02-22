def password_validator(passw) :

    SpecialSym = ['$', '@', '#', '%']
    val = True

    if len(passw) < 6 :
        print("Password must more than 6 digits")
        val = False

    if len(passw) > 20 :
        print("Password must less than 20 digits")
        val = False

    if not any(char.isdigit() for char in passw) :
        print("Password should at least one numeral")
        val = False

    if not any(char.isupper() for char in passw) :
        print("Password must at least one upper letter")
        val = False

    if not any(char.islower()for char in passw):
        print("Password must at least one lower")
        val = False

    if not any(char in SpecialSym for char in passw) :
        print("Password muust at least one special character")
        val = False

    if val:
        return val

def main():

    passw = "Retro1234$"

    if(password_validator(passw)):
        print("Password is valid")
    else:
        print("password is not valid")

if __name__ == '__main__':
    main()



