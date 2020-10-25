from lib.cs import game

with open('dataset.txt', 'a') as file:
    for i in (game(720406, 800000)):
        file.write(str(i) + '\n')

# with open('dataset.txt', 'r') as file:
#     for i in file:
#         print('-' + i + '-')
#         print(1)