'''
Created on Apr 20, 2015
Last modified on Jan 23, 2016

@author: Brian Borowski

CS115 - Undergraduate student class derived from Student class.
'''
from student import Student

class UndergradStudent(Student):
    def __init__(self, first_name, last_name, sid, gpa, meal_plan_balance):
        super().__init__(first_name, last_name, sid, gpa)
        self.__meal_plan_balance = meal_plan_balance

    def __str__(self):
        return super().__str__() + ', meal plan balance: $' \
            + str(self.__meal_plan_balance)

if __name__ == '__main__':
    u1 = UndergradStudent('John', 'Doe', '123456', '4.0', 1000)
    print(u1)
    u1.gpa = 3
    print(u1.gpa)
