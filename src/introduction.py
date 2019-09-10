#!/bin/python3
from __future__ import print_function
import os
import random
import re
import sys
import typing
from io import StringIO


class Introduction(object):

    def __init__(self, out=sys.stdout):
        self.out = out

    def hello_world(self):
        return "hello world"

    def conditions(self, number: int):
        if number % 2 != 0:
            self.out.write("Weird")
        elif number >= 2 and number <= 5:
            self.out.write("Not Weird")
        elif number >= 6 and number <= 20:
            self.out.write("Weird")
        elif number > 20:
            self.out.write("Not Weird")

    def arithmetic_operators(self, first_integer: int, second_integer: int):
        self.out.write(str(first_integer+second_integer)+' ')
        self.out.write(str(first_integer-second_integer)+' ')
        self.out.write(str(first_integer*second_integer)+' ')

    def division_operation(self, first_integer: int, second_integer: int):
        self.out.write(str(first_integer/second_integer)+' ')
        self.out.write(str(float(first_integer)/float(second_integer))+' ')

    def loops(self, number: int):
        for i in range(number):
            self.out.write(str(i**2))

    def is_leap(self, year):
        '''
        A function to check if the year is leap or not
        '''
        leap = False

        if (year >= 1900 and year <= 10**5):
            if (year % 4 == 0 and year % 100 != 0):
                leap = True
            if (year % 100 == 0 and year % 400 == 0):
                leap = True

        self.out.write(str(leap))
        return leap

    def print_future(self, number):
        '''
        A print function using ___future___ function
        '''
        for i in range(1, number+1):
            print(i, sep=' ', end='')
            self.out.write(str(i))


if __name__ == '__main__':
    pass
