def normalize_name(name: str) -> str:
    """Strip outer whitespace and collapse internal whitespace runs to one space."""
    return " ".join(name.split())
