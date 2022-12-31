favorite_languages = {
    "guido": "python",
    "dennis": "c",
    "bjarn": "c++",
    "graydon": "rust",
    "roberto": "lua",
}

print("Here are some awesome programming languages:")
for lang in favorite_languages.values():
    print(f"- {lang.title()}")
