#!/usr/bin/env python3

def famous_births(user_dict):
    sorted_birth = dict(sorted(women_scientists.items(), key=lambda item: item[1]["date_of_birth"]))
    return (sorted_birth)

def output_woman(user_dict):
    for key, value in user_dict.items():
       woman = value["name"]
       year = value["date_of_birth"]
       print(f"{woman} is a great scientist born in {year}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

sorted_birth = famous_births(women_scientists)
output_woman(sorted_birth)
