def get_neighbours(i: int, j: int, size_x: int, size_y: int) -> list[tuple]:
    # given an n * m matrix, find the neighbours (up, down, left, right) for [i, j] cell:
    result = []
    if j - 1 >= 0:
        result.append((i, j - 1))
    if j + 1 < size_y:
        result.append((i, j + 1))
    if i - 1 >= 0:
        result.append((i - 1, j))
    if i + 1 < size_x:
        result.append((i + 1, j))
    return result
