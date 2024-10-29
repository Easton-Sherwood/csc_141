def make_album(artist, album):
     person = {'Artist': artist, 'Album': album}
     return person
while True:
     thelist = []
     artist = input("What is the name of the artist (input q to quit): ")
     if artist.lower() == "q":
          break
     album = input("What is the name of the album (input q to quit): ")
     if album.lower() == "q":
          break

     thelist.append(make_album(artist, album))
     print(thelist)