"""
Дана строка, которая является абсолютным путем к файлу или директории в системе Unix.
Нужно упростить эту строку до каноничного пути.

Каноничный путь - это тот путь, который будет максимально простым и строгим, а именно:
1.	Путь начинается с единичного слеша /
2.	Любые две директории разделяются одиночным слешем
3.	Путь не может оканчиваться на /
4.	Путь может содержать только истинные директории к нужному файлу (то есть в пути не может быть '.' или '..')
На вход подается путь к файлу или директории в системе Unix.
На выходе ожидается каноничный путь.

Пример
абсолютный путь: /home/abc/../abc/file.txt
каноничный путь: /home/abc/file.txt

Программа должна возвращать упрощенный каноничный путь до файла или директории
Sample Input:
/../
Sample Output:
/
"""
import sys


class MyTrip:
    """Класс для помощи"""

    def __init__(self):
        self._root_list = []

    def add(self, value: str) -> None:
        """Добавление данных"""
        if value.startswith(".."):
            if len(self._root_list) != 0:
                self._root_list.pop(-1)
            return
        if value.startswith(".") or value.startswith("\\"):
            return

        self._root_list.append(value)

    @property
    def root_list(self):
        if len(self._root_list) == 0:
            return "/"
        return "/".join(self._root_list)


def main():
    input_str = sys.stdin.read()
    # Фильтруем на пустые значения
    data_list = [e for e in input_str.split("/") if e != ""]

    # Создаем экзампляр класса
    trip = MyTrip()

    # Добавляем директории
    for path in data_list:
        trip.add(path)

    # Выводим результат
    print(trip.root_list)


if __name__ == "__main__":
    main()
