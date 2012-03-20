'''
Practice creating classes and subclasses.
Will Townes
'''

class Animal():
    def __init__(self):
        self.alive = True
    def setdata(self):
        self.health = 100

class Bird(Animal):
    def __init__(self):
        self.alive = False

        
