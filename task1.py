"""
Дан json cо вложенной структурой. Необходимо убрать вложенность и конвертировать структуру данных в словарь без сложенных структур.
На вход подается строка в формате json. На выходе ожидается полученный словарь. Словарь нужно выводить отсортированным по ключам. Например:

{"list": [1, 2, 3]}
{'list.0': 1, 'list.1': 2, 'list.2': 3}
{"a": {"a1": null,"a2": 2},"b": {"b1": "12","b2": 1.2}}
{'a.a1': None, 'a.a2': 2, 'b.b1': '12', 'b.b2': 1.2}

Если встретился пустой список или словарь, тогда значение сохраняется.

{"empty_dict": {}, "empty_list": []}
{'empty_dict': {}, 'empty_list': []}

Если на вход подается невалидный json, то нужно выдавать пустой словарь {}.
Задачу нужно решать не через рекурсию. Решения через рекурсию засчитываться не будут.

Sample Input:
{"list": [1, 2, 3]}
Sample Output:
{'list.0': 1, 'list.1': 2, 'list.2': 3}

"""
import os
import json

from collections import deque


def depth(d):
    """Узнаем глубину словаря"""
    queue = deque([(id(d), d, 1)])
    memo = set()
    while queue:
        id_, o, level = queue.popleft()
        if id_ in memo:
            continue
        memo.add(id_)
        if isinstance(o, dict):
            queue += ((id(v), v, level + 1) for v in o.values())
    return level


def main():
    json_str = os.system.read()
    try:
        json_obj = json.loads(json_str)
        # ???????????
    except json.decoder.JSONDecodeError:
        print("{}")
        return


if __name__ == "__main__":
    main()
