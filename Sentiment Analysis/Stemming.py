from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["Tradition", "Traditional", "Traditionally","Traditioned", "Traditioning"]

##for w in example_words:
##    print(ps.stem(w))

sample_text = " It is the traditionally the tradition to practice traditional rituals in a Traditioning Society"

words = word_tokenize(sample_text)

for w in words:
    print(ps.stem(w))
    
