#!/usr/bin/env python3

class Hello:
    def __init__(self, name):
        self.name = name
    
    def intro(self):
        return f"Hello, {self.name}!"

hello = Hello("Everyone")
print(Hello.intro())
