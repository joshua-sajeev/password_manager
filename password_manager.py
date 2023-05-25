from menu import menu, create, find, find_accounts,update,delete,show

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
        choice = menu()
    elif choice == '2':
        find_accounts()
        choice = menu()
    elif choice == '3':
        find()
        choice = menu()
    elif choice == '4':
        update()
        choice = menu()
    elif choice =='5':
        delete()
        choice = menu()
    elif choice =='6':
        show()
        choice = menu()
    else:
        choice = menu()
exit()
