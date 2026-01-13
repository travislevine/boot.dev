def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def text_accept(text):
    str_text = text.split()
    return f"Found {len(str_text)} total words"

def main():
    print()
    print(text_accept(get_book_text("/home/pepso/workspace/bootdotdev/bookbot/books/frankenstein.txt")))

main()