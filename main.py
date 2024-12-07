import json

with open("stars.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

count = 0

while True:
    print("""
    Меню:
    1 - Вывести все записи
    2 - Вывести запись по полю
    3 - Добавить запись
    4 - Удалить запись по полю
    5 - Выйти из программы
    """)

    n = input("Введите номер пункта: ")

    if n.isdigit():
        n = int(n)
        if n == 1:  # Вывести все записи
            for star in data:
                print(f"""
                Номер записи: {star['id']},
                Общее название звезды: {star['name']},
                Название созвездия: {star['constellation']},
                Можно ли увидеть звезду без телескопа: {star['is_visible']},
                Солнечный радиус звезды: {star['radius']},
                """)
            count += 1

        elif n == 2:  # Вывести записи по полю
            search = input("Введите id: ")

            for i, star in enumerate(data):
                if star['id'] == search:
                    print(f"""
                Номер записи: {star['id']},
                Общее название звезды: {star['name']},
                Название созвездия: {star['constellation']},
                Можно ли увидеть звезду без телескопа: {star['is_visible']},
                Солнечный радиус звезды: {star['radius']},
                """)
                    print(f"Позиция в словаре: {i}")
                    break
            else:
                print("Не найдено")
            count += 1

        elif n == 3:  # Добавить запись
            new_id = int(input("Введите id: "))
            for star in data:
                if star['id'] == new_id:
                    print("Звезда уже добавлена")
                    break
            else:
                new_name = input("Название звезды: ")
                new_constellation = input("Название созвездия: ")
                new_is_visible = bool(input("Можно ли увидеть звезду без телескопа: "))
                new_radius = float(input("Солнечный радиус звезды: "))

                new_star = {
                    "id": new_id,
                    "name": new_name,
                    "constellation": new_constellation,
                    "is_visible": new_is_visible,
                    "radius": new_radius
                }

                data.append(new_star)
                with open("stars.json", "w", encoding="UTF-8") as new_file:
                    json.dump(data, new_file, ensure_ascii=False, indent=4)
                print("Запись добавлена")

            count += 1

        elif n == 4:  # Удалить запись по полю
            del_id = int(input("Введите id для удаления: "))
            for star in data:
                if star['id'] == del_id:
                    data.remove(star)
                    with open("stars.json", "w", encoding="UTF-8") as new_file:
                        json.dump(data, new_file, ensure_ascii=False, indent=4)
                    print("Запись удалена")
                    break
            else:
                print("Запись не найдена")
            count += 1

        elif n == 5:  # Выйти из программы
            print("Выход из программы")
            print("Количество выполненных операций с записями: ", count)
            break

        else:
            print("Ошибка: введенное число вне пункта")
    else:
        print("Ошибка: введите числовое значение")
