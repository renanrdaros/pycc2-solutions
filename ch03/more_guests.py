# Exercise 3-6. More Guests

guests = ["Bill", "Tyler", "Liz", "Leslie", "Riley", "Anne"]

for guest in guests:
    print(f"{guest}, you're invited for our dinner party tomorrow.")

print("\nI just found a bigger dinner table, so I'll invite three more guests.\n")

guests.insert(0, "Kenneth")
guests.insert(3, "Erin")
guests.append("Ever")

for guest in guests:
    print(f"{guest}, you're invited for our dinner party tomorrow.")

