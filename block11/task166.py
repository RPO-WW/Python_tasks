from typing import List


def bisect_insert(heights: List[int], new_height: int) -> None:
    left, right = 0, len(heights)
    while left < right:
        mid = (left + right) // 2
        # For a descending list we move right when mid value is less than new value
        if heights[mid] < new_height:
            right = mid
        else:
            left = mid + 1
    heights.insert(left, new_height)


def insert_by_values_efficient(heights: List[int], new_height1: int, new_height2: int) -> List[int]:
    if new_height1 > new_height2:
        bisect_insert(heights, new_height1)
        bisect_insert(heights, new_height2)
    else:
        bisect_insert(heights, new_height2)
        bisect_insert(heights, new_height1)
    return heights


def parse_input_line(s: str) -> List[int]:
    s = s.strip()
    if not s:
        return []
    parts = [p for part in s.split(',') for p in part.split()]
    return [int(p) for p in parts]


if __name__ == '__main__':
    # Example usage: interactive prompt or default sample
    try:
        line = input('Введите список ростов через пробел или запятую (или Enter для примера): ').strip()
        if line:
            heights = parse_input_line(line)
        else:
            heights = [180, 175, 170, 165, 160]

        nh1_line = input('Введите первый новый рост (например: 172): ').strip()
        nh2_line = input('Введите второй новый рост (например: 168): ').strip()
        new_height1 = int(nh1_line) if nh1_line else 172
        new_height2 = int(nh2_line) if nh2_line else 168
    except ValueError:
        print('Ошибка: ввод должен содержать целые числа.')
    else:
        updated_heights = insert_by_values_efficient(heights, new_height1, new_height2)
        print('Результат:', updated_heights)
