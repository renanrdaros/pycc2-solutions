# Exercise 6-10. Favorite Numbers 2

favorite_numbers = {
        "Guido": [5, 11, 23],
        "Dennis": [13, 34, 40, 53],
        "Bjarn": [25, 30, 50, 80, 100],
        "Graydon": [1, 2, 3, 4, 5],
        "Roberto": [100, 200, 500],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}: {numbers}")
