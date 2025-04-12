first = {1:345,567:0,98:0}
second = {32:1,0:0,1:1}
third = {67:41 , 56:78 , 12:21}
fourth = {}


for member in (first,second,third):
    fourth.update(member)
    print(fourth)