def has_valid_length(text:str, length:12) -> bool:
    """Check if text length is valid."""
    return len(text) == length

def is_decimal_on_indices(text:str, start:int, stop:int) -> bool:
    """Check if the first 3 digits are decimal."""
    return all([
        text[i].is_decimal() for i in range(start, stop)
    ])

def is_phonenumber(text:str) -> bool:
    """Check if text is a valid phone number."""

    is_valid = all((
        has_valid_length(text=text, length=12),
    ))

    return is_valid
