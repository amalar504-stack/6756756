while True:
    print("1 - Додати альбом")
    print("2 - Переглянути всі")
    print("3 - Пошук за виконавцем")
    print("4 - Видалити альбом")
    print("5 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Назва альбому: ")
        artist = input("Виконавець: ")
        year = input("Рік: ")

        with open("music_collection.txt", "a") as f:
            f.write(name + "," + artist + "," + year + "\n")

    elif choice == "2":
        with open("music_collection.txt", "r") as f:
            print(f.read())

    elif choice == "3":
        artist = input("Виконавець: ")
        with open("music_collection.txt", "r") as f:
            for line in f:
                if artist in line:
                    print(line)

    elif choice == "4":
        name = input("Назва альбому: ")

        with open("music_collection.txt", "r") as f:
            lines = f.readlines()

        with open("music_collection.txt", "w") as f:
            for line in lines:
                if name not in line:
                    f.write(line)

    elif choice == "5":
        break