# squares = [x**2 for x in range(10)]
# print(squares)

# squares2 = [ x**2 for x in range(1,6)]
# print(squares2)

# evenSquares = [x**2 for x in range(1,11) if x%2 == 0]
# print(evenSquares)

# oddSquares = [x**2 for x in range(1,11) if x%2 != 0]
# print(oddSquares)


# nested
pairs = [(x,x**2) for x in range (1,4)]
print(pairs)

matrix=[[1,2,3] , [4,5,6] , [7,8,9]]
flatten = [elements for row in matrix for elements in row]
print(flatten)