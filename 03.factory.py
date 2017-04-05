# Filename      : 03.factory.py
# Author        : Robert Tang
# Created       : 4/5/2017
# Last Modified :
# Description   : Factory Pattern of Creational Patterns
# Python Version: 2.7

from abc import ABCMeta, abstractmethod

# Abstract product
class Car:
  # instance of ABCMeta
  __metaclass__ = ABCMeta

  @abstractmethod
  def getType(self):
    pass

# Concrete products
class Truck(Car):
  def getType(self):
    return 'Truck'


class Van(Car):
  def getType(self):
    return 'Van'

# Abstract Factory
class carFactory:
  # instance of ABCMeta
  __metaclass__ = ABCMeta

  @abstractmethod
  def createProduct(self):
    pass

# Concrete Factories
class truckFactory:
  @staticmethod
  def createProduct():
    return Truck()

class vanFactory:
  @staticmethod
  def createProduct():
    return Van()

# Test
truck = truckFactory.createProduct()
print truck.getType()

van = vanFactory.createProduct()
print van.getType()