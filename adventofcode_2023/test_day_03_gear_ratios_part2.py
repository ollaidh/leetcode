import pathlib
import unittest


def file_to_list(input_path: str):
    symbols = []
    filepath_inp = pathlib.Path(__file__).parent.resolve() / 'inputs' / input_path
    with open(filepath_inp) as f:
        file_lines = f.readlines()
        for line in file_lines:
            line = line.rstrip()
            curr_line = []
            for letter in line:
                curr_line.append(letter)
            symbols.append(curr_line)
    return symbols


def get_numbers_right(symbol_x: int, symbol_y: int, size_x: int, size_y: int, matrix: list[list[str]]) -> list[int]:
    digits = '1234567890'
    result = []
    # check right:
    if symbol_y != size_y - 1:
        j = symbol_y + 1
        right_digits = []
        while j <= size_y - 1 and matrix[symbol_x][j] in digits:
            right_digits.append(matrix[symbol_x][j])
            matrix[symbol_x][j] = ' '
            j += 1
        if right_digits:
            result.append(int(''.join(right_digits)))
    return result


def get_numbers_left(symbol_x: int, symbol_y: int, size_x: int, size_y: int, matrix: list[list[str]]) -> list[int]:
    digits = '1234567890'
    result = []
    # check right:
    if symbol_y != 0:
        j = symbol_y - 1
        right_digits = []
        while j >= 0 and matrix[symbol_x][j] in digits:
            right_digits.append(matrix[symbol_x][j])
            matrix[symbol_x][j] = ' '
            j -= 1
        if right_digits:
            result.append(int(''.join(reversed(right_digits))))
    return result


def get_numbers_up_down(direction: str, symbol_x: int, symbol_y: int, size_x: int, size_y: int, matrix: list[list[str]]) -> list[int]:
    digits = '1234567890'
    result = []
    if (direction == 'up' and symbol_x != 0) or (direction == 'down' and symbol_x < size_x - 1):
        i_line = symbol_y
        if direction == 'up':
            i_line = symbol_x - 1
        else:
            i_line = symbol_x + 1

        if matrix[i_line][symbol_y] in digits:
            left, right = [], []
            j = symbol_y - 1
            while j >= 0 and matrix[i_line][j] in digits:
                left.append(matrix[i_line][j])
                matrix[i_line][j] = ' '
                j -= 1
            j = symbol_y
            while j < size_y and matrix[i_line][j] in digits:
                right.append(matrix[i_line][j])
                matrix[i_line][j] = ' '
                j += 1
            result.append(int(''.join(reversed(left)) + ''.join(right)))
        else:
            if symbol_y - 1 >= 0 and matrix[i_line][symbol_y - 1] in digits:
                j = symbol_y - 1
                left = []
                while j >= 0 and matrix[i_line][j] in digits:
                    left.append(matrix[i_line][j])
                    matrix[i_line][j] = ' '
                    j -= 1
                result.append(int(''.join(reversed(left))))
            if symbol_y + 1 < size_y and matrix[i_line][symbol_y + 1] in digits:
                j = symbol_y + 1
                right = []
                while j < size_y and matrix[i_line][j] in digits:
                    right.append(matrix[i_line][j])
                    matrix[i_line][j] = ' '
                    j += 1
                result.append(int(''.join(right)))

    return result


def gear(input_path: str):
    result = 0
    not_symbols = '1234567890. '

    matrix = file_to_list(input_path)
    size_x = len(matrix)
    size_y = len(matrix[0])
    for i in range(size_x):
        for j in range(size_y):
            if matrix[i][j] == "*":
                numbers = []
                numbers.extend(get_numbers_left(i, j, size_x, size_y, matrix))
                numbers.extend(get_numbers_right(i, j, size_x, size_y, matrix))
                numbers.extend(get_numbers_up_down('up', i, j, size_x, size_y, matrix))
                numbers.extend(get_numbers_up_down('down', i, j, size_x, size_y, matrix))
                if len(numbers) == 2:
                    result += numbers[0] * numbers[1]

    return result


if __name__ == '__main__':
    result = gear('input_day_03_gear_ratios.dat')
    print(result)
