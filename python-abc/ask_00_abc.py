#!/usr/bin/env python3
"""Module for Animal abstract class and its subclasses"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal"""
    @abstractmethod
    def sound(self):
        """Abstract method sound"""
        pass


class Dog(Animal):
    """Dog subclass"""
    def sound(self):
        """Returns Bark"""
        return "Bark"


class Cat(Animal):
    """Cat subclass"""
    def sound(self):
        """Returns Meow"""
        return "Meow"
