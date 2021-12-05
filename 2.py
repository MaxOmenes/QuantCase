import codecs

def menu_point(dos): #dos - do something
    text = []
    if dos == 1: 
        file_path = str(input("Input file path: "))
        f = codecs.open(file_path, "r", encoding='utf-8')
        text = f.readlines()
    elif dos == 2:
        print('В конце введите 0')
        s = str(input()) 
        while s != '0':
            text.append(s)
            s = str(input()) 

    return text



#entry_point
txt = menu_point(int(input('Input 1 if file, or 2 if input: ')))
result = []
special_symbols = [".", ",", "?", "!",":",";"]
for j in range(len(txt)):
    paragraph = txt[j] 
    space = 0
    start_p = True
    n = len(paragraph)
    for i in range(n):
        #лишние пробелы
        if (paragraph[i] != ' ') and start_p:
            space = i
            start_p = False
        if paragraph[i] in special_symbols:
            k_l = 1
            k_r = 2
            flag_l, flag_r = False, False
            while paragraph[i-k_l] != ' ':
                k_l+=1
                flag_l = True
            while paragraph[i+k_r] != ' ':
                k_r+=1
                flag_r = True
            if flag_l:
                paragraph = paragraph[:k_l]+paragraph[i:]
                n -= k_l
            if flag_r:
                paragraph=paragraph[:i]+paragraph[k_r:]
                n -= k_r
            


    paragraph = '   ' + paragraph[space:]



    if paragraph[len(paragraph)-1] == '-':
        paragraph = paragraph[:(len(paragraph)-2)] + txt[j+1]
        j+=1

    result.append(paragraph)

for i in result:
    print(i)









