cities = {
 "Las Vegas": {
 "Country": "USA",
 "Population": "665,640",
 "Fact": "gambling capital of america",
 },
 "Rome": {
 "Country": "Italy",
 "Population": "2,873,000",
 "Fact": "home of the colosseum",
 },
 "Matamata": {
 "Country": "New Zealand",
 "Population": "9,130",
 "Fact": "home of the village of Hobbiton from the Lord Of The Rings movies",
 }, 
 }

for city, info in cities.items():
    print (f"{city} is located in {info['Country']}, with a population of {info['Population']}, it is known for being the {info['Fact']}.\n")