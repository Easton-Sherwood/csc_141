chapter = "Black Templar"

print("Is the chapter == 'Ultramarine'? I predict False.")
print(chapter == "Ultramarine")

print("Is the chapter == 'Black Templar'? I predict True.")
print(chapter == "Black Templar")

print("Is the chapter == 'black templar'? I predict False.")
print(chapter == "black templar")

print("Is the chapter == 'black templar'? I predict True.")
print(chapter.lower() == "black templar")

chapter = int(7)

print("Is the chapter == 7? I predict True.")
print(chapter == 7)

print("Is the chapter == 8? I predict False.")
print(chapter == 8)

print("Is the chapter > 7? I predict False.")
print(chapter > 7)

print("Is the chapter >= 5? I predict True.")
print(chapter >= 5)

print("Is the chapter <= 5? I predict False.")
print(chapter <= 5)

print("Is the chapter < 5? I predict False.")
print(chapter < 5)

founding = 2
chapter = ["Space Wolves", "Blood Angels", "Black Templars"]

print("Is the chapter[1] == 'Black Templars'? I predict False.")
print(chapter[1] == 'Black Templars')

print(founding == 2 and chapter[2] == "Black Templars")

print ('Space Wolves' in chapter)

print ('Dark Angels' in chapter)