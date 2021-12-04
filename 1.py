import codecs

#entry_point
file_path = str(input("Input file path: "))
f = codecs.open(file_path, "r", encoding='utf-8')
text = f.read()
#count_alghorithm
word_book = {}
word = ""
for letter in text:
    if letter in [".", ",", "-", "?", "!", "\r", "\n"]:
        letter = ""
    if letter != " ": #change all ".", ",", "-", "?", "!" to "" @MaxOmenes
        word+=letter
    else:
        if not (word in word_book):
            word_book[word] = 0 #add new word in list
        word_book[word]+=1
        word = ""

#write dict sort @MaxOmenes

print(word_book)