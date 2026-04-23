#!/usr/bin/env python3

def average(user_dict):
    ave = sum(user_dict.values()) / len(user_dict)
    return (ave)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
    }

class_3C = {
    "quetin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
    }

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
print()
