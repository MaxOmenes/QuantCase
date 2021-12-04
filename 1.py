import codecs

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

#write dict sort @MaxOmenes
OrderedDict(sorted(word_book.items(), key=lambda x: x[1], reverse=True))

print(word_book)
