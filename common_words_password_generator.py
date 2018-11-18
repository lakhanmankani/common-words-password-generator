import random

def get_words(n):
    with open('wordlist', 'r') as f:
        list = f.read().split('\n')
        return list[n]
        
        
class CommonWordsPasswordGenerator:
    def __init__(self, words=None, min_len=None, splitter=None):
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
            
        with open('wordlist', 'r') as f:
            self.word_list = set(f.read().split('\n'))
            
    def generate_password(self):
        reduced_word_list = set()
        for word in self.word_list:
            if len(word) >= self.min_len:
                reduced_word_list.add(word)
        return random.sample(reduced_word_list, self.words)
    
if __name__ == "__main__":
    generator = CommonWordsPasswordGenerator()
    print(generator.generate_password())