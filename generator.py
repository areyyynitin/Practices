# def count(num):
#     counter = 1
#     while counter <= num:
#         yield counter
#         counter+=1

# gen=count(10)

# for n in gen:
#     print(n)


# geenerator demo 2
# gen = (x**2 for x in range(5))

# for num in gen:
#     print(num)

# genrator demo 3
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=(num for num in numbers if num%2==0)
# for e in even:
#     print(e)

# odd=(num1 for num1 in numbers if num1%2!=0)
# for o in odd:
#     print(o)

# generators demo 4
# words=["FIRST" , "topic" , "in" ,"python" , "generators"]
# ucase = (w.upper() for w in words)

# for w in ucase:
#     print(w)

#gen demo 5
def infinite(start=0):
    while True:
        yield start
        start +=1

counter = infinite()
for i in range(5):
    print(next(counter))