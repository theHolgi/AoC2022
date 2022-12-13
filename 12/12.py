from typing import List

infinite = 1000000
field = []
max_x = 9
max_y = 9


class Knoten:
   def __init__(self, hoehe: int, x: int, y: int):
      self.weight = infinite
      self.vorgaenger = None
      self.hoehe = hoehe
      self.abstand = 0
      self.x = x
      self.y = y

   def reachable(self, other: "Knoten") -> bool:
      return self.hoehe <= other.hoehe+1

   def nachbarn(self) -> List["Knoten"]:
      nachbarn = []
      if self.x > 0:
         nachbarn.append(field[self.x-1][self.y])
      if self.x < max_x:
         nachbarn.append(field[self.x+1][self.y])
      if self.y > 0:
         nachbarn.append(field[self.x][self.y-1])
      if self.y < max_y:
         nachbarn.append(field[self.x][self.y+1])
      return filter(self.reachable, nachbarn)

   def update(self, other: "Knoten") -> bool:
      if self.weight > other.weight:
         self.weight = other.weight+1
         self.vorgaenger = other
         return True
      else:
         return False

   def __repr__(self) -> str:
      return f"[{self.x},{self.y}] ({self.weight})"


class Unvisited(list):
   def pop_lowest(self):
      c = self[0]
      for i in self:
         if i.weight < c.weight:
            c = i
      self.remove(c)
      return c


unvisited = Unvisited()

for x in range(max_x+1):
   hoehe = 1
   field.append([])
   for y in range(max_y+1):
      field[x].append(Knoten(hoehe, x, y))
      unvisited.append(field[x][y])

start = field[0][0]
start.weight = 0
ziel = field[max_x][max_y]

while ziel in unvisited:
   cur = unvisited.pop_lowest()
   for neighbor in cur.nachbarn():
      neighbor.update(cur)

cur = ziel
print(f"{cur}")
while True:
   print(f" <- {cur}")
   cur = cur.vorgaenger
   if cur is None:
      break
