#!/usr/bin/env python3

def find_the_redheads(user_dict):
    filtered_red = {k: v for k, v in user_dict.items() if v == "red"}
#    print(filtered_red)
    return (filtered_red)
       
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
    }

red_only = find_the_redheads(dupont_family)
print(list(red_only))
print()
