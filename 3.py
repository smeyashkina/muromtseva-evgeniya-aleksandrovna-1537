with open("languages.txt", 'r', encoding="utf-8") as file:
    a = file.readlines()
s = input()
while s != '0000':
    t = 0
    for i in range(1, len(a)):
        p = a[i].split('$')
        if int(p[2]) == int(s):
            t = 1
            title = p[0]
            creators = p[3]
            print('В', s, 'был создан',  title, 'его создатель:', creators)
    if t == 0: print('В этом году не было создано ЯП')
    s = input()
