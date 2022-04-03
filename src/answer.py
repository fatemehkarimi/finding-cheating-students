from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


class Answer:
    def __init__(self, plain_text):
        self.ps = PorterStemmer()
        self.plain_text = plain_text
        self.tokens = word_tokenize(self.plain_text)
        self.remove_special_char()
        self.word_freq = {}
        self.setup_word_freq()

    def remove_special_char(self):
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
                         '-', '_', '+', '=', ',', '.', ':', ';', '"', '?', '~']
        self.tokens = [t for t in self.tokens if t not in special_chars]

    def setup_word_freq(self):
        for word in self.tokens:
            stem = self.ps.stem(word)
            if stem in self.word_freq.keys():
                self.word_freq[stem]['count'] += 1
                self.word_freq[stem]['original'].append(word)
            else:
                self.word_freq[stem] = {
                    'original': [word],
                    'count': 1
                }

    def get_word_freq(self):
        return self.word_freq
