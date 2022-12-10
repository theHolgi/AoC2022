
busy = False
cycle = 0
sumstrength = 0
x = 1

def check():
   global x
   global cycle
   if x-1 <= cycle%40 <= x+1:
      print('🎁', end="")
   else:
      print('🌲', end="")
   cycle += 1
   if cycle == 40:
      cycle = 0
      print("")

with open("10.txt") as f:
   for line in f.readlines():
      line = line.replace("\n", "")
      if line == "noop":
         check()
      else:
         check()
         check()
         x = x + int(line[5:])

