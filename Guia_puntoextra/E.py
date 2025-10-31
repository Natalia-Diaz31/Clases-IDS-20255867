N = int(input())  # cantidad de combos
Pa, Pb, Pc = map(int, input().split())  # daños de A, B y C

for i in range(N):
    combo = input().strip()
    daño = combo.count('A') * Pa + combo.count('B') * Pb + combo.count('C') * Pc
    print(daño)