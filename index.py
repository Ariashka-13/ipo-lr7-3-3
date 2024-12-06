import json

def main():
    with open("stars.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    global count
    count = 0
    open_programme = True

    def menu():
        print("""
        Меню:
        1 - Вывести все записи
        2 - Вывести запись по полю
        3 - Добавить запись
        4 - Удалить запись по полю
        5 - Выйти из программы
        """)

    def all_stars():
        global count
        for star in data:
            print(f"""
            Номер записи: {star['id']},
            Общее название звезды: {star['name']},
            Название созвездия: {star['constellation']},
            Можно ли увидеть звезду без телескопа: {star['is_visible']},
            Солнечный радиус звезды: {star['radius']},
            """)
        count += 1

    def search_stars():
        global count
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

    def add_stars():
        global count
        new_id = input("Введите id: ")
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
                with open("stars.json", "w",encoding="UTF-8") as new_file:
                  json.dump(data, new_file, ensure_ascii = False, indent=4)
                print("Запись добавлена")
                break
        count += 1
    
    def delete_stars():
        global count
        del_id = int(input("Введите id для удаления: "))
        for star in data:
            if star['id'] == del_id:
                data.remove(star)
                with open("stars.json", "w",encoding="UTF-8") as new_file:
                    json.dump(data, new_file, ensure_ascii = False, indent=4)
                print("Запись удалена")
                break
            else:
                print("Запись не найдена")
                break
        count += 1

    def end():
        print("Выход из программы")
        print("Количество выполненных операций с записями: ", count)
        open_programme = False

    while open_programme:
        menu()

        n = input("Введите номер пункта: ")
        if n.isdigit():
            n = int(n)
            if n == 1:
                all_stars()
            elif n == 2:
                search_stars()
            elif n == 3:
                add_stars()
            elif n == 4:
                delete_stars()
            elif n == 5:
                end()
            else:
                print("Ошибка")
        else:
            print("Ошибка: введите числовое значение")

if __name__ == "__main__":
    main()
