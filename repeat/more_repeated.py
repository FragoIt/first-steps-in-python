
from collections import Counter
from string import ascii_letters

with open('../cuento.txt', 'r+',encoding='utf-8') as c:
    history=c.read()

def tell_tales():
    new=history
    abc=ascii_letters
    new_string = ''.join(ch for ch in new if ch.isalnum() or ch.isspace())
    new_string_2=new_string.lower().replace('\n','').split(' ')
    return new_string_2



new_string=tell_tales()
counter= Counter(new_string)
my_list_I=list()
for k,v in counter.most_common(21):
    my_list_I.append([k,v])

print(my_list_I)  

 