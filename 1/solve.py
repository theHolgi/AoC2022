
with open("input.txt") as f:
   lines = map(lambda l: l.replace("\n",""), f.readlines())

class Elve:
   has: int = 0
   id: int
   def __gt__(self, other):
      return self.has > other.has

cur_id = 1
max = Elve()

current = Elve()
current.id = 1

elves = []

for line in lines:
   if line == "":
      cur_id += 1
      if current.has > max.has:
         max = current

      elves.append(current)
      current = Elve()
      current.id = cur_id
   else:
      current.has += int(line)

elves.append(current)

top = sorted(elves, reverse=True)

print(f"Elve {max.id} has {max.has}")

print ("Top is " + str(top[0].has + top[1].has + top[2].has))