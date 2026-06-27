#!/usr/bin/env python3
"""Module for Dragon class using Mixins"""


class SwimMixin:
    """Mixin for swimming behavior"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying behavior"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from SwimMixin and FlyMixin"""
    def roar(self):
        print("The dragon roars!")
