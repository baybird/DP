# Filename      : 01.singleton.py
# Author        : Robert Tang
# Created       : 3/29/2017
# Last Modified :
# Description   : Singleton Pattern of Creational Patterns
# Python Version: 2.7

class Singleton:
  instance = None

  @staticmethod
  def getInstance():
    if Singleton.instance == None:
      Singleton.instance = Singleton()

    return Singleton.instance


# Test
obj = Singleton.getInstance()
print obj;

obj2 = Singleton.getInstance()
print obj2;

# Result:
# <__main__.Singleton instance at 0x02E01710>
# <__main__.Singleton instance at 0x02E01710>