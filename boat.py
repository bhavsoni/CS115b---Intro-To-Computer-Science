'''
CS 115, Spring 2017 - Test 3, Questions 7 and 8

Author: Bhavin Soni
Pledge: I pledge my honor that I have abided by the Stevens Honor System
'''

from math import sqrt

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' RULES: You can use Canvas to download this file and upload your solution.
' You can use Eclipse to edit and run your program. You should NOT look at
' other programs in Eclipse, you should NOT use any other programs, and you
' should NOT use any notes or books.
' According to the Honor Code, you should report any student who appears
' to be violating these rules.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 7 (15 points)
' Implement missing sections of the MotorBoat class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class MotorBoat(object):
    '''Write the constructor below. It should take in four arguments:
       - overall_length (a float representing the total length in meters)
       - waterline_length (a float representing the length in meters where
                           the boat meets the water)
       - weight (an int representing the weight of the boat in pounds)
       - horsepower (an int representing the horsepower of the motor)
       All fields must be private. No error checking or type conversions
       are required.
       5 points'''
    def __init__(self, overall_length, waterline_length, weight, horsepower):
        self.__overall_length = overall_length
        self.__waterline_length = waterline_length
        self.__weight = weight
        self.__horsepower = horsepower

    '''Write a property for horsepower. 3 points'''
    @property
    def horsepower(self):
        return self.__horsepower

    '''Write a setter for horsepower. 3 points'''
    @horsepower.setter
    def horsepower(self, horsepower):
        self.__horsepower = horsepower

    '''Write a method called get_max_speed.
       It returns the maximum speed of the boat based on the horsepower of
       the motor and the total weight of the boat.
       The formula is: 225 x sqrt(horsepower / weight)
       4 points'''
    def get_max_speed(self):
        return 225 * sqrt(self.__horsepower / self.__weight)

    def __str__(self):
        return '%s:\n  Overall length: %.1f meters\n' \
               '  Waterline length: %.1f meters\n' \
               '  Weight: %d pounds\n  Horsepower: %d\n' \
               '  Max speed: %.1f mph' % \
            (self.__class__.__name__, self.__overall_length, \
             self.__waterline_length, self.__weight, \
             self.__horsepower, self.get_max_speed())

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Question 8 (15 points)
' Implement missing sections of the MotorSailor class. MotorSailor should be
' a subclass of MotorBoat.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class MotorSailor(MotorBoat):  # 2 points
    '''Write the constructor below. It should take in five arguments:
    - the first four are the same as in the MotorBoat constructor.
    - sail_dimension, a float >= 0. This attribute represents the length
      and width in meters of the square sail attached to the boat.

      MAKE SURE sail_dimension is a float >= 0. Otherwise, if it's not a float
      raise a TypeError stating, "Sail dimension must be a float."  You must
      use the type() function to get credit for this part.
      If it's a float but < 0, raise a ValueError stating,
      "Sail dimension cannot be negative."
      
      sail_dimension must be private.

    8 points'''
    def __init__(self, overall_length, waterline_length, weight, horsepower, sail_dimension):
        super().__init__(overall_length, waterline_length, weight, horsepower)
        self.__sail_dimension = sail_dimension
#         try:
#             type(self.__sail_dimension) = float
#         except:
#             raise TypeError("Sail dimension must be a float.")
        if type(self.__sail_dimension) == float:
            raise TypeError('must be float')
        if self.__sail_dimension < 0:
            raise ValueError("Sail dimension cannot be negative.")

    '''Override the method get_max_speed.
    It returns the maximum speed the boat can travel.
    The maximum speed is the sum of speed obtained from the motor plus
    the boost picked up from the sail.
    The formula for sail boost is the sail's area in meters / 3.5.
    To get full credit, you must call get_max_speed in the superclass.
    5 points'''
    def get_max_speed(self):
        return super().get_max_speed() + ((self.__sail_dimension **2)/ 3.5)

if __name__ == '__main__':
    mb = MotorBoat(46, 42, 1000, 300)
    print(mb)
    mb.horsepower = 320
    print(mb.horsepower)
    print(mb)
    ms = MotorSailor(46, 42, 1000, 320, 4.5)
    print(ms)