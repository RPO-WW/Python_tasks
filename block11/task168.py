from typing import List


def insert_between_same_sign(arr: List[int], n: int) -> List[int]:
    if not isinstance(arr, list):
        raise TypeError('arr must be a list')

    result: List[int] = []
    for i, value in enumerate(arr):
        result.append(value)
        if i + 1 < len(arr) and value != 0 and arr[i + 1] != 0 and value * arr[i + 1] > 0:
            result.append(n)
    return result


def parse_input_line(s: str) -> List[int]:
    s = s.strip()
    if not s:
        return []
    parts = [p for part in s.split(',') for p in part.split()]
    return [int(p) for p in parts]


if __name__ == '__main__':
    try:
        line = input('Введите массив (например: 1 2 -3 -4 5 -6 или 1,2,-3,-4,5,-6): ')
        arr = parse_input_line(line)
        n_line = input('Введите число для вставки между одноимённо-зарядными элементами (например: 0): ')
        n = int(n_line)
    except ValueError:
        print('Ошибка: ввод должен содержать целые числа, разделённые пробелами или запятыми.')
    else:
        print('До:', arr)
        res = insert_between_same_sign(arr, n)
        print('После:', res)
