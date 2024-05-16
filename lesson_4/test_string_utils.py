import pytest
from strings_utils import StringUtils


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        ("b", "B"),
        ("skypro", "Skypro"),
        ("скайпро", "Скайпро"),
        ("skypro skypro", "Skypro skypro"),
        ("777a", "777a"),
    ],
)
def test_positive_capitilize(in_string, out_string):
    example_string = StringUtils()
    result = example_string.capitilize(in_string)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        ("", ""),
        (" ", " "),
        ("!skypro", "!skypro"),
        (" skypro", " skypro"),
        ("SKYPRO", "Skypro"),
        ("S", "S"),
    ],
)
def test_negative_capitilize(in_string, out_string):
    example_string = StringUtils()
    result = example_string.capitilize(in_string)
    assert result == out_string


# @pytest.mark.xfail
# def test_negative_int_capitilize():
#     example_string = StringUtils()
#     with pytest.raises(AttributeError):
#         example_string.capitilize(123)


# @pytest.mark.parametrize("in_string", [(None)])
# def test_negative_none_capitilize(in_string):
#     example_string = StringUtils()
#     result = example_string.capitilize(in_string)
#     assert result is None


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        (" skypro", "skypro"),
        ("sky pro", "sky pro"),
        ("   ", ""),
    ],
)
def test_positive_trim(in_string, out_string):
    example_string = StringUtils()
    result = example_string.trim(in_string)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        ("", ""),
        ("skypro     ", "skypro     "),
    ],
)
def test_negative_trim(in_string, out_string):
    example_string = StringUtils()
    result = example_string.trim(in_string)
    assert result == out_string


# @pytest.mark.xfail
# def test_negative_int_trim():
#     example_string = StringUtils()
#     with pytest.raises(AttributeError):
#         example_string.trim(123)


@pytest.mark.parametrize(
    "in_string, out_string, delimiter",
    [
        ("s,k,y,p,r,o", ["s", "k", "y", "p", "r", "o"], ","),
        ("s:k:y", ["s", "k", "y"], ":"),
    ],
)
def test_positive_to_list(in_string, out_string, delimiter):
    example_string = StringUtils()
    result = example_string.to_list(in_string, delimiter)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string, delimiter",
    [("", [], ","), (",", ["", ""], ","), ("sky", ["sky"], ",")],
)
def test_negative_to_list(in_string, out_string, delimiter):
    example_string = StringUtils()
    result = example_string.to_list(in_string, delimiter)
    assert result == out_string


# @pytest.mark.xfail
# def test_negative_int_to_list():
#     example_string = StringUtils()
#     with pytest.raises(AttributeError):
#         example_string.to_list(123)


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [
        ("skypro", "s", True),
        ("sky$pro", "$", True),
        ("sky pro", " ", True),
    ],
)
def test_positive_contains(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.contains(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [("skypro", "t", False), ("skypro", "o", True), ("", "s", False), ("", "", True)],
)
def test_negative_contains(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.contains(in_string, symbol)
    assert result == out_string


# @pytest.mark.xfail
# def test_negative_int_contains(in_string, symbol):
#     example_string = StringUtils()
#     with pytest.raises(AttributeError):
#         example_string.contains(123, 2)


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [
        ("skypro", "sky", "pro"),
        ("sky pro sky", "sky", " pro "),
        ("sky pro", "sky pro", ""),
    ],
)
def test_positive_delete_symbol(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.delete_symbol(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [("skypro", "t", "skypro"), ("", "z", ""), ("z", "", "z"), (" ", " ", "")],
)
def test_negative_delete_symbol(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.delete_symbol(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [
        ("skypro", "s", True),
        ("Skypro", "s", False),
        ("skypro", "", True),
        (" ", " ", True),
        ("s", "s", True),
        ("", "", True),
    ],
)
def test_positive_starts_with(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.starts_with(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [
        ("skypro", "t", False),
        ("", "s", False),
        ("p", "o", False),
    ],
)
def test_negative_starts_with(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.starts_with(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [
        ("skypro", "o", True),
        ("skypro", "O", False),
        ("skypro", "", True),
        (" ", " ", True),
        ("s", "s", True),
        ("", "", True),
    ],
)
def test_positive_end_with(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.end_with(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, symbol, out_string",
    [
        ("skypro", "t", False),
        ("", "s", False),
        ("s", "k", False),
    ],
)
def test_negative_end_with(in_string, symbol, out_string):
    example_string = StringUtils()
    result = example_string.end_with(in_string, symbol)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        ("", True),
        ("   ", True),
        ("# comment", False),
    ],
)
def test_positive_is_empty(in_string, out_string):
    example_string = StringUtils()
    result = example_string.is_empty(in_string)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string",
    [
        ("skypro", False),
        ("   skypro", False),
    ],
)
def test_negative_is_empty(in_string, out_string):
    example_string = StringUtils()
    result = example_string.is_empty(in_string)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string, joiner",
    [
        (["s", "k", "y", "p", "r", "o"], "s, k, y, p, r, o", ", "),
        (["s", "k", "y"], "s:k:y", ":"),
        (["sky", "pro"], "sky, pro", ", "),
        ([1, 2, 3, 4, 5], "1, 2, 3, 4, 5", ", "),
        (["###, ###"], "###, ###", ", "),
        ([True, True], "True, True", ", "),
    ],
)
def test_positive_list_to_string(in_string, out_string, joiner):
    example_string = StringUtils()
    result = example_string.list_to_string(in_string, joiner)
    assert result == out_string


@pytest.mark.parametrize(
    "in_string, out_string, joiner",
    [
        ([], "", ","),
        (["s"], "s", ":"),
    ],
)
def test_negative_list_to_string(in_string, out_string, joiner):
    example_string = StringUtils()
    result = example_string.list_to_string(in_string, joiner)
    assert result == out_string


# @pytest.mark.parametrize(
#     "in_string, out_string",
#     [
#         (["s", "k", "y", "p", "r", "o"], "s, k, y, p, r, o"),
#         (["s", "k", "y"], "s, k, y",),
#         (["sky", "pro"], "sky, pro"),
#         ([1, 2, 3, 4, 5], "1, 2, 3, 4, 5"),
#         (["###, ###"], "###, ###"),
#         ([True, True], "True, True"),
#     ],
# )
# def test_positive_list_to_string(in_string, out_string):
#     example_string = StringUtils()
#     result = example_string.list_to_string(in_string)
#     assert result == out_string
