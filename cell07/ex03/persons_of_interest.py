#!/usr/bin/python3

def famous_births(fame_arg):
    sorted_fame = sorted(fame_arg.items(), key=lambda fame: fame[1]["date_of_birth"])

    for fame in sorted_fame:
        print(f"{fame[1]["name"]} is a great scientist born in {fame[1]["date_of_birth"]}")


women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}

famous_births(women_scientists)
