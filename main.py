import random
import string

password = int(input('How long do you want your password to be? '))

print('''   Choose what your password consists of.
            1. Digits
            2. Letters 
            3. Special charecters
            4. To generate password

''')

password_list = ''

while True:
    choice = int(input('Pick a number: '))
    if choice == 1:
        password_list += string.ascii_letters
    elif choice == 2:
        password_list += string.digits
    elif choice == 3:
        password_list += string.punctuation
    elif choice == 4:
        break
    else:
        print('You must pick an option from the list above.')

password1 = []

for i in range(password):
    randompass = random.choice(password_list)
    password1.append(randompass)

print('Your random password is:' + ''.join(password1))