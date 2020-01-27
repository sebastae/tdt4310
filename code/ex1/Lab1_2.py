from nltk.book import text9
from sys import argv
from pprint import pprint

DEFAULT_WORD = "sunset"

def find_sentence_by_word(text, word: str, start: int = 0) -> tuple:
    try:
        word_index = text[start:].index(word)
    except ValueError as e: # NLTK raises ValueError if the word does not exist
        return (-1, -1)
    try:
        end_offset = text[start + word_index:].index(".")
    except ValueError as e:
        end_offset = len(text[start + word_index:] - 1)
    
    try:
        start_offset = text[word_index:0:-1].index(".")
    except ValueError as e:
        start_offset = len(text[])

    return (word_index - start_offset + 1, word_index + end_offset + 1)

def find_all_sentences(text, word:str) -> list:
    sentences = []
    previous_end = 0
    while True:
        sent = find_sentence_by_word(text, word, previous_end)
        if start == -1:
            break
        sentences.append(sent)
        previous_end = sent[1]
        


if __name__ == "__main__":
    if(len(argv) > 1):
        pass
    else:
        start, end = find_sentence_by_word(text9, DEFAULT_WORD)
        if start == -1 or end == -1:
            raise IOError(f"'{DEFAULT_WORD}' is not in the provided text")
        else:
            print(" ".join(text9[start:end]))