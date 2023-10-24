def main():
    boo = True

    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    user_input = int(input('Please enter an option: '))


    while boo:
        if user_input == 1:
            password = input('Please enter your password: ')
            print('Your password has been encoded and stored!')
            pass_word = encode(password)
        elif user_input == 2:
            print('The encoded password is', pass_word, 'and the original password is', password)

        
        

def encode(password):
    temp_string = ''        
    for i in password:
        i = int(i)
        i += 3
        temp_string += str(i)
    return temp_string
