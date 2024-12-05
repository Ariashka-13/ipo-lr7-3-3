import json

with open("stars.json", "r", encoding="UTF-8") as file:
    data = json.load(file)

def main():
  count = 0
  open = True

  def menu():
    print("""
    Меню:
    1 - Вывести все записи
    2 - Вывести запись по полю
    3 - Добавить запись
    4 - Удалить запись по полю
    5 - Выйти из программы
    """)

  def all():#Вывести все записи
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

  def polo():
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

  def add():
      global count 
      new_id = input("Введите новый id: ")
      for star in data:
        if star['id'] == new_id:
          print("Звезда уже добавлена")
          break
        else:
          new_name = str(input("Название звезды: "))
          new_constellation = str(input("Название созвездия: "))
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
      count += 1

  def delete():
      global count
      del_id = input("Введите id для удаления: ")
      for star in data:
        if star['id'] == del_id:
          data.remove(star)
          with open("stars.json", "w",encoding="UTF-8") as new_file:
              json.dump(data, new_file, ensure_ascii = False, indent=4)
          print("Запись удалена")
          break 
        else:
          print("Запись не найдена")
      count += 1
    
  def end():
      print("Выход из программы")
      print("Количество выполненных операций с записями: ", count)

  while open:
      menu()

      n = input("Введите номер пункта: ")

      if n == 1:
        all()
      elif n == 2:
        pole()
      elif n == 3:
        add()
      elif n == 4:
        delete()
      elif n == 5:
        end()
      else:
        print("Ошибка")

if __name__ == "__main__":
  main()
