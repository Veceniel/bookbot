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

