# precticing dict in dict & in list

ratings2 = [
    {"name": "Ela", "ratings": (1, 2, 3), "behaviour": 6},
    {"name": "Andrzej", "ratings": (4, 5, 6), "behaviour": 1}
    ]
#to jest słownik w liście

for person in ratings2:
    for key in person:
        print(key, person[key])
    print()

print(ratings2[1])

#-----------------------------------------------------------------------

people1= {
    "person1": {"name": "Anna", "age": 20, "sex": "female"},
    "person2": {"name": "Adam", "age": 30, "sex": "male"},
    "person3": {"name": "Ola", "age": 40, "sex": "female"}
    }
print()
#to jest słownik w słowniku

for person in people1:   #name to person1, person2, person3
    info = people1[person] #info to {"name": "Anna", "age": 20, "sex": "female"}
    name = info["name"] # to jest wartosc dla klucza 'name'
    age  = info["age"] # to jest wartosc dla klucza wieku
    sex  = info["sex"] # to jest warotosc dla klucza płci
    print("Name:", name + ", " "Age:", str(age) +", " "Sex:", sex)
    
