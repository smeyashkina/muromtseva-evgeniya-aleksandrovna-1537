
def first():
    """Описание функции first.

        Функция анализирует данный файл и создает новый согласно заданному условию.

        """
    alist = []
    langs = set()
    with open("languages.txt", 'r', encoding="utf-8") as file:
        header = "title;creators;book_count"
        line = file.readline()
        for line in file:
            line = line.split("$")
            alist.append([line[0], line[3], line[4]])
            langs.add(line[0])

    with open("program.csv", 'w', encoding="utf-8") as out_file:
        out_file.write(header+"\n")
        for line in alist:
            line = ";".join(line)
            out_file.write(line)
    print(f"Количество языков запросов равно: {len(langs)}")
first()
