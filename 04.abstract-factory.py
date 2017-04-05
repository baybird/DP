# Filename      : 03.factory.py
# Author        : Robert Tang
# Created       : 4/5/2017
# Last Modified :
# Description   : Abstract Factory Pattern of Creational Patterns
# Python Version: 2.7

from abc import ABCMeta, abstractmethod

# Abstract car
class Car:
  # instance of ABCMeta
  __metaclass__ = ABCMeta

  @abstractmethod
  def getType(self):
    pass

# Concrete cars
class Truck(Car):
  def getType(self):
    return 'Truck'


class Van(Car):
  def getType(self):
    return 'Van'


# Abstract shoe
class Shoe:
  # instance of ABCMeta
  __metaclass__ = ABCMeta

  @abstractmethod
  def getType(self):
    pass

# Concrete cars
class Boot(Shoe):
  def getType(self):
    return 'Boot'


class Sandal(Shoe):
  def getType(self):
    return 'Sandal'



# Abstract Factory
class Factory:
  # instance of ABCMeta
  __metaclass__ = ABCMeta

  @abstractmethod
  def createCar(self):
    pass

  @abstractmethod
  def createShoe(self):
    pass

# Concrete Factories
class FactoryA:
  @staticmethod
  def createCar():
    return Truck()

  @staticmethod
  def createShoe():
    return Boot()

class FactoryB:
  @staticmethod
  def createCar():
    return Van()

  @staticmethod
  def createShoe():
    return Boot()

# Test
car   = FactoryA.createCar()
shoe  = FactoryA.createShoe()
print car.getType()
print shoe.getType()

car   = FactoryB.createCar()
shoe  = FactoryB.createShoe()
print car.getType()
print shoe.getType()
