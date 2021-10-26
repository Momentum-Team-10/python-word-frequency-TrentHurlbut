STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

"""Two packages imported. I definitely used string, I don't think I used operator. Too afraid to delete now."""
import string
import operator

"""Function which takes a text file and provides a printout of the most used words and their counts."""
def print_word_freq(file):
    
    """This section opens the text file, removes all punctuation, converts it to lowercase, and then to a list of each word."""
    with open(file) as text:
        content = text.read()
        formatted_content = content.replace(string.punctuation, "")
        cleaned_content = formatted_content.replace("-" , " ").replace("—", " ").replace(".", "").replace(",", "").replace(":", "").replace("'", "").replace('"', "").replace("-\n","").lower().split()

    """This block creates a dictionary which stores each word as a key and the amount of times it is used in the .txt document as the corresponding value."""
    keys = {}
    for word in cleaned_content:
        if word in STOP_WORDS:
            pass
        elif word not in keys:
            keys[word] = 1
        else:
            keys[word] += 1

    """These variables are both declared for use in the final printing process."""
    asterisk = '*'
    i = 0

    """These two lists are used to store the top 10 words by usage number (max_key_list) and the amount they were used (max_value_list)."""
    max_key_list = []
    max_value_list = []

    """A loop that looks through the keys dictionary, finds the max value, records it to the respective 'max' lists, and then pops it from the dictionary."""
    while i < 10:
        max_key = max(keys, key=keys.get)
        max_key_list.append(max_key)
        max_value_list.append(keys[max_key])
        keys.pop(max_key)
        i += 1

    """This establishes the space required (matching the length of the longest word in the top-10) for the right alignment so everything looks nice."""
    float_length = len(max(max_key_list, key=len))

    """Zipping both max lists together so they can be iterated over simultaneously."""
    zipped_maxxes = zip(max_key_list, max_value_list)

    """Iterating over both max lists and passing the respective values to produce the desired print strings."""
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
