def get_word_count(text):
    str_text = text.split()
    return f"Found {len(str_text)} total words"

def get_chars_dict(text):
    lower_text = text.lower()
    char_counts = {
    }
    for char in lower_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts