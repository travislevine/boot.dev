from stats import text_word_count
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    print()
    print(text_word_count(get_book_text("/home/pepso/workspace/bootdotdev/bookbot/books/frankenstein.txt")))

main()