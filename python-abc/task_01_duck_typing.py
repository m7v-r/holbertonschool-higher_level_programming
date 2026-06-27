#!/usr/bin/env python3
"""Module for Shape abstract class and concrete implementations"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class Shape"""
    @abstractmethod
    def area(self):
        """Abstract method for area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter"""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class inheriting from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Function to print area and perimeter of a shape object"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
