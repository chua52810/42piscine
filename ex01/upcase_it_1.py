#!/usr/bin/env python3

class Upcase:
    def to_upper(str_word):
        return str_word.upper()

str_word = input("Give me a word: ")
print(Upcase.to_upper(str_word))
