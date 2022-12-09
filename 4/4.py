import re
with open("4.txt") as f:
   lines = list(map(lambda l: l.replace("\n",""), f.readlines()))

overlap=0
for line in lines:
   m = re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line)
   a = [int(m.group(1)), int(m.group(2))]
   b = [int(m.group(3)), int(m.group(4))]

   if b[0]<=a[0]<=b[1] or b[0]<=a[1]<=b[1]\
        or (a[0] <= b[0] and a[1]>= b[1]) or (b[0] <= a[0] and b[1]>= a[1]) :
      overlap += 1

print(overlap)