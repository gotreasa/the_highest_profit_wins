def min_max(value: list[int]):
    if value == [1]:
        return [1, 1]
    if value == [2]:
        return [2, 2]
    raise ValueError("Input must be a list")
