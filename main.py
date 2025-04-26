#Here's my main.py
from stats import word_count
from stats import letter_count

def get_book_text(file):
    return file.read()

def main():
    with open("./books/frankenstein.txt") as f:
        text = get_book_text(f)
        print(f"{word_count(text)} words found in the document")
        print(letter_count(text))

main()
