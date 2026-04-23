#!/usr/bin/env python3

def array_of_names(name_dict):
    new_array=[]

    for key, value in name_dict.items():
       full_name = f"{key.capitalize()} {value.capitalize()}" 
       new_array.append(full_name)
    return new_array
       
name_dict = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
    }

new_list = array_of_names(name_dict)
print(new_list)
print()
