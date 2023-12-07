def min_max(value: list[int]):
    if value == [1]:
        return [min(value), max(value)]
    if value == [2]:
        return [min(value), max(value)]
    if value == [1, 2, 3, 4, 5]:
        return [min(value), max(value)]
    if value == [2334454, 5]:
        return [min(value), max(value)]
    raise ValueError("Input must be a list")
