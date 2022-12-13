from typing import List

infinite = 1000000
field = []

class Knoten:
   def __init__(self, hoehe: int, x: int, y: int):
      self.weight = infinite
      self.vorgaenger = None
      self.hoehe = hoehe
      self.abstand = 0
      self.x = x
      self.y = y

   def reachable(self, other: "Knoten") -> bool:
      return self.hoehe+1 >= other.hoehe

   def nachbarn(self) -> List["Knoten"]:
      nachbarn = []
      if self.x > 0:
         nachbarn.append(field[self.y][self.x-1])
      if self.x < max_x:
         nachbarn.append(field[self.y][self.x+1])
      if self.y > 0:
         nachbarn.append(field[self.y-1][self.x])
      if self.y < max_y:
         nachbarn.append(field[self.y+1][self.x])
      return filter(self.reachable, nachbarn)

   def update(self, other: "Knoten") -> bool:
      if self.weight > other.weight:
         self.weight = other.weight+1
         self.vorgaenger = other
         return True
      else:
         return False

   def __repr__(self) -> str:
      w = '∞' if self.weight == infinite else str(str(self.weight))
      return f"[{self.x},{self.y}] ({self.hoehe} {w})"


class Unvisited(list):
   def pop_lowest(self):
      c = self[0]
      for i in self:
         if i.weight < c.weight:
            c = i
      self.remove(c)
      return c

max_x = None
unvisited = Unvisited()

with open("12.txt") as f:
   for y, line in enumerate(f.readlines()):
      l = []
      line = line.replace("\n", "")
      if max_x is None:
         max_x = len(line)
      else:
         assert max_x == len(line)
      for x,c in enumerate(line):
         if c == 'S':
            hoehe = 1
         elif c == 'E':
            hoehe = 26
         else:
            hoehe = 1+ord(c)-ord('a')
         f = Knoten(hoehe, x, y)
         l.append(f)
         unvisited.append(f)
         if c == 'S':
            start = f
         elif c == 'E':
            ziel = f
      field.append(l)

max_x = x
max_y = y

def reinitialize(start: Knoten):
   global field
   global Unvisited
   unvisited.clear()
   for x in field:
      for y in x:
         y.weight = infinite
         unvisited.append(y)

   start.weight = 0

def run():
   while ziel in unvisited:
      cur = unvisited.pop_lowest()
      for neighbor in cur.nachbarn():
         neighbor.update(cur)

possible_starts = [y for x in field for y in x if y.hoehe == 1]

shortest = 10000
for start in possible_starts:
   reinitialize(start)
   run()
   print (f"{start} has length {ziel.weight}")
   if ziel.weight < shortest:
      shortest = ziel.weight

print (f"Shortest: {shortest}")
