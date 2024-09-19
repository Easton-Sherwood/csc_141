astartes = ["Bladeguard", "Intercessors", "Centurions"]
print (f"The {astartes[0]} have made it to the battle.")
print (f"The {astartes[1]} have made it to the battle.")
print (f"The {astartes[2]} have made it to the battle.\n")

print("They need reinforements\n")

astartes.insert(0, "High Marshall")
astartes.insert(2, "Terminators")
astartes.append("Hellblasters")

print (f"The {astartes[0]} has joined the battle to reinforce.")
print (f"The {astartes[2]} have joined the battle to reinforce.")
print (f"The {astartes[5]} have joined the battle to reinforce.\n")

pop1 = astartes.pop(5)

print (f"The {pop1} ship was shot down on its way!\n")


print (f"Here is my original list \n {astartes}\n")
print (f"Here is my sorted list \n {sorted(astartes)}\n")
astartes.reverse()
print (f"Here is my reversed list \n {astartes}\n")
astartes.reverse()
astartes.sort()
print (f"Here is my sorted list \n {sorted(astartes)}\n")
astartes.sort(reverse=True)
print (f"Here is my reverse sorted list \n {astartes}\n")

del astartes[1]
del astartes[3]

print(f"Here is what remains of the squad after the battle \n {astartes}")

