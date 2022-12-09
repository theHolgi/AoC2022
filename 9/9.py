from dataclasses import dataclass


@dataclass
class Pos:
   x: int = 0
   y: int = 0

   def step(self, direction: str)-> None:
      if direction == 'L':
         self.x -= 1
      elif direction == 'R':
         self.x += 1
      elif direction == 'U':
         self.y -= 1
      elif direction == 'D':
         self.y += 1

   def follow(self, other: "Pos") -> None:
      dist_x, dist_y = abs(self.x-other.x), abs(self.y-other.y)
      if dist_x <= 1 and dist_y <= 1:
         return
      elif dist_x == 0 and dist_y >= 1:
         if self.y<other.y: self.y += 1
         else: self.y -= 1
      elif dist_y == 0 and dist_x >= 1:
         if self.x<other.x: self.x += 1
         else: self.x -= 1
      else:  # diagonal
         if self.x<other.x: self.x += 1
         else: self.x -= 1
         if self.y<other.y: self.y += 1
         else: self.y -= 1

   def __hash__(self) -> int:
      return hash(f"{self.x}, {self.y}")

visited = set()

knots = [Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos(), Pos()]
head = knots[0]
tail = knots[-1]

with open("9.txt") as f:
   for line in f.readlines():
      d, steps = line.split(" ")
      for n in range(int(steps)):
         head.step(d)
         for i in range(1, len(knots)):
            knots[i].follow(knots[i-1])
         if tail not in visited:
            visited.add(tail)

print(f"{visited} has {len(visited)} elements")
