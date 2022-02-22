command = ""
started = False

while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('car is already started.')
        else:
            started = True
            print('car is started...')
    elif command == 'stop':
        if not started:
            print('car stopped...')
        else:
            started = False
            print('car is already stopped.')
    elif command == 'help':
        print( '''
            press <start> to start the game
            press <stop> to stop the game
            press <quit> to quit the game
        ''')
        break
    elif command == 'quit':
       break
    else:
        print("Invalid input..")
    

