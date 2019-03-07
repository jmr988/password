correctPassword = 'bye'
password = input('Enter password: ')
count = 1
while (password != correctPassword):
    print('not correct')
    print('youve attempted to enter a password ',count, ' times')
    password = input('Enter password: ')

    count+=count

print('correct')


