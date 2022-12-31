alien = {"color": "green", "points": 5, "x_pos": 10, "y_pos": 23}

value = alien.get("z_pos", "Error - This is a two-dimensional alien.")
print(f"z_pos: {value}")
