# Exercise 6-11 Cities

cities = {
    "Rio de Janeiro": {
        "country": "Brazil",
        "population": 6_750_000,
        "fact": "Rio’s carnival party is the biggest carnival in the world.",
    },

    "Kyoto": {
        "country": "Japan",
        "population": 1_470_000,
        "fact": "It was the capital of Japan for over 1,000 years.",
    },

    "San Francisco": {
        "country": "USA",
        "population": 815_000,
        "fact": "The chinese fortune cookie was invented in San Francisco.",
    },
}

for city, info in cities.items():
    print(f"\n{city}:")
    for k, v in info.items():
        print(f"- {k}: {v}")
