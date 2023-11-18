rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country)
