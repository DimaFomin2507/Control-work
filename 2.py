# """
# Напишите скрипт, который прочитает файл 2.txt
# И создаст новый файл 2_raint.txt
# И точно так же запишет тот же текст, заменив все слова дождь на ДОЖДЬ
# (большими буквами)
# Учитывая окончания, например  дожде -> ДОЖДЕ
# """
#
# with open("2.txt", 'r', encoding='utf-8') as  f:
#     text = [
#         line.split()
#         for line in f.readlines()
#     ]
# new_text = []
# for line in text:
#     new_line = []
#     for word in line:
#         if 'дожд' in word.lower():
#             new_line.append(word.upper())
#         else:
#             new_line.append(word)
#     new_text.append(' '.join(new_line))
# print('\n'.join(new_text))


# class FileHandler:
#     def __init__(self, path):
#         self.path = path
#
#     def read(self) -> str:
#         with open(self.path, 'r', encoding='utf-8') as f:
#             return f.read()
#
#     def write(self, text: str):
#         with open(self.path, 'w', encoding='utf-8') as f:
#             f.write(text)
#
# f1 = FileHandler('test1.txt')
# f1.write("Привет!")
# f2 = FileHandler('test2.txt')
# f2.write("Ещё пример текста!")
# print(f1.read())
# print(f2.read())

