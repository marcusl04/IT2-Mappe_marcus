assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting

try: 
    assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmelding
except:
    print("Hei på deg!")



print("koden er ferdig")

