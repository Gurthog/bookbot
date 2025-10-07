import sys

from stats import (
    word_count,
    char_count,
    sort_dict_by_value,
)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[-1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    wc = word_count(book_text)
    print(f"Found {wc} total words")

    print("--------- Character Count -------")
    chars_dict = char_count(book_text)
    sorted_dicts = sort_dict_by_value(chars_dict)
    for d in sorted_dicts:
        if d["char"].isalpha():
            print(f"{d["char"]}: {d["num"]}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
