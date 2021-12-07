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
import json


def main():
    json_str = input()
    try:
        prev_result = {}
        cur_result = json.loads(json_str)
        while prev_result != cur_result:
            prev_result = cur_result
            cur_result = {}
            for key in prev_result.keys():
                if type(prev_result[key]) in [list, tuple] and len(prev_result[key]) != 0:
                    for i in range(len(prev_result[key])):
                        cur_result['.'.join([key, str(i)])] = prev_result[key][i]
                    continue
                if type(prev_result[key]) == dict and prev_result[key] != {}:
                    for small_key in prev_result[key].keys():
                        cur_result['.'.join([key, str(small_key)])] = prev_result[key][small_key]
                    continue
                cur_result[key] = prev_result[key]
        print(cur_result)
    except json.decoder.JSONDecodeError:
        print("{}")
        return


if __name__ == "__main__":
    main()
