from menu import menu, create, find, find_accounts,update,delete,show

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
        choice = menu()
    if choice == '2':
        find_accounts()
        choice = menu()
    if choice == '3':
        find()
        choice = menu()
    if choice == '4':
        update()
        choice = menu()
    if choice =='5':
        delete()
        choice = menu()
    if choice =='6':
        show()
        choice = menu()
    else:
        choice = menu()
exit()
