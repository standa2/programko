import json

films = {
    "comedy":"Big Bang",
    "horor": ["Smile","IT"],
    "animated": ["Spongebob", "Powerpuffgirls", "Kungfu Panda"],
    "musical":"Hamilton"
    }

with open("data.json", mode="w") as file:
    json.dump(films, file, indent=4)

with open("data.json", mode="r") as file:
    data = json.load(file)

print(data)