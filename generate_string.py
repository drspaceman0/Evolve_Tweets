from __future__ import division
from word_bank import return_word
import random
import copy
__author__ = 'eric'

MIN_DNA_SIZE = 3  # len(OPTIMAL)
MAX_DNA_SIZE = 7
POP_SIZE = 50
GENERATIONS = 5000
DNA_SYMBOLS = ['N', 'V', 'A', 'J', 'D', 'P', 'C']
DNA_SYMBOLS_SIZE = 7


class Individual:
    def __init__(self, sent_struc):
        self.dna = sent_struc
        self.dna_size = len(self.dna)
        self.fit = -1
        self.tweet = ""
        self.noun_bank = []
        self.verb_bank = []
        self.adjective_bank = []
        self.article_bank = []
        self.adverb_bank = []
        self.preposition_bank = []
        self.conjunction_bank = []
        self.init_word_bank()
        self.init_tweet()

    def init_word_bank(self):
        self.noun_bank.append(return_word("N"))
        self.verb_bank.append(return_word("V"))
        self.article_bank.append(return_word("A"))
        self.adjective_bank.append(return_word("J"))
        self.adverb_bank.append(return_word("D"))
        self.preposition_bank.append(return_word("P"))
        self.conjunction_bank.append(return_word("C"))
        for c in xrange(0, len(self.dna)):
            if self.dna[c] == "N":
                self.noun_bank.append(return_word("N"))
            if self.dna[c] == "V":
                self.verb_bank.append(return_word("V"))
            if self.dna[c] == "A":
                self.article_bank.append(return_word("A"))
            if self.dna[c] == "J":
                self.adjective_bank.append(return_word("J"))
            if self.dna[c] == "D":
                self.adverb_bank.append(return_word("D"))
            if self.dna[c] == "P":
                self.preposition_bank.append(return_word("P"))
            if self.dna[c] == "C":
                self.conjunction_bank.append(return_word("C"))
        return

    def init_tweet(self):
        self.update_word_bank()
        self.tweet = ""
        noun_index = 0
        verb_index = 0
        article_index = 0
        adjective_index = 0
        adverb_index = 0
        preposition_index = 0
        conjunction_index = 0
        for c in self.dna:
            if c == "N":
                self.tweet += self.withdraw_word("N", noun_index)
                noun_index += 1
            elif c == "V":
                self.tweet += self.withdraw_word("V", verb_index)
                verb_index += 1
            elif c == "A":
                self.tweet += self.withdraw_word("A", article_index)
                article_index += 1
            elif c == "J":
                self.tweet += self.withdraw_word("J", adjective_index)
                adjective_index += 1
            elif c == "D":
                self.tweet += self.withdraw_word("D", adverb_index)
                adverb_index += 1
            elif c == "P":
                self.tweet += self.withdraw_word("P", preposition_index)
                preposition_index += 1
            elif c == "C":
                self.tweet += self.withdraw_word("C", conjunction_index)
                conjunction_index += 1
            self.tweet += " "
        return

    def withdraw_word(self, word_type, index):
        if word_type == "N":
            try:
                return self.noun_bank[index]
            except IndexError:
                word = return_word("N")
                self.noun_bank.append(word)
                return word
        elif word_type == "V":
            try:
                return self.verb_bank[index]
            except IndexError:
                word = return_word("V")
                self.verb_bank.append(word)
                return word
        elif word_type == "A":
            try:
                return self.article_bank[index]
            except IndexError:
                word = return_word("A")
                self.article_bank.append(word)
                return word
        elif word_type == "J":
            try:
                return self.adjective_bank[index]
            except IndexError:
                word = return_word("J")
                self.adjective_bank.append(word)
                return word
        elif word_type == "D":
            try:
                return self.adverb_bank[index]
            except IndexError:
                word = return_word("D")
                self.adverb_bank.append(word)
                return word
        elif word_type == "P":
            try:
                return self.preposition_bank[index]
            except IndexError:
                word = return_word("P")
                self.preposition_bank.append(word)
                return word
        elif word_type == "C":
            try:
                return self.conjunction_bank[index]
            except IndexError:
                word = return_word("C")
                self.conjunction_bank.append(word)
                return word

    def add_word(self, word, word_type, pos):
        if word_type == "N":
            try:
                self.noun_bank[pos] = word
            except IndexError:
                self.noun_bank.append(word)
        elif word_type == "V":
            try:
                self.verb_bank[pos] = word
            except IndexError:
                self.verb_bank.append(word)
        elif word_type == "A":
            try:
                self.article_bank[pos] = word
            except IndexError:
                self.article_bank.append(word)
        elif word_type == "J":
            try:
                self.adjective_bank[pos] = word
            except IndexError:
                self.adjective_bank.append(word)
        elif word_type == "D":
            try:
                self.adverb_bank[pos] = word
            except IndexError:
                self.adverb_bank.append(word)
        elif word_type == "P":
            try:
                self.preposition_bank[pos] = word
            except IndexError:
                self.preposition_bank.append(word)
        elif word_type == "C":
            try:
                self.conjunction_bank[pos] = word
            except IndexError:
                self.conjunction_bank.append(word)
        return

    def assign_dna(self, new_dna):
        self.dna = new_dna

    def update_word_bank(self):
        cut_bank_fat(self.noun_bank)
        cut_bank_fat(self.verb_bank)
        cut_bank_fat(self.article_bank)
        cut_bank_fat(self.adjective_bank)
        cut_bank_fat(self.adverb_bank)
        cut_bank_fat(self.preposition_bank)
        cut_bank_fat(self.conjunction_bank)
        noun_amount = 0
        verb_amount = 0
        article_amount = 0
        adjective_amount = 0
        adverb_amount = 0
        preposition_amount = 0
        conjunction_amount = 0
        for c in self.dna:
            if c == "N":
                noun_amount += 1
                if noun_amount > self.return_bank_length("N"):
                    self.noun_bank.append(return_word("N"))
            if c == "V":
                verb_amount += 1
                if noun_amount > self.return_bank_length("V"):
                    self.verb_bank.append(return_word("V"))
            if c == "A":
                article_amount += 1
                if noun_amount > self.return_bank_length("A"):
                    self.article_bank.append(return_word("A"))
            if c == "J":
                adjective_amount += 1
                if noun_amount > self.return_bank_length("J"):
                    self.adjective_bank.append(return_word("J"))
            if c == "D":
                adverb_amount += 1
                if verb_amount > self.return_bank_length("D"):
                    self.adverb_bank.append(return_word("D"))
            if c == "P":
                preposition_amount += 1
                if preposition_amount > self.return_bank_length("P"):
                    self.preposition_bank.append(return_word("P"))
            if c == "C":
                adjective_amount += 1
                if conjunction_amount > self.return_bank_length("C"):
                    self.conjunction_bank.append(return_word("C"))

    def return_dna(self):
        return self.dna

    def return_fitness(self):
        self.fit = return_fitness(self.dna)
        return self.fit

    def return_tweet(self):
        self.init_tweet()
        return self.tweet

    def return_bank_length(self, word_type):
        if word_type == "N":
            return len(self.noun_bank)
        elif word_type == "V":
            return len(self.verb_bank)
        elif word_type == "A":
            return len(self.article_bank)
        elif word_type == "J":
            return len(self.adjective_bank)
        elif word_type == "D":
            return len(self.adverb_bank)
        elif word_type == "P":
            return len(self.preposition_bank)
        elif word_type == "C":
            return len(self.conjunction_bank)

    def return_length(self):
        self.dna_size = len(self.dna)
        return self.dna_size


def generate_tweet():
    x = "Ever hear a robot fart?"
    return x


def return_fitness(word):
    # return a fitness based on basic English grammar rules
    grammar_fit = 0
    noun_check = 0
    verb_check = 0
    adjective_check = 0
    article_check = 0
    adverb_check = 0
    preposition_check = 0
    conjunction_check = 0

    for x in xrange(0, len(word)-1):
        if word[x] == word[x+1]:  # same type of word next to each other
            grammar_fit += 4
        if word[x] == "N":
            noun_check = 1
        if word[x] == "V":
            verb_check = 1
        if word[x] == "J":
            adjective_check = 1
        if word[x] == "A":
            article_check = 1
        if word[x] == "D":
            adverb_check = 1
        if word[x] == "P":
            preposition_check = 1
        if word[x] == "C":
            conjunction_check = 1
    if noun_check == 0:
        grammar_fit += 5
    if verb_check == 0:
        grammar_fit += 5
    if adjective_check == 0:
        grammar_fit += 5
    if article_check == 0:
        grammar_fit += 5
    if adverb_check == 0:
        grammar_fit += 5
    if preposition_check == 0:
        grammar_fit += 5
    if conjunction_check == 0:
        grammar_fit += 5
    if word[len(word)-1] == "A":
        grammar_fit += 1
    if word[0] == "V" or word[0] == "D":
        grammar_fit += 2
    return float(grammar_fit/len(word))


def selection(population):
    winner = random.randint(0, POP_SIZE-1)
    winner_fit = population[winner].return_fitness()
    for x in xrange(0, 3):
        opponent = random.randint(0, POP_SIZE-1)
        opponent_fit = population[opponent].return_fitness()
        if winner_fit > opponent_fit:
            winner = opponent
            winner_fit = opponent_fit
    return population[winner]


def random_char():
    # Return a random character between ASCII 97 and 122
    return chr(int(random.randrange(97, 122, 1)))


def random_symbol():
    # Returns a random word type (N = Noun, V = Verb, etc)
    return DNA_SYMBOLS[random.randrange(0, DNA_SYMBOLS_SIZE)]


def random_population():
    # Return a list of POP_SIZE individuals, each randomly generated
    pop = []
    for i in xrange(POP_SIZE):
        dna = ""
        rand_num = random.randint(2, MIN_DNA_SIZE)
        for c in xrange(rand_num):
            dna += random_symbol()
        pop.append(Individual(dna))
    return pop


def counter(seq):
    r = {}
    for x in seq:
        r[x] = r.setdefault(x, 0) + 1
    return r


def cut_bank_fat(word_list):
    if len(word_list) == len(counter(word_list).values()):
        return
    index = 0
    for x in counter(word_list).values():
        if x > 1:
            extra = x - 1
            for t in xrange(extra):
                word_list.remove(word_list[index])
        index += 1


# GA functions


def mutate(indiv):
    # For each gene in the DNA, there is a 1/mutation_chance chance that it will be
    # switched out with a random word type
    dna_out = ""
    dna = indiv.return_dna()
    for c in xrange(0, len(indiv.return_dna())):
        if int(random.randint(0, 100)) >= 80:
            dna_out += random_symbol()
        else:
            dna_out += dna[c]
    if int(random.randint(0, 100)) >= 95:
        rand_num = random.randint(0, 2)
        for _ in xrange(rand_num):
            if len(dna_out) >= MAX_DNA_SIZE:
                break
            dna_out += random_symbol()
    elif int(random.randint(0, 100)) >= 95:
        rand_num = random.randint(0, 2)
        for _ in xrange(rand_num):
            if len(dna_out) <= MIN_DNA_SIZE:
                break
            dna_out = dna_out[1:]
    indiv.assign_dna(dna_out)
    return


def crossover(indiv1, indiv2):
    if random.randint(0,100) > 75:
        temp_dna1 = indiv1.return_dna()
        temp_dna2 = indiv2.return_dna()
        pos = random.randint(2, len(temp_dna1))
        dna1 = temp_dna1[0:pos]+temp_dna2[pos:]
        indiv2_words = indiv2.return_tweet().split(" ")
        indiv2_words = indiv2_words[pos:]
        words_crossover(indiv1, dna1, indiv2_words, pos)
        indiv1.assign_dna(dna1)
    return


def words_crossover(indiv, dna, words, pos):
    current_nouns, current_verbs, current_articles, current_adjectives, current_adverbs, current_prepositions, current_cunjunctions = return_amount_types(dna[:pos])
    for c in dna[pos:]:
        if c == "N":
            indiv.add_word(words.pop(0), "N", current_nouns)
            current_nouns += 1
        if c == "V":
            indiv.add_word(words.pop(0), "V", current_verbs)
            current_verbs += 1
        if c == "A":
            indiv.add_word(words.pop(0), "A", current_articles)
            current_articles += 1
        if c == "J":
            indiv.add_word(words.pop(0), "J", current_adjectives)
            current_adjectives += 1
        if c == "D":
            indiv.add_word(words.pop(0), "D", current_adverbs)
            current_adverbs += 1
        if c == "P":
            indiv.add_word(words.pop(0), "P", current_prepositions)
            current_prepositions += 1
        if c == "C":
            indiv.add_word(words.pop(0), "C", current_cunjunctions)
            current_cunjunctions += 1


def return_amount_types(dna):
    noun_amount = 0
    verb_amount = 0
    article_amount = 0
    adjective_amount = 0
    adverb_amount = 0
    preposition_amount = 0
    conjunction_amount = 0
    for c in dna:
        if c == "N":
            noun_amount += 1
        if c == "V":
            verb_amount += 1
        if c == "A":
            article_amount += 1
        if c == "J":
            adjective_amount += 1
        if c == "D":
            adverb_amount += 1
        if c == "P":
            preposition_amount += 1
        if c == "C":
            conjunction_amount += 1
    return noun_amount, verb_amount, article_amount, adjective_amount, adverb_amount, preposition_amount, conjunction_amount


def return_sentence(dna):
    out_sentence = ""
    for char in dna:
        out_sentence += return_word(char)
        out_sentence += " "
    return out_sentence


def print_population(pop):
    for x in xrange(0, POP_SIZE):
        pop[x].init_tweet()
        print pop[x].return_dna()
        print pop[x].return_tweet()
    print "\n"
    return


def next_generation(previous_pop, best1, best2):
    new_population = []
    new_population.append(best1)
    new_population.append(best2)
    for c in xrange(2, POP_SIZE, 2):
        # Selection
        ind1 = previous_pop[c]
        ind2 = previous_pop[c+1]
        while ind1 == ind2:
            ind2 = selection(previous_pop)

        # Crossover
        temp = copy.copy(ind1)
        crossover(ind1, ind2)
        crossover(ind2, temp)

        # Mutate
        mutate(ind1)
        mutate(ind2)

        # Add to next population
        new_population.append(ind1)
        new_population.append(ind2)
    return new_population


def get_best(pop):
    best_fit = 1000
    for x in pop:
        if best_fit > x.return_fitness():
            best_fit = x.return_fitness()
            best = x
    # print "\n\n"
    # print best_fit
    # print best.return_dna()
    # print best.return_tweet()
    return best

def get_avg_fit(pop):
    avg = 0
    for x in pop:
        avg += x.return_fitness()
    avg = avg/POP_SIZE
    return avg


def get_5_tweets(pop):
    tweet1 = selection(pop).return_tweet()
    tweet2 = selection(pop).return_tweet()
    while tweet2 == tweet1:
        tweet2 = selection(pop).return_tweet()
    tweet3 = selection(pop).return_tweet()
    while tweet3 == tweet1 or tweet3 == tweet2:
        tweet3 = selection(pop).return_tweet()
    tweet4 = selection(pop).return_tweet()
    while tweet4 == tweet1 or tweet4 == tweet2 or tweet4 == tweet3:
        tweet4 = selection(pop).return_tweet()
    tweet5 = selection(pop).return_tweet()
    while tweet5 == tweet1 or tweet5 == tweet2 or tweet5 == tweet3 or tweet5 == tweet4:
        tweet5 = selection(pop).return_tweet()
    return tweet1, tweet2, tweet3, tweet4, tweet5