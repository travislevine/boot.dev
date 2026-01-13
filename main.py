from stats import get_word_count, get_chars_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    print()
    print(get_word_count(get_book_text("/home/pepso/workspace/bootdotdev/bookbot/books/frankenstein.txt")))
    print(get_chars_dict(get_book_text("/home/pepso/workspace/bootdotdev/bookbot/books/frankenstein.txt")))


main()