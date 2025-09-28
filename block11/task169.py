def move_first_to_last(arr):
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')

    if len(arr) <= 1:
        return arr

    first_element = arr.pop(0)
    arr.append(first_element)
    return arr


def parse_input_line(s: str):
    s = s.strip()
    if not s:
        return []
    # allow separators: spaces and/or commas
    parts = [p for part in s.split(',') for p in part.split()]
    return [int(p) for p in parts]


if __name__ == '__main__':
    try:
        line = input('Введите массив (например: 1 2 3 4 или 1,2,3,4): ')
        arr = parse_input_line(line)
    except ValueError:
        print('Ошибка: ввод должен содержать целые числа, разделённые пробелами или запятыми.')
    else:
        print('До:', arr)
        move_first_to_last(arr)
        print('После:', arr)
