def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count


def is_palindrome(s):
    text = s.lower().replace(" ", "")
    return text == text[::-1]