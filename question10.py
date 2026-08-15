# Playlist Slicing and Rearrangement

songs = [
    "Song A",
    "Song B",
    "Song C",
    "Song D",
    "Song E",
    "Song F",
    "Song G",
    "Song H"
]

print(f"Complete Playlist: {songs}")
print(f"First 3 songs: {songs[:3]}")
print(f"Last 3 songs: {songs[-3:]}")
print(f"Songs from Position 3 to 6: {songs[3:7]}")
print(f"Every Alternate Song: {songs[::2]}")
print(f"Playlist in Reverse Order: {songs[::-1]}")
print(f"Playlist Without First and Last Song: {songs[1:-1]}")

short_playlist = songs[2:6]
for i in range(len(short_playlist)):
    if short_playlist[i] == "Song E":
        short_playlist[i] = "Song M"

print(f"Original Playlist: {songs}")
print(f"Shortened Playlist: {short_playlist}")