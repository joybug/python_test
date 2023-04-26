pet = {
    "animal": "Iguana",
    "name": "Iggy",
    "food": "Veggies",
    "mealsPerDay": 1
}
print(len(pet))

pet["mealsPerDay"] = 2

print(pet["name"], "eats", pet["mealsPerDay"], "meals")

pets = [
    {
        "animal": "Iguana",
        "name": "Iggy",
        "food": "Veggies",
        "mealsPerDay": 1
    },
    {
        "animal": "Goldfish",
        "name": "Goldy",
        "food": "Flakes",
        "mealsPerDay": 3
    }
]


for pet in pets:
    print(pet["animal"],"-",pet["name"])



#딕셔너리 메서드 사용
pet.update({"mealsPerDay":5,"name":"gody"})

print("pet.keys() :",pet.keys())   
print("pet.values() :",pet.values())   


print("copy pet to pet2")

pet2 = pet.copy()

pet.clear()

print("clare pet:",pet)
print("pet2:",pet2)





