aliens = {
    "formics": {"color": "reddish-brow", "points": 500},
    "harvesters": {"color": "grayish-blue", "points": 100},
    "invaders": {"color": "white", "points": 30},
    "overlords": {"color": "red", "points": 0},  # please don't kill the good guys
    "heptapods": {"color": "grey", "points": 0},
}

for k, v in aliens.items():
    print(f"{k.title()}: {v}")
