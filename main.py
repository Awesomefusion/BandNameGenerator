# Band Name Generator
def band_name_generator():
    print("Hello! Welcome to Band Name Generator.")
    city = input("What City did you grow up in?\n")
    pet = input("What is your pet's name?\n")
    print(f"Perhaps your band name could be {city} {pet}")


def main():
    band_name_generator()


if __name__ == '__main__':
    main()
