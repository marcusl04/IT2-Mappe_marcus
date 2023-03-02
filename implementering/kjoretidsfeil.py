try:
    alder = int(input("Fødselsår: "))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: alder må være et heltall")

print("koden fortsetter")


while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")