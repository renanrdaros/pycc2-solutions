# Exercise 6-5. Rivers

rivers = {"nile": "egypt", "amazon": "brazil", "yangtze": "china"}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nKeys:")
for river in rivers:    # could use rivers.keys() instead
    print(f"- {river}")

print("\nValues:")
for country in rivers.values():
    print(f"- {country}")
