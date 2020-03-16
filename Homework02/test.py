"""
Exercise 2.1
Name: Won Seok Park
Date: Mar/11/2020

Spam Filter
"""

from collections import Counter

# Spam corpus contains spam e-mails.
spam_corpus = [["I", "am", "spam", "spam", "I", "am"], ["I", "do", "not", "like", "that", "spamiam"]]
# Ham corpus contains non-spam e-mails.
ham_corpus = [["do", "i", "like", "green", "eggs", "and", "ham"], ["i", "do"]]
# Test corpus
test_corpus = [["I" "like" "Green", "eggs", "and", "spam"], ["Ham", "is", "the", "best", "food"],
               ["I", "am", "who", "I", "am", "not", "green", "spam"]]

# Number of spam and non-spam e-mails.
b_num = len(spam_corpus)
g_num = len(ham_corpus)

# Threshold value for the spam filter algorithm (Given by VanderLinden).
threshhold = 1
# Threshold value to determine if the message is actually spam.
spam_threshhold = 0.9
# Threshold value for the number of interesting tokens to use in testing for spam.
interesting_tokens_num = 15

class SpamFilter:
    """ Initialize class variables. """

    def __init__(message):
        self.message = message

def spam_filter(corpus):
    pass

def token_creater(corpus):
    tokens = [token.lower() for message in corpus for token in message]

    print(tokens)
    return tokens

def token_counter(message, tokens):
    token_count_map = {}
    for token in tokens:
        token_count_map[token] = message.count(token)

    print(token_count_map)
    return token_count_map

def spam_probability_map(gtoken_occurences_map, btoken_occurences_map, good_num, bad_num, tokens):
    probability_map = {}
    for token in tokens:
        good = float(2 * gtoken_occurences_map[token])
        bad = float(btoken_occurences_map[token])
        if (good + bad) > 0.9:
            probability_map[token] = max(0.01, min(0.99, min(1.0, good / good_num) + min(1.0, bad / bad_num))
        elif (good + bad) <= 0.9:
            probability_map[token] = 0

    return probability_map

def spam_filter(corpus, prob_map):
    product = 1.0
    complement_product = 1.0

    for token in corpus:
        if token in prob_map:
            probability = prob_map[token]
        else:
            probability = 0.4

        product *= probability
        complement_product = (1.0 - probability)

    return product / (product * complement_product)

if __name__ == '__main__':
    """
    Pithy Introduction.
    Executes the program.
    """
    print("\nExecuting spam filter algorithm!")
    print("I like Spam! - Delicious!")
    print("\n\n")

    # Get occurrences of each word in the list of words - returned as list of dictionaries.
    spam_wordlist = token_creater(spam_corpus)
    norm_wordlist = token_creater(ham_corpus)

    print(spam_worddict)
    print(nonspam_worddict)
    print(lower_case_words)

    tokens = list(set(norm_worddict_l) | set(spam_worddict_l))

    norm_map = token_counter(norm_wordlist, tokens)
    spam_map = token_counter(spam_wordlist, tokens)

    prob_map = spam_probability_map(norm_map, spam_map, g_num, b_num, tokens)

    # print(spam_filter(test_corpus[0], prob_map))

    # Determine probability that each word in the message is spam based on spam and non-spam corpus
    # - returned as dictionary.
    # TODO - this returns all the calculated probabilities for each word in the spam and ham corpus!
    # word_spam_chance = individual_word_spam_chance(lower_case_words_only[0],
    #                                                lower_case_words_only[1], algorithm_threshold_value)
    # print("ALL WORDS SPAM PROBABILITIES (should make sense): " + str(word_spam_chance))

    # ############################################
    # """
    # This section is purely to use a test corpus to test for spam'liness against our established dataset.
    # """

    # # Obtain the 15 most interesting tokens in the message based on their normalized spam probabilities.
    # interesting_words_only = find_interesting_tokens(test_corpus[0], word_spam_chance)
    # interesting_words_only = find_interesting_tokens(spam_corpus[0], word_spam_chance)
    # interesting_words_only = find_interesting_tokens(spam_corpus[1], word_spam_chance)
    # interesting_words_only = find_interesting_tokens(ham_corpus[0], word_spam_chance)
    # interesting_words_only = find_interesting_tokens(ham_corpus[1], word_spam_chance)

    # # Obtain the spam message final probability value.
    # result = message_spam_chance(interesting_words_only)

    # # Compare spam message final probability value against threshold spam probability value.
    # print("\nThreshold value above which e-mail message is considered spam: " + str(spam_message_threshold_value))
    # if result >= spam_message_threshold_value:
    #     print("Spam!!!!")
    # else:
    #     print("Not spam.")

