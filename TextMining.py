import nltk

#Tokenizing - Grouping (word tokenizers - seperates by words and sentence tokenizers
#Corpora - Body of Text - ex. Medical Journals, presidential soeeches, English Language
#Lexicon - Words and Meaning

# investor- speak & regular english speak
#bull - investor = someone who is positive about the market..

from nltk.tokenize import sent_tokenize, word_tokenize

example_text = " Hi, I am an American! I am from New York and I love Python Programming. The day is beautiful today but it's really hot"

##print(sent_tokenize(example_text))
##print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print (i)
