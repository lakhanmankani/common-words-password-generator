import random
import functools


class CommonWordsPasswordGenerator:
    def __init__(self, words=None, min_len=None, splitter=None, capitalize=None):
        if words is None:
            self.words = 4
        else:
            self.words = words

        if min_len is None:
            self.min_len = 5
        else:
            self.min_len = min_len

        if splitter is None:
            self.splitter = '-'
        else:
            self.splitter = splitter

        if capitalize is None:
            self.capitalize = False
        else:
            self.capitalize = capitalize

        word_list = {}
        with open('wordlist', 'r') as f:
            raw_word_list = f.read().split('\n')
        # `words` is a mapping from length to a set of words
        # with that length
        for word in raw_word_list:
            word_list.setdefault(len(word), set()).add(word)
        self.word_list = {k: frozenset(v) for k, v in word_list.items()}

    def generate_password(self):
        # Take the union of words with length >= min_len
        reduced_word_list = functools.reduce(frozenset.union, (v for k, v in self.word_list.items() if k >= self.min_len))
        password_words = random.sample(reduced_word_list, self.words)
        if self.capitalize:
            password_words = [s.capitalize() for s in password_words]
        return self.splitter.join(password_words)

if __name__ == '__main__':
    generator = CommonWordsPasswordGenerator(words=6, capitalize=True)
    print(generator.generate_password())
