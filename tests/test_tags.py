import pytest

from tags import parse_tags


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("alpha,beta,gamma", ["alpha", "beta", "gamma"]),
        ("  alpha ,\tbeta\n, gamma ", ["alpha", "beta", "gamma"]),
        ("single", ["single"]),
    ],
)
def test_normal_values(raw: str, expected: list[str]) -> None:
    assert parse_tags(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Straße, STRASSE", ["Straße"]),
        ("STRASSE, Straße", ["STRASSE"]),
        ("ǅ, ǆ", ["ǅ"]),
    ],
)
def test_unicode_casefold_dedupe(raw: str, expected: list[str]) -> None:
    assert parse_tags(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        (" Hello   world, hello world ", ["Hello world"]),
        ("a \t b,  c\n\nd", ["a b", "c d"]),
        ("hello world, hello\tworld", ["hello world"]),
    ],
)
def test_repeated_whitespace(raw: str, expected: list[str]) -> None:
    assert parse_tags(raw) == expected


@pytest.mark.parametrize("raw", ["", "   ", ",", " , , ", ",,,", "\t,\n"])
def test_empty_inputs(raw: str) -> None:
    assert parse_tags(raw) == []


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("Alpha, beta, ALPHA, gamma", ["Alpha", "beta", "gamma"]),
        ("b, a, B, A, b", ["b", "a"]),
        ("x,,x, ,X", ["x"]),
    ],
)
def test_duplicates_keep_first_spelling_and_order(raw: str, expected: list[str]) -> None:
    assert parse_tags(raw) == expected


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("alpha;beta", ["alpha;beta"]),
        ("alpha|beta, gamma", ["alpha|beta", "gamma"]),
        ("alpha beta", ["alpha beta"]),
        ("a;b, A;B", ["a;b"]),
    ],
)
def test_splits_on_commas_only(raw: str, expected: list[str]) -> None:
    assert parse_tags(raw) == expected
