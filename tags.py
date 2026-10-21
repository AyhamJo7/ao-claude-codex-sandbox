from normalize_name import normalize_name


def parse_tags(raw: str) -> list[str]:
    """Split on commas, normalize whitespace, drop empties, dedupe by casefold.

    The first occurrence's spelling and order are kept.
    """
    seen: dict[str, str] = {}
    for item in raw.split(","):
        tag = normalize_name(item)
        if tag:
            seen.setdefault(tag.casefold(), tag)
    return list(seen.values())
