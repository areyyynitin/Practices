demo = [1,2,3,4,5,6,7,8,9]
print("Demo List : ",demo)

lengthoflist = len(demo)                # length function
print("Length : ", lengthoflist)

demo.append(10)                         # append function
print(demo)

demo.extend([15,16])                    # extend function
print(demo)
demo.insert(5,55)                       #insert function
print(demo)
demo.remove(5)                          #remove function
print(demo) 
pop_member = demo.pop(4)                #pop function
print(demo)