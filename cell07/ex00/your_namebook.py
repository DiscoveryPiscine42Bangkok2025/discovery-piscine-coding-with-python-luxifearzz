#!/usr/bin/python3

def array_of_names(names):
    full_names = [f"{fname.capitalize()} {names[fname].capitalize()}" for fname in names]
    return full_names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
