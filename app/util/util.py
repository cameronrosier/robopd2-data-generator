def empty_str_to_zero(value: str) -> int:
    """Return 0 if value is an empty string"""
    if not value:
        return 0
    return int(value)