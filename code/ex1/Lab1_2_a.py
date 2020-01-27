from nltk.book import text9 as text

WORD = "sunset"

if __name__ == "__main__":
    index = text.index(WORD)
    sentence_end_offset = text[index:].index(".")
    sentence_start_offset = text[index:0:-1].index(".")

    print(" ".join(text[index - sentence_start_offset + 1: index + sentence_end_offset + 1]))