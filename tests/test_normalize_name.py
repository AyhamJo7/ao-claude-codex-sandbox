import pytest

from normalize_name import normalize_name


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Ada Lovelace", "Ada Lovelace"),
        ("", ""),
        ("   ", ""),
        ("\tAda\tLovelace\t", "Ada Lovelace"),
        ("Ada    Lovelace", "Ada Lovelace"),
        ("  Ada \t  King \n Lovelace  ", "Ada King Lovelace"),
    ],
)
def test_normalize_name(raw: str, expected: str) -> None:
    assert normalize_name(raw) == expected
