def min_max(value: list[int]):
    if not isinstance(value, list):
        raise ValueError("Input must be a list")
    if not all(isinstance(item, int) for item in value):
        raise ValueError("Input must be a numbered list")
    return [min(value), max(value)]
