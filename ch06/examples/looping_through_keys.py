favorite_languages = {
    "guido": "python",
    "dennis": "c",
    "bjarn": "c++",
    "graydon": "rust",
    "roberto": "lua",
}

print("Looping through the keys in dict.keys()")
for name in favorite_languages.keys():
    print(f"- {name.title()}")

print("\nLooping through the keys in dict also works")
for name in favorite_languages:
    print(f"- {name.title()}")

print("\nRemember that we can get the values using the keys")
for name in favorite_languages:
    print(f"- {name}: {favorite_languages[name]}")
