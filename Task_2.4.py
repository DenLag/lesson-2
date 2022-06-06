my_words = input("Input the words with space").split()
i1 = 0
for i in my_words:
    if len(i) > 10:
        print(i1, i[:10])
    else:
        print(i1, i)
    i1 += 1
