from nltk.corpus import brown
from collections import Counter
from sys import argv

# treshold: the k, slice: n
def find_first_occurences(treshold: int, slice: int) -> tuple:
    words = Counter()

    for word in brown.words()[0:slice]:
        words[word.lower()] += 1
    
    filtered = filter(lambda w: words[w] >= treshold, words)
    return list(filtered)

if __name__ == "__main__":
    if len(argv) < 3:
        print("Not enough arguments, expects 2 after script name: [threshold] [first N words]")
    else:
        k = int(argv[1])
        n = int(argv[2])

        for w in find_first_occurences(k,n):
            print(w)