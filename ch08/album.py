# Exercise 8-7. Album

def make_album(artist_name, album_title, number_of_songs=None):
    """Build a dictionary describing a music album."""
    album = {"artist": artist_name, "album": album_title} 
    if number_of_songs:
        album["number_of_songs"] = number_of_songs
    return album

print(make_album("Ozzy Osbourne", "No More Tears"))
print(make_album("Black Sabbath", "Heaven and Hell"))
print(make_album("Angra", "Angels Cry"))
print(make_album("Helloween", "Master of the Rings", 11))
