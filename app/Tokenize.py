from keras.preprocessing.text import tokenizer_from_json
from keras.preprocessing.sequence import pad_sequences
import string 
import contractions
import json

class Comment(object):
    punc = string.punctuation

    tokenizer = tokenizer_from_json(json.load(open('tokenizer.json')))
    
    word_index = tokenizer.word_index
    MAX_LENGTH = 42
     
    def __init__(self, text):
        self.text = text

    def tokenize(self):
        text_contract_fixed = contractions.fix(self.text)
        punc_removed = ' '.join(s for s in text_contract_fixed.split() if s not in self.punc)
        text_token = self.tokenizer.texts_to_sequences([punc_removed])
        text_token_pad = pad_sequences(text_token, maxlen=self.MAX_LENGTH, truncating='post', padding='post')
 
        return text_token_pad
