# Write your code here
import random

def generate_card_number():
    iin = '400000'
    random_numbers = ''
    for i in range(0, 10):
        n = random.randint(0, 9)
        random_numbers += str(n)
    return iin + random_numbers

def generate_pin():
    random_numbers = ''
    for i in range(0, 4):
        n = random.randint(0, 9)
        random_numbers += str(n)
    return random_numbers
    
card_info = {}

while True:
    print('')
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    user_input = int(input())
    print('')
    if user_input == 1:
        print('Your card has been created')
        print('Your card number:')
        card_info['card_number'] = int(generate_card_number())
        print(card_info['card_number'])
        print('Your card PIN:')
        card_info['pin_number'] = int(generate_pin())
        print(card_info['pin_number'])
    elif user_input == 2:
        print('Enter your card number:')
        card_input_number = int(input())
        print('Enter your PIN:')
        pin_input_number = int(input())
        if card_info['card_number'] == card_input_number and card_info['pin_number'] == pin_input_number:
            print('')
            print('You have successfully logged in!')
            while True:
                print('')
                print('1. Balance') 
                print('2. Log out')
                print('0. Exit')
                print('')
                user_input_2 = int(input())
                if user_input_2 == 1:
                    print('Balance: 0')
                elif user_input_2 == 2:
                    print('You have successfully logged out!')
                    break
                elif user_input_2 == 0:
                    exit()
        else:
            print('')
            print('Wrong card number or PIN!')    
    elif user_input == 0:
        print('Bye!')
        exit()
