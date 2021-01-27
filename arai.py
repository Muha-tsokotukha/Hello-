aviacompanies = ["AirAstana", "FlyArystan", "SCAT"]
print(len(aviacompanies))
print(aviacompanies[1])
for x in aviacompanies:
    print(x)

newcomp = input()
aviacompanies.append(newcomp)
print("________")
for x in aviacompanies:
    print(x)

aviacompanies.pop(1)
print("-----------")
print(aviacompanies[1])

