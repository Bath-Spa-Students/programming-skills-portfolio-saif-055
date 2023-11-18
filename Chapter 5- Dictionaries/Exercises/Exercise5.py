pet1 = {'kind': 'dog', 'owner': 'Alice'}
pet2 = {'kind': 'cat', 'owner': 'Bob'}
pet3 = {'kind': 'parrot', 'owner': 'Charlie'}
pet4 = {'kind': 'fish', 'owner': 'David'}


pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"{owner}'s pet is a {kind}.")


for pet in pets:
    print(f"\nPet Information:")
    for key, value in pet.items():
        print(f"{key.capitalize()}: {value}")
    print("------------------")
