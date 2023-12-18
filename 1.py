# """
# Сделайте функцию, которая создаст новый список из этого, заменив None на 0
# """
#
# test_lst = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [None, 8, 9],
#     [10, 11, 12],
#     [13, None, 15],
#     [16, 17, 18],
#     [19, 20, 21],
#     [22, 23, None],
# ]
#
# # end_lst = []
# # for item in test_lst:
# #     middle_lst = []
# #     for item2 in item:
# #         middle_lst.append(
# #             item2 if item2 is not None else 0
# #         )
# #     end_lst.append(middle_lst)
# end_lst = [
#     [
#         item2 if item2 is not None else 0
#         for item2 in item
#     ]
#     for item in test_lst
# ]
# print(end_lst)


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def meow(self):
#         print(f"{self.name}: Мяу!")
# cat = Cat("Барсик")
# cat2 = Cat("Антошка")
# cat.meow()
# cat2.meow()

# class Student:
#     def __init__(self, full_name, age, course):
#         self.full_name = full_name
#         self.age = age
#         self.course = course
#     def info(self):
#         return (f"{self.full_name}: {self.age} лет, {self.course} курс")
# dima = Student('Дмитрий', 22 , 2)
# print(dima.info())

class Field:

    def __init__(self):
        self.field = [' '] * 9
    def _check(self, index):
        return self.field[index] == ' '
    def turn(self, index, symbol):
        if self._check(index):
            self.field[index] = symbol
    def print(self):
        print(self.field[:3])
        print(self.field[3:6])
        print(self.field[6:])
        print()
field = Field()
field.print()
field.turn(3, 'X')
field.print()
field.turn(3,'O')
field.print()
