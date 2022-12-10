
busy = False
cycle = 0
sumstrength = 0
x = 1
def check():
   global cycle
   global sumstrength
   cycle += 1
   if (cycle-20) % 40 == 0:
      strength = cycle*x
      sumstrength += strength
      print(f"x ist {x} strength {strength} sum {sumstrength}")

with open("10.txt") as f:
   for line in f.readlines():
      line = line.replace("\n", "")
      if line == "noop":
         check()
      else:
         check()
         check()
         x = x + int(line[5:])

