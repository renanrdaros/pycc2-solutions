# Exercise 5-8. Hello Admin

users = ["admin", "john", "andrew", "carolina", "david"]

for user in users:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")
