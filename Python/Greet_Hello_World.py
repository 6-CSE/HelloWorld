import sys

class Greet:
    def __init__(self, greeting):
        self.greeting = greeting

    def __str__(self):
        return self.greeting

class HelloWorld:
    def __init__(self):
        self.h = Greet('Hello, ')
        self.w = Greet('World!')
    
    def greet(self):
        return str(self.h) + str(self.w)

if __name__ == "__main__":
    hello_world = HelloWorld()
    print(hello_world.greet())
