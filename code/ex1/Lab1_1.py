#!/usr/bin/env python3

import nltk
from collections import Counter

# Define "constants" for gender names
MALE = 'male'
FEMALE = 'female'
UNKNOWN = 'unknown'
BOTH = 'both'

# Create set of male words
MALE_WORDS = set([
    'guy','spokesman','chairman',"men's",'men','him',"he's",'his',
    'boy','boyfriend','boyfriends','boys','brother','brothers','dad',
    'dads','dude','father','fathers','fiance','gentleman','gentlemen',
    'god','grandfather','grandpa','grandson','groom','he','himself',
    'husband','husbands','king','male','man','mr','nephew','nephews',
    'priest','prince','son','sons','uncle','uncles','waiter','widower',
    'widowers'
])

# Create set of female words
FEMALE_WORDS = set([
    'heroine','spokeswoman','chairwoman',"women's",'actress','women',
    "she's",'her','aunt','aunts','bride','daughter','daughters','female',
    'fiancee','girl','girlfriend','girlfriends','girls','goddess',
    'granddaughter','grandma','grandmother','herself','ladies','lady',
    'lady','mom','moms','mother','mothers','mrs','ms','niece','nieces',
    'priestess','princess','queens','she','sister','sisters','waitress',
    'widow','widows','wife','wives','woman'
])

# Define a function that takes a list of words as argument
def genderize(words):

    # Store the size of the set of intersections between the words passed as arguments and the words in the male word set
    # i.e how many of the provided words are male words
    mwlen = len(MALE_WORDS.intersection(words))

    # Same as above but for female words
    fwlen = len(FEMALE_WORDS.intersection(words))

    if mwlen > 0 and fwlen == 0:
        return MALE # Returns "male" if only male words are found 
    elif mwlen == 0 and fwlen > 0:
        return FEMALE # Returns "female" if only female words are found
    elif mwlen > 0 and fwlen > 0:
        return BOTH # Returns "both" if both male and female words are found
    else:
        return UNKNOWN # Otherwise, if none of the words provided are in either the MALE_WORDS of FEMALE_WORDS sets return "unknown"

# Defines a function that takes in a list of sentences (as defined by nltks recommended tokenizer, delimited by punctuation marks)
def count_gender(sentences):

    # Define two counters
    sents = Counter()
    words = Counter()

    for sentence in sentences:

        # Find genders in each sentence
        gender = genderize(sentence)
        # Count the number of sentences with this gender by increasing the sentence counter by one
        sents[gender] += 1
        # Count the number of words in sentences with the gender of the sentence
        words[gender] += len(sentence)

    # Return a tuple with the sentence counter and the word counter
    return sents, words

# Defines a function that takes a whole text as argument
def parse_gender(text):

    # Creates a 2D list of tokenize words in sentences in the provided text, converts all words to lowercase for simpler processing
    sentences = [
        [word.lower() for word in nltk.word_tokenize(sentence)]
        for sentence in nltk.sent_tokenize(text)
    ]

    # Count the gender words used
    sents, words = count_gender(sentences)

    # Count the total amount of words processed
    total = sum(words.values())

    # Calculate the percentage of the genders usage in the sentences and print them
    for gender, count in words.items():
        pcent = (count / total) * 100
        nsents = sents[gender]        
        print(
            "{:0.3f}% {} ({} sentences)".format(pcent, gender, nsents)
        )

# Runs when the file is run as an application
if __name__ == '__main__':
    # Read the file "sample.txt" in the current directory
    with open('sample.txt', 'r') as f:
        # Parse the content of the text file
        parse_gender(f.read())

# This application reads the file "sample.txt" and finds the percentage of sentences talking about males, females, both or none of them
# It does this by definig a list of contextual female and male words andd then finding the intersections between the words in each
# sentence and the male/female "dictionaries"