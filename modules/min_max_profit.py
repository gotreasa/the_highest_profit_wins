def min_max(value: list[int]):
    if not isinstance(value, list):
        raise ValueError("Input must be a list")
    return [min(value), max(value)]
