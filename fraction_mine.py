'''
Created on Apr 17, 2017

@author: BhavinSoni
'''

class Fraction(object):
    '''Defines an immutable rational number with common arithmetic operations.
    '''

    def __init__(self, numerator=0, denominator=1):
        '''Constructs a rational number (fraction) initialized to zero or a user
        specified value.

        Args:
            numerator: the numerator of the fraction. (Default is 0).
            denominator: the denominator of the fraction (Default is 1).

        Raises:
            ZeroDivisionError: if the user tries to construct a fraction with
            the denominator 0.
        '''

        # The denominator cannot be zero.
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # If the rational number is zero, set the denominator to 1.
        if numerator == 0:
            self.__numerator = 0
            self.__denominator = 1 #simplest denominator and will always give back fraction in simplest terms

        # Otherwise, store the rational number in reduced form.
        else:
            # Determine the sign.
            if numerator * denominator < 0:
                sign = -1
            else:
                sign = 1

            # Reduce to smallest form.
            a = abs(numerator)
            b = abs(denominator)
            while a % b != 0:
                temp_a = a
                a = b
                b = temp_a % b #

            self.__numerator = abs(numerator) // b * sign
            self.__denominator = abs(denominator) // b

    def __eq__(self, other):
        '''Determines if this fraction is equal to another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if the fractions are equal, False otherwise
        '''
        return self.__numerator == other.__numerator and \
            self.__denominator == other.__denominator

    def reciprocal(self):
        return Fraction(self.__denominator, self.__numerator)
    
    
    def __add__(self, other):
        '''Adds a fraction to this fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the addition
        '''
        num = self.__numerator * other.__denominator + self.__denominator * other.__numerator
        den = self.__denominator * other.__denominator
        
        return Fraction(num,den)

    def __sub__(self, other):
        '''Subtracts a fraction from this fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the subtraction
        '''
        num = self.__numerator * other.__denominator - self.__denominator * other.__numerator
        den = self.__denominator * other.__denominator
        
        return Fraction(num,den)
    
    
    def __mul__(self, other):
        '''Multiplies this fraction by another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the multiplication
        '''
        num = self.__numerator * other.__numerator
        den = self.__denominator * other.__denominator
        
        return Fraction(num, den)

    def __truediv__(self, other):
        '''Divides this fraction by another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            a new Fraction object resulting from the division
        '''
        num = self.__numerator * other.__denominator
        den = self.__denominator * other.__numerator
        
        return Fraction(num, den)

    def __lt__(self, other):
        '''Determines if this fraction is less than another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is less than the other, False otherwise
        '''
        return self.__numerator * other.__denominator < self.__denominator * self.__numerator

    def __ne__(self, other):
        '''Determines if this fraction is not equal to another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if the fractions are not equal, False otherwise
        '''
        return not self == other #cannot do != bc it will recursive call the function

    def __le__(self, other):
        '''Determines if this fraction is less than or equal to another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is less than or equal to the other, False
            otherwise
        '''
        return not other < self #self greater than other then negate it 

    def __gt__(self, other):
        '''Determines if this fraction is greater than another fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is greater than the other, False otherwise
        '''
        return other < self

    def __ge__(self, other):
        '''Determines if this fraction is greater than or equal to another
        fraction.

        Args:
            other: the right-hand side fraction

        Returns:
            True if this fraction is greater than or equal to the other, False
            otherwise
        '''
        return not self < other
    
    def __int__(self):
        '''Converts a fraction to an integer.

        Returns:
            the interger value of this fraction
        '''
        return self.__numerator // self.__denominator

    def __float__(self):
        '''Converts a fraction to a floating-point number.

        Returns:
            the floating-point value of this fraction
        '''
        return self.__numerator / self.__denominator

    def __repr__(self):
        '''Gets an official string representation of the fraction.
  
        Returns:
            a string in the format Fraction(numerator, denominator)
        '''
        return self.__class__.__name__ + '(' + str(self.__numerator) + ',' + str(self.__denominator) + ')'

    def __str__(self):
        '''Gets a user-friendly string representation of the fraction.

        Returns:
            a string in the format numerator/denominator
        '''
        return str(self.__numerator) + '/' + str(self.__denominator)

if __name__ == '__main__':
    f = Fraction(2,4)
    g = Fraction(18,6)
    
    print(f)
    print(f == g)
    print(f.__eq__(g))
    h = f.reciprocal()
    print (h)
    print(f >= g)
    print(float(g))
    print(int(g))
    print(repr(g))
    
