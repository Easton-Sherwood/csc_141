#I reworked 6_10 to output a cleaner sentence, meaning it didn't include the [] and ''
favorite_num = {
 "Easton": {
 "first": "0",
 "second": "1",
 "third": "99",
 },
 "Jack": {
 "first": "12",
 "second": "34",
 "third": "67",
 },
  "Sean": {
 "first": "19",
 "second": "55",
 "third": "88",
 },
  "Jimmy": {
 "first": "37",
 "second": "22",
 "third": "6",
 },
  "Billy": {
 "first": "8",
 "second": "43",
 "third": "95",
 },
 }

for name, num in favorite_num.items():
    print(f"{name.title()}'s favorite numbers are {num['first']}, {num['second']}, and {num['third']}.")