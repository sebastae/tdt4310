#!/usr/bin/env python3
from nltk.book import text9
from sys import argv

DEFAULT_WORD = "sunset"
DELIMITER = '.'
DEBUG = False

def find_sentence_by_word(text, word: str, start: int = 0) -> tuple:
    if len(text) == 0: return (-1, -1)
    try:
        index = text[start:].index(word)
    except ValueError as e: # NLTK raises ValueError if the word does not exist
        return (-1, -1)
  
    start_index = index + start
    end_index = index + start

    # Find start of word

    while start_index > 0 and DELIMITER not in text[start_index - 1]:
        start_index -= 1

    while end_index < len(text) and DELIMITER not in text[end_index]:
        end_index += 1

    return (start_index, end_index)

def find_all_sentences(text, word:str) -> list:
    sentences = []
    previous_end = 0
    MAX_COUNT = 10000 # Guard against infinite loop
    count = 0
    while previous_end >= 0 and count < MAX_COUNT:
        start, end = find_sentence_by_word(text, word, previous_end)
        count += 1
        if start != -1:
            sentences.append((start, end))
            previous_end = end + 1
        else: break
    return sentences


if __name__ == "__main__":
    if(len(argv) > 1):
        sentences = find_all_sentences(text9, argv[1])
        for start, end in  sentences:
           if DEBUG: print(f"({start}, {end}): [{text9[max(0, start - 1)]}] {' '.join(text9[start:end])} [{text9[end]}]")
           else: print(' '.join(text9[start:end]))
        if len(sentences) == 0: print(f"'{argv[1]}' is not in '{text9.name}'")
           
        if DEBUG: print(f"[Total words: {len(text9)}]")
    else:
        start, end = find_sentence_by_word(text9, DEFAULT_WORD)
        if start == -1 or end == -1:
            raise IOError(f"'{DEFAULT_WORD}' is not in '{text9.name}'")
        else:
            print(" ".join(text9[start:end]))