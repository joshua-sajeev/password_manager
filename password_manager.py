from menu import menu, create, find, find_accounts

ADMIN_KEY = "ADMIN_KEY"
passw = input('Please provide the master password to start using the app: ')

if passw == ADMIN_KEY:
    print('You\'re in')

else:
    print('no luck')
    exit()

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find()
    else:
        choice = menu()
exit()
