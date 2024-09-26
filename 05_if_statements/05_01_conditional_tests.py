chapter = "Black Templar"

print("Is the chapter == 'Ultramarine'? I predict False.")
print(chapter == "Ultramarine")

print("Is the chapter == 'Black Templar'? I predict True.")
print(chapter == "Black Templar")

print("Is the chapter == 'black templar'? I predict False.")
print(chapter == "black templar")

print("Is the chapter == 'black templar'? I predict True.")
print(chapter.lower() == "black templar")

print("Is the chapter == 'BLACK TEMPLAR'? I predict True.")
print(chapter.upper() == "BLACK TEMPLAR")

chapter = "BLACK TEMPLAR"

print("Is the chapter == 'Black Templar'? I predict True.")
print(chapter.title() == "Black Templar")

print("Is the chapter == 'black templar'? I predict False.")
print(chapter == "black templar")

chapter = int(7)

print("Is the chapter == 7? I predict True.")
print(chapter == 7)

print("Is the chapter <= 5? I predict False.")
print(chapter <= 5)

chapter = ["Space Wolves", "Blood Angels", "Black Templars"]

print("Is the chapter[1] == 'Black Templars'? I predict False.")
print(chapter[1] == 'Black Templars')