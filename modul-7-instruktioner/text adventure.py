def get_command(prompt, valid_commands):
    print(prompt)
    print("Available commands:")
    for command in valid_commands:
        print(f"- {command}")

    while True:
        command = input("\n> ").strip().lower()
        if command in valid_commands:
            return command
        print("\nInvalid command.")
        print(f"Try: {', '.join(valid_commands)}")


def scene_confrontation():
    print("\nYou unlock the door and step inside.")
    print("A man lurks in the shadows with a shotgun pointed at you.")
    print('\n???: "Care to explain yourself?"')

    command = get_command(
        "\nWhat do you say?",
        ["say lost", "be rude", "run away"],
    )

    if command == "say lost":
        print('\nMan: "Lost, in the middle of the night?"')
        print('Man: "Hmm... I will allow you to call someone."')

        command = get_command(
            "\nWho do you call?",
            ["call girlfriend", "call police"],
        )

        if command == "call girlfriend":
            print("\nThe phone rings, but she doesn't answer.")
            print('Man: "So you tried to trick me huh?"')
            print("The man pushes you out of his home.")
            return "lose"

        print("\nPolice trace your location and rescue you.")
        print("Congratulations! You achieved the 'Flawless' ending.")
        return "win"

    if command == "be rude":
        print('\nMan: "Wrong answer son."')
        print("The man pushes you out of his home.")
        return "lose"

    print("\nYou sprint back into the forest.")
    return "lose"


def scene_shed(inventory):
    print("\nYou walk toward the shed.")
    print("You notice a key hidden under the carpet.")

    while True:
        command = get_command(
            "\nWhat do you do?",
            ["take key", "knock door", "inventory", "open door"],
        )

        if command == "inventory":
            print(f"\nInventory: {inventory}")
            continue

        if command == "knock door":
            print("\nYou knock, but nobody answers.")
            print("The only option seems to be taking the key.")
            continue

        if command == "take key":
            if "key" not in inventory:
                inventory.append("key")
                print("\nYou take the key.")
                print(f"Inventory: {inventory}")
            else:
                print("\nYou already have the key.")
            continue

        if command == "open door":
            if "key" not in inventory:
                print("\nYou try the door, but it is locked.")
                print("You need the key first.")
                continue
            return scene_confrontation()

    return "lose"


def scene_backtrack():
    print("\nYou decide to backtrack deeper into the forest.")
    print("After a long walk, you notice a faint light.")

    command = get_command(
        "\nWhat do you do?",
        ["investigate light", "avoid light"],
    )

    if command == "avoid light":
        print("\nYou continue walking.")
        print("Hours later, you find a road.")
        print("A truck driver notices you and offers help.")
        print("Congratulations! You achieved the 'Lucky Escape' ending.")
        return "win"

    print("\nYou approach the light.")
    print("It turns out to be an abandoned car with its headlights on.")

    command = get_command(
        "\nWhat do you do?",
        ["search car", "call for help", "leave area"],
    )

    if command == "call for help":
        print("\nNobody answers.")
        print("The car battery dies, leaving you in darkness.")
        return "lose"

    if command == "leave area":
        print("\nYou wander deeper into the woods.")
        return "lose"

    print("\nYou find a phone with 2% battery.")
    command = get_command(
        "\nWho do you call?",
        ["call emergency", "call girlfriend"],
    )

    if command == "call girlfriend":
        print("\nThe phone dies before the call connects.")
        print("You hear footsteps nearby.")
        return "lose"

    print("\nEmergency services track your location.")
    print("Rescue teams find you.")
    print("Congratulations! You achieved the 'Survivor' ending.")
    return "win"


def game():
    inventory = []

    print("\nYou are lost in a forest late at night.")
    print("The wind howls through the trees.")

    command = get_command(
        "\nWhat do you do?",
        ["go shed", "go back"],
    )

    if command == "go back":
        return scene_backtrack()

    return scene_shed(inventory)


if __name__ == "__main__":
    while True:
        result = game()
        if result == "win":
            print("\nGAME OVER")
            break
        print("\nYou failed. Restarting game...\n")