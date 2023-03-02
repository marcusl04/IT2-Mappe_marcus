# Vern mot kjøretidsfeil og logiske feil i problemer

## Kjøretidsfeil

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og except.
Python forsøker å kjøre kodeblokken som ligger under 'try:', hvis python får en feilmelding vil den kjøre kodeblokken som ligger under 'except:'.

````python
try:
    alder = int(input("Fødselsår: "))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: alder må være et heltall")

print("koden fortsetter")
````

### Eksperttips: While-løkke med try-except

````python
while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
````