def read_studentdemo():
    fileReadDemo = open("E:/demoStudent.txt", "r")
    for line in fileReadDemo:
        print(line)
    fileReadDemo.close()


read_studentdemo()


def count_words():
    file = open("E:/demoStudent.txt", "r")
    count = 0
    data = file.read()
    words = data.split()

    for words in words:
        count += 1
    print("Number of words in a file: ", count)
    file.close()

count_words()