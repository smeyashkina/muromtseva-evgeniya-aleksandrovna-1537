
def insertion_sort(alist: list):
    """Описание фукнции insertion_sort.
        Сортировка вставками, на выход выдает отсортированный список данных.
        Описание аргументов:
        alist - список, требующий сортировки
        """
        
    for i in range(1, len(alist)):
        j = i
        while (j > 0 and alist[j] < alist[j - 1]):
            alist[j], alist[j - 1] = alist[j - 1], alist[j]
            j -= 1
    return alist


def second():
    alist = []
    with open("languages.txt", 'r', encoding="utf-8") as file:
        header = "title;creators;book_count"
        line = file.readline()
        for line in file:
            line = line.split("$")
            alist.append(line)
    alist = insertion_sort(alist=alist)
    for i in range(5):
        print(f"{alist[i][0]} - год создания {alist[i][2]} - {alist[i][-1]}")

second()
