with open("2.txt") as f:
   lines = map(lambda l: l.replace("\n",""), f.readlines())

score = {'A':   {'Y': 1, 'Z': 2, 'X': 3},
         'B': {'Y': 2, 'Z': 3, 'X': 1},
         'C': {'Y': 3, 'Z': 1, 'X': 2}

         }
win = {'A': 'Y', 'B': 'Z', 'C': 'X'}
eq = {'A': 'X', 'B': 'Y', 'C': 'Z'}

total = 0
for line in lines:
   a,b = line.split(" ")

   won = b == 'Z'
   draw = b == 'Y'
   s = score[a][b] + (6 if won else (3 if draw else 0))
   total += s

   print(f"score: {s}")
print(f"total: {total}")

