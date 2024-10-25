
from aranorm import normalize_arabic_text



def normlizeComment(file1,file2):

    with open(file1, 'r') as file1:
        with open(file2, 'w',newline='') as file2:
            for row in file1:
       
       
                file2.write(normalize_arabic_text(row))
                file2.write('\n')




normlizeComment('data/data6000.txt','data/NormlizeComment')
