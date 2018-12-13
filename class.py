'''
Created on Apr 11, 2017

@author: BhavinSoni
'''
import sys
'''a class is a blueprint for  something you wish to represent. 
classes contain attributes and methods. 
attributes are variables that represent the state of the object'''

'''methods are functions inside the class that allows you to change the state of an object. 
__ini__ is the constructor of special method of specializing the attributes of the object'''

'''private member variables begin with self.__(variable name)
private member variables cannot be referenced outside the class '''

'''instantiation means to create instance of an object'''

'''you cannot have a  setter without first having the corresponding property.
another name for a setter = mutator'''

'''inheritance represents an 'is-a' relationship that is objects of the sub class are instances of the superclass
and attributes of the superclass are inherited in the subclass'''

'''   animal
        /\
       /  \
    Dog     Cat
    
'has-a' relationship describes composition. instances of the object have those attributes'''

class Student(object):
    def __init__(self, first_name, last_name, sid, gpa):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sid = sid
        try:
            self.__gpa = float(gpa)
        except:
            raise TypeError('gpa must be a float')
                
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name
    
    @property
    def sid(self):
        return self.__sid
    
    @sid.setter
    def sid(self, sid):
        self.__sid = sid
    
    @property
    def gpa(self):
        '''this is an accessor or getter method. if you have a reference s1, to a student object, simply read the value of 
        the gpa by referencing s1.gpa'''
        return self.__gpa
    
    @gpa.setter
    def gpa(self, gpa):
        try:
            local_gpa = float(gpa)
        except:
            raise TypeError('gpa must be a float')
        if local_gpa < 0.0 or local_gpa > 4.0:
            raise ValueError('gpa must be between 0.0 and 4.0')
        self.__gpa = local_gpa
    
    
    def __str__(self):
        return self.__first_name + ' ' + self.__last_name + ' (SID: ' + \
            self.__sid + ', GPA: ' + str(self.__gpa) + ')'
    
if __name__ == '__main__':
    try:
        s1 = Student('john', 'doe', '123456' , '5.0')
    except TypeError as error:
        print('error:',error )
        sys.exit(1)
    print (s1.first_name)
    s1.first_name = 'brian'
    print(s1.first_name)
    print(s1.last_name)
    s1.last_name = 'soni'
    print(s1.last_name)
    s1.gpa = 100.3
    print(s1.gpa)
    