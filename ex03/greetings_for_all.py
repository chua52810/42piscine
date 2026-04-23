#!/usr/bin/env python3

class greetings:
    def __init__(self, name):
        self.name = name

    def greets(self):
        if self.name == "":
            return f"Hello, noble stranger."

        elif any(char.isdigit() for char in self.name):
            return f"Error! It was not a name."
            
        else:
            return f"Hello, {self.name}."

sub1 = greetings("Alexandra")
print(sub1.greets())

sub2 = greetings("Wil")
print(sub2.greets())

sub3 = greetings("")
print(sub3.greets())

sub4 = greetings("42")
print(sub4.greets())
