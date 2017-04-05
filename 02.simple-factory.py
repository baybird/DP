# Filename      : 02.simple-factory.py
# Author        : Robert Tang
# Created       : 4/5/2017
# Last Modified :
# Description   : Simple Factory Pattern of Creational Patterns
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

# Factory
class Factory:
  @staticmethod
  def createProduct(product):
    if product == 'Truck':
      return Truck()
    elif product == 'Van':
      return Van()
    else:
      return None


# Test
truck = Factory.createProduct('Truck')
print truck.getType()

van = Factory.createProduct('Van')
print van.getType()
