from stats import word_count, char_count


def main():
    FRANK = r"books/frankenstein.txt"
    book_text = get_book_text(FRANK)
    wc = word_count(book_text)
    print(f"Found {wc} total words")

    chars = char_count(book_text)
    print(chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
