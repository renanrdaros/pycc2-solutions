# Exercise 5-10. Checking Usernames

current_users = ["admin", "John", "andrew", "carolina", "DAVID"]
current_users_lower = [user.lower() for user in current_users]

new_users = ["Admin", "mary", "Jane", "Peter", "David"]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"'{user}' has already been used. Please enter a new username!")
    else:
        print(f"The username '{user}' is available.")
