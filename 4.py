with open("languages.txt", 'r', encoding="utf-8") as file:
    a = file.readlines()
count = {}
for i in range(1, len(a)):
    p = a[i].split('$')
    k = p[1]
    if k in count:
        count[k] += 1
    else:
        count[k] = 1
for line in count:
    print(str(count[line]) + ' книг содержится в библиотеке по типу ' + line)






























