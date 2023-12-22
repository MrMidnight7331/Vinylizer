# @Name: Vinylizer
# @Author: MrMidnight
# @Version: 7.8

import json
import random

def load_albums(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            if not content:
                return []
            albums = json.loads(content)
    except FileNotFoundError:
        albums = []
    except json.JSONDecodeError:
        print(f"Error decoding JSON_Config: {filename}.")
        albums = []
    return albums


def save_albums(filename, albums):
    with open(filename, 'w') as file:
        json.dump(albums, file, indent=None)


def print_albums(albums):
    if not albums:
        print("No albums available.")
    else:
        print("Available Albums:")
        for album in albums:
            print(f"- {album['name']}, Sides: {', '.join(album['sides'])}")


def randomize_sides(album):
    sides = list(album['sides'])
    random.shuffle(sides)
    return {"name": album['name'], "sides": sides}


def randomize_vinyl(albums):
    if not albums:
        print("No albums available. Add one with 'A'.")
        return None, None

    random_album = random.choice(albums)
    random_side = random.choice(random_album['sides'])

    return random_album['name'], random_side


def add_vinyl(albums, filename, name, num_sides):
    # Generate sides from A to the specified number
    sides = [chr(ord('A') + i) for i in range(num_sides)]

    # Add new vinyl
    new_album = {"name": name, "sides": sides}
    albums.append(new_album)
    save_albums(filename, albums)
    print(f"Album '{name}' with {num_sides} sides added successfully.\n")


def delete_vinyl(albums, filename, name):
    for album in albums:
        if album['name'] == name:
            albums.remove(album)
            save_albums(filename, albums)
            print(f"Album '{name}' deleted successfully!\n")
            return
    print(f"Album '{name}' not found.")


def list_all(albums):
    print_albums(albums)


if __name__ == "__main__":

    # Banner. Dont touch!
    print("o      'O                  o\nO       o o               O  o\no       O                 o\no       o                 O\nO      O' O  'OoOo. O   o o  O  ooOO .oOo. `OoOo.\n`o    o   o   o   O o   O O  o    o  OooO'  o\n `o  O    O   O   o O   o o  O   O   O      O\n  `o'     o'  o   O `OoOO Oo o' OooO `OoO'  o\nBy: MrMidnight          o\n                     OoO'                         \n")

    config_file = "config.json"

    albums_config = load_albums(config_file)

    while True:
        choice = input("Do you want to (R)andomly choose a Album, (A)dd a new one, (D)elete an album, (L)ist all albums, or (Q)uit? : ").upper()

        if choice == "R":
            random_album, random_side = randomize_vinyl(albums_config)
            if random_album is not None and random_side is not None:
                print(f"Randomly selected album: {random_album}, Random side: {random_side}\n")

        elif choice == "A":
            name = input("\nEnter the name of the new album: ")

            while True:
                try:
                    num_sides = int(input("Enter the number of sides for the new album: "))
                    break  # Break the loop if the input is a integer
                except ValueError:
                    print("\nInvalid input. Please enter a valid integer for the number of sides.")

            add_vinyl(albums_config, config_file, name, num_sides)

        elif choice == "D":
            name = input("\nEnter the name of the album to delete: ")
            delete_vinyl(albums_config, config_file, name)

        elif choice == "L":
            list_all(albums_config)
            print("")

        elif choice == "Q":
            print("\nQuitting Vinylizer.")
            break

        else:
            print("Invalid Input!")