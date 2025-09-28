from typing import List


def insert_numbers(arr: List[int], n: int, m: int) -> List[int]:
    # First pass: insert n before elements greater than n
    first_pass: List[int] = []
    for x in arr:
        if x > n:
            first_pass.append(n)
        first_pass.append(x)

    # Second pass: insert m after elements less than m
    second_pass: List[int] = []
    for x in first_pass:
        second_pass.append(x)
        if x < m:
            second_pass.append(m)

    return second_pass


def parse_input_line(s: str) -> List[int]:
    s = s.strip()
    if not s:
        return []
    parts = [p for part in s.split(',') for p in part.split()]
    return [int(p) for p in parts]


if __name__ == '__main__':
    try:
        line = input('Введите массив (например: 1 2 3 4 или 1,2,3,4): ')
        arr = parse_input_line(line)
        n = int(input('Введите n: '))
        m = int(input('Введите m: '))
    except ValueError:
        print('Ошибка: ввод должен содержать целые числа, разделённые пробелами или запятыми.')
    else:
        print('До:', arr)
        result = insert_numbers(arr, n, m)
        print('После:', result)
