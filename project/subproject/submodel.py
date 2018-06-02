#fileName:submodel.py
import copy
class Dog:
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

dog1 = Dog('dog1',2,'red')
dog2 = Dog('dog2',2,'black')
dog3 = Dog('dog3',4,'green')
my_dogs = [dog1,dog2,dog3]
more_dogs = copy.deepcopy(my_dogs)
print (more_dogs[0].name)
print (more_dogs[0].color)
my_dogs[0].name = 'dog111'
print ('my_dogs[0].name:',my_dogs[0].name)
print ('more_dogs[0].name:',more_dogs[0].name)
