resultat = 0
reste = 200
for a in range(0, reste+1, 200):
    reste = 200 - a
    for b in range(0, reste+1, 100):
        reste = 200 - a - b
        for c in range(0, reste+1, 50):
            reste = 200 - a - b - c
            for d in range(0, reste+1, 20):
                reste = 200 - a - b - c - d
                for e in range(0, reste+1, 10):
                    reste = 200 - a - b - c - d - e
                    for f in range(0, reste+1, 5):
                        reste = 200 - a - b - c - d - e - f
                        for g in range(0, reste+1, 2):
                            h = 200 - a - b - c - d - e - f - g
                            if h >= 0:
                                resultat += 1
print(resultat)