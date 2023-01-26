# Exercise 3-5. Changing Guest List

guests = ["Bill", "Tyler", "Liz", "Leslie", "Riley", "Kenneth", "Erin", "Ever"]

for guest in guests:
    print(f"{guest}, you're invited for our dinner party tomorrow.")

# :( Leslie can't make it to dinner tomorrow
guest_to_remove = "Leslie"
guest_to_add = "Anne"

print(f"\n{guest_to_remove} can't make it to dinner. Let's remove her from the list and include {guest_to_add} instead.\n")

guests.remove(guest_to_remove)
guests.append(guest_to_add)

for guest in guests:
    print(f"{guest}, you're invited for our dinner party tomorrow.")
