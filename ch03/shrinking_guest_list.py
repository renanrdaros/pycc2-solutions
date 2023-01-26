
# Exercise 3-7. Shrinking Guest List

guests = ["Bill", "Tyler", "Liz", "Leslie", "Riley", "Anne"]

for guest in guests:
    print(f"{guest}, you're invited for our dinner party tomorrow.")

print("\nI just found a bigger dinner table, so I'll invite three more guests.\n")

guests.insert(0, "Kenneth")
guests.insert(3, "Erin")
guests.append("Ever")

for guest in guests:
    print(f"{guest}, you're invited for our dinner party tomorrow.")

print(f"\nI changed my mind. I'll invite just two people for dinner.\n")

# keep just 2 guests in the list
while len(guests) > 2:
    popped_guest = guests.pop()
    print(f"I'm sorry, {popped_guest}. I can't invite you this time.")

for guest in guests:
    print(f"Hi, {guest}. You're are still invited.")

# while guests list is not empty, delete a guest
while guests:
    del guests[0]

print(guests)
