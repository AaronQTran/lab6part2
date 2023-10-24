def main():
    boo = True
    pass_word = ""


    while boo:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        user_input = int(input('Please enter an option: '))
        if user_input == 1:
            password = input('Please enter your password: ')
            print('Your password has been encoded and stored!\n')
            pass_word = encode(password)
        if user_input == 2:
            print('The encoded password is', pass_word, 'and the original password is', decode(pass_word), ".\n")
        if user_input == 3:
            break


def encode(password):
    temp_string = ''        
    for i in password:
        i = int(i)
        i += 3
        temp_string += str(i)
    return temp_string


def decode(password):
    temp_string = ''
    for i in password:
        i = int(i)
        i -= 3
        temp_string += str(i)
    return temp_string


if __name__ == "__main__":
    main()
