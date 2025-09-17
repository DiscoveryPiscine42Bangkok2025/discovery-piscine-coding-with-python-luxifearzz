#!/usr/bin/python3

def find_the_redheads(family_members):
    redheads = filter(
        lambda name: family_members[name] == "red", family_members)
    return list(redheads)


dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "frank": "red"
}

print(find_the_redheads(dupont_family))
