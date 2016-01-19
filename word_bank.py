import random
__author__ = 'eric'
#
# Extract words from local dictionary files
#

NUM_NOUNS = 1525  # N
NUM_VERBS = 634  # V
NUM_ARTICLES = 4  # A
NUM_ADJECTIVES = 210  # J

NUM_ADVERBS = 331  # D
NUM_PREPOSITIONS = 70  # P
NUM_CONJUNCTIONS = 27  # C


def return_word(wordType):
    if wordType == "N":
        return get_word_from_file("NounBank", NUM_NOUNS)
    elif wordType == "V":
        return get_word_from_file("VerbBank", NUM_VERBS)
    elif wordType == "A":
        return get_word_from_file("ArticleBank", NUM_ARTICLES)
    elif wordType == "J":
        return get_word_from_file("AdjectiveBank", NUM_ADJECTIVES)
    elif wordType == "D":
        return get_word_from_file("AdverbBank", NUM_ADVERBS)
    elif wordType == "P":
        return get_word_from_file("PrepositionBank", NUM_PREPOSITIONS)
    elif wordType == "C":
        return get_word_from_file("ConjunctionBank", NUM_CONJUNCTIONS)
    else:
        return "NULL"


def get_word_from_file(file, size):
    fo = open(file, "rw")
    nrand = random.randint(0, size)
    for x in xrange(nrand):
        fo.readline()
    word = fo.readline()
    fo.close()
    return word.rstrip()