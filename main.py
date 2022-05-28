# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from collections import Counter
import re

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as handle:
        content = handle.read()
    return content

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    result = Counter(text.split())
    return dict(result)
