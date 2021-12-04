import codecs
from collections import OrderedDict

#entry_point
file_path = str(input("Input file path: "))
f = codecs.open(file_path, "r", encoding='utf-8')
text = f.read()
#count_alghorithm
word_book = {}
word = ""
special_symbols = [".", ",","-","—", "?", "!", "\r", "\n", "(", ")", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":"]
for letter in text:
    if letter in special_symbols:
        letter = ""
    if letter != " ": #change all ".", ",", "-", "?", "!" to "" @MaxOmenes
        word+=letter
    else:
        if not (word in word_book):
            word_book[word] = 0 #add new word in list
        word_book[word]+=1
        word = ""

#write dict sort @MaxOmenes/
#write dict sort @MaxOmenes///
word_book = {key: value for key, value in sorted(word_book.items(), key= lambda value: value[1], reverse=True)}

k = 60
for element in word_book:
    print(element)
    k-=1
    if k < 0:
        break

