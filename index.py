import json

def main():
    with open("stars.json", "r", encoding="UTF-8") as file:
        data = json.load(file)

    count = 0

    def menu():
        print("""
        Меню:
        1 - Вывести все записи
        2 - Вывести запись по полю
        3 - Добавить запись
        4 - Удалить запись по полю
        5 - Выйти из программы
        """)

    def info_star(star):
        return f"""
        Номер записи: {star['id']}, 
        Общее название звезды: {star['name']}, 
        Название созвездия: {star['constellation']}, 
        Можно ли увидеть звезду без телескопа: {star['is_visible']}, 
        Солнечный радиус звезды: {star['radius']},
        """

    def open_data_file():
        with open("stars.json", "w",encoding="UTF-8") as new_file:
            json.dump(data, new_file, ensure_ascii = False, indent=4)

    def all_stars(count):
        for star in data:
            print(info_star(star))
        return count + 1

    def search_stars(count):
        while True:
            search = input("Введите id: ")
            if search.isdigit():
                break
            else:
                print("Некорректный ввод")

        found = False
        for star in data:
            if star['id'] == search:
                print(info_star(star))
                found = True
                break
        if not found:
            print("Не найдено")
        return count + 1

    def add_stars(count):
        while True:
            new_id = input("Введите id: ")
            if new_id.isdigit():
                break
            else:
                print("Некорректный ввод")

        if [star for star in data if star['id'] == new_id]:
            print("Звезда уже добавлена")
        else:
            new_name = input("Название звезды: ")
            new_constellation = input("Название созвездия: ")

            while True:
                new_is_visible = input("Можно ли увидеть звезду без телескопа(True/False): ").lower()
                if new_is_visible in ['true', 'false']:
                    new_is_visible = new_is_visible == 'true'
                    break
                else:
                    print("Некорректный ввод")

            while True:
                new_radius = input("Солнечный радиус звезды: ")
                if new_radius.isdigit():
                    new_radius = float(new_radius)
                    break
                else:
                    print("Некорректный ввод")

            new_star = {
                "id": new_id,
                "name": new_name,
                "constellation": new_constellation,
                "is_visible": new_is_visible,
                "radius": new_radius
            }

            data.append(new_star)
            open_data_file()
            print("Запись добавлена")
        return count + 1

    def delete_stars(count):
        while True:
            del_id = input("Введите id для удаления: ")
            if del_id.isdigit():
                break
            else:
                print("Некорректный ввод")

        star_list = [star for star in data if star['id'] == del_id]
        if star_list:
            data.remove(star_list[0])
            open_data_file()
            print("Запись удалена")
        else:
            print("Запись не найдена")
        return count + 1

    def end(count):
        print("Выход из программы")
        print("Количество выполненных операций с записями: ", count)
        return False

    while True:
        menu()
        n = input("Введите номер пункта: ")
        if n.isdigit():
            n = int(n)
            if n == 1: 
                count = all_stars(count) 
            elif n == 2: 
                count = search_stars(count) 
            elif n == 3: 
                count = add_stars(count) 
            elif n == 4: 
                count = delete_stars(count) 
            elif n == 5: 
                count = end(count) 
            else: print("Ошибка: введите число из пункта") 
        else: print("Ошибка: введите числовое значение")

if __name__ == "__main__":
    main()
