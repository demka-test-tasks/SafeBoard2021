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

                #Если по ключу у нас list/tuple и значение не пустое
                if type(prev_result[key]) in [list, tuple] and len(prev_result[key]) != 0:
                    
                    #То запускаем цикл по всем элементам вложенной коллекции
                    for i in range(len(prev_result[key])):

                        #Получаем текущий элемент коллекции через индекс
                        current_element = prev_result[key][i]
                        
                        #Формируем новый ключ на основе ключа и индекса элемента коллекции
                        new_key = '.'.join([key, str(i)])
                        
                        #Присваиваем новый ключ и значение словарю
                        cur_result[new_key] = current_element
                    
                    continue

                #Если присутствует вложенный словарь и он не пустой
                if type(prev_result[key]) == dict and prev_result[key] != {}:

                    #Итерируемся по ключам вложенного словаря
                    for sub_key in prev_result[key].keys():

                        #Получаем текущий элемент коллекции через sub_key
                        current_element = prev_result[key][sub_key]

                        # Формируем новый ключ на основе ключа и sub_key
                        new_key = '.'.join([key, str(sub_key)])

                        #Присваиваем новый ключ и значение словарю
                        cur_result[new_key] = current_element
                    
                    continue
                
                cur_result[key] = prev_result[key]
        
        print(cur_result)

    #Если на вход некорректный json
    except json.decoder.JSONDecodeError:
        print("{}")
        return

if __name__ == "__main__":
    main()
