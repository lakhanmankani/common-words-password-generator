import random

        
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
            
        with open('wordlist', 'r') as f:
            self.word_list = set(f.read().split('\n'))
            
    def generate_password(self):
        reduced_word_list = set()
        for word in self.word_list:
            if len(word) >= self.min_len:
                reduced_word_list.add(word)
        password_words = random.sample(reduced_word_list, self.words)
        if self.capitalize:
            password_words = [s.capitalize() for s in password_words]
        return self.splitter.join(password_words)
    
if __name__ == '__main__':
    generator = CommonWordsPasswordGenerator(words=6, capitalize=True)
    print(generator.generate_password())