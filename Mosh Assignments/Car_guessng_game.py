command = ""
started = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print( "Car is already Started!")
        else:
            started = True
            print( "Car Started, Let's Go")
    elif command == "stop":
        if not started:
            print( "Car is already stopped!")
        else:
            started = False
            print("Car Stopped")
    elif command == "help":
        print("""
Stop - To stop the car
Start - To start the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I dont understand that!")