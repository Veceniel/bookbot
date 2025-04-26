# Here's my stats.py
def word_count(text):
    return len(text.split())

def letter_count(body):
    lowered = body.lower()
    num_chars = {}
    for char in lowered:
        if char in num_chars:
            num_chars[char] += 1
        else:
            num_chars[char] = 1
    return num_chars

def sort_on(dict):
    return dict["num"]

def sort_chars(chars):
    sorted = []
    for char in chars:
        char_count = {}
        char_count["char"] = char
        char_count["num"] = chars[char]
        sorted.append(char_count)
    sorted.sort(reverse = True, key = sort_on)
    return sorted
