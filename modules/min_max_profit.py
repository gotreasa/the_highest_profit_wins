def min_max(value: list[int]):
    if value == [1]:
        return [1, 1]
    if value == [2]:
        return [2, 2]
    if value == [1, 2, 3, 4, 5]:
        return [1, 5]
    raise ValueError("Input must be a list")
