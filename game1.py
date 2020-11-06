from lib.cs import game

# Read in the file
while True:
    with open('dataset.txt', 'r') as file:
        filedata = file.readlines()
    listik = []
    for index, line in enumerate(filedata):
        if 'Stop' in line:
            listik.append(index)

    print(listik)
    if not listik:
        break

    for element in listik:
        with open('dataset.txt', 'r') as file:
            filedata = file.readlines()
            previous = filedata[element - 1]
            if 'Stop' in previous:
                previous = filedata[element - 2]
                if 'Stop' in previous:
                    previous = filedata[element - 3]
                    previous = previous[- 8:- 2]
                    changed = list(game(int(previous) + 3, int(previous) + 4))[0]
                else:
                    previous = previous[- 8:- 2]
                    changed = list(game(int(previous) + 2, int(previous) + 3))[0]
            else:
                previous = previous[- 8:- 2]
                changed = list(game(int(previous) + 1, int(previous) + 2))[0]

        file.close()
        filedata[element] = str(changed) + '\n'
        with open('dataset.txt', 'w') as file:
            file.writelines(filedata)
        file.close()


