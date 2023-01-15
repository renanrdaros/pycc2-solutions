# Exercise 7-5. Movie Tickets

while True:
    age = input("\nEnter your age (or 'quit'): ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

    print(f"The cost of your movie ticket is ${cost}")

