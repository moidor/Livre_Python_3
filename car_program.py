menu = ('''
start - to start the car
stop - to stop the car
quit - exit
''')
help = input('Display the menu : ')
if help == "help":
    print(menu)

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        # started ici veut dire True, donc "si la voiture est bien démarrée"
        if started:
            print('The car is already started...')
        else:
            started = True
            print("The car started... Ready to go !")
    elif command == "stop":
        if not started:
            print("The car is already stopped...")
        else:
            started = False
            print("The car stopped")
    elif command == "quit":
        print("Bye bye...")
        break
    else:
        print('Sorry, what did you mean ?')