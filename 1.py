import codecs

#modules
def menu_point(mode):
    '''
        menu_point select text reading mode
        returns the final text in variable
        @MaxOmenes
    '''
    if mode == 'f':
        file_path = str(input("Input file path: "))
        f = codecs.open(file_path, "r", encoding='utf-8')
        text = f.read()
    elif mode == 'i':
        text = str(input())
    else:
        exit()

    return text


#entry_point
reading_mode = str(input("Input reading mode(f - file, i - input): "))
text = menu_point(reading_mode)
#count_alghorithm
word_book = {}
word = ""
for letter in text:
    if letter in [".", ",", "-", "?", "!"]:
        letter = ""
    if letter != " ": #change all ".", ",", "-", "?", "!" to "" @MaxOmenes
        word+=letter
    else:
        if not (word in word_book):
            word_book[word] = 0 #add new word in list
        word_book[word]+=1
        word = ""

print(word_book)
