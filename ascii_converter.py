while True:
    direction = input("\n>>>  Select an option:\n"
                      "[1]: character >>> number\n"
                      "[2]: character <<< number\n"
                      "1/2: ")
    if direction == "1":
        character = input("Type a character: ")
        if len(character) == 1:
            number = ord(character)
            if 0 <= number <= 127:
                print("The corresponding ASCII number is " + str(number) + ".")
            else:
                print("The corresponding Unicode number is " + str(number) + ".")
        else:
            print("That's not a character!")
    elif direction == "2":
        number = 0
        try:
            number = int(input("Type a number: "))
        except ValueError:
            print("That's not a number!")
            continue
        character = chr(number)
        if 0 <= number <= 127:
            print("The corresponding ASCII character is " + character + ".")
        elif 128 <= number <= 1114111:
            print("The corresponding Unicode character is " + character + ".")
        else:
            print("That's not a valid ASCII/Unicode number!")
    else:
        print("Exiting program...")
        break
