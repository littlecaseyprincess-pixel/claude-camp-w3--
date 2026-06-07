from string_utils import reverse_words, count_vowels, is_palindrome


def test_reverse_words_normal():
    assert reverse_words("hello world") == "world hello"


def test_reverse_words_empty():
    assert reverse_words("") == ""


def test_reverse_words_extra_spaces():
    assert reverse_words("hello   world") == "world hello"


def test_count_vowels_normal():
    assert count_vowels("hello") == 2


def test_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5


def test_count_vowels_empty():
    assert count_vowels("") == 0


def test_is_palindrome_true():
    assert is_palindrome("level") is True


def test_is_palindrome_with_spaces():
    assert is_palindrome("A man a plan a canal Panama") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False