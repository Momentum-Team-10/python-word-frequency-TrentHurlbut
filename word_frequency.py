STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string
import operator

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as text:
        content = text.read()
        formatted_content = content.replace(string.punctuation, "")
        cleaned_content = formatted_content.replace("-" , " ").replace("—", " ").replace(".", "").replace(",", "").replace(":", "").replace("'", "").replace('"', "").replace("-\n","").lower().split()

    keys = {}
    for word in cleaned_content:
        if word in STOP_WORDS:
            pass
        elif word not in keys:
            keys[word] = 1
        else:
            keys[word] += 1

    asterisk = '*'
    i = 0

    max_key_list = []
    max_value_list = []

    while i < 10:
        max_key = max(keys, key=keys.get)
        max_key_list.append(max_key)
        max_value_list.append(keys[max_key])
        keys.pop(max_key)
        i += 1

    float_length = len(max(max_key_list, key=len))

    zipped_maxxes = zip(max_key_list, max_value_list)

    for key, value in zipped_maxxes:
        print(f"{key.rjust(float_length)} | {value} {asterisk * value}")

    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path
    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
