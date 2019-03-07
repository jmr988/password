correctPassword = 'red'
password = input('Enter password: ')
count = 1

while (password != correctPassword):
    print('not correct')
    print('Youve attempted to enter the password: ', count, 'time(s)')
    count = count +1
    password = input('Enter password: ')
    
print('correct')


