import re


class Grid:
   def __init__(self):
      self.g = {}
      self.min_x = 10000
      self.min_y = 10000
      self.max_x = 0
      self.max_y = 0

   def draw(self, x0,y0,x1,y1):
      if x0 == x1:
         if y0<y1:
            for y in range(y0,y1+1):
               self.put(x0,y)
         else:
            for y in range(y0, y1-1, -1):
               self.put(x0, y)
      elif y0 == y1:
         if x0<x1:
            for x in range(x0,x1+1):
               self.put(x,y0)
         else:
            for x in range(x0,x1-1, -1):
               self.put(x,y0)

   def put(self, x,y, what: str = '#'):
      self.min_x = min(self.min_x, x)
      self.max_x = max(self.max_x, x)
      self.min_y = min(self.min_y, y)
      self.max_y = max(self.max_y, y)
      if x in self.g:
         self.g[x][y] = what
      else:
         self.g[x] = {y: what}

   def empty(self, x,y) -> bool:
      return self.g.get(x, {}).get(y, '.') == '.'

   def __repr__(self) -> str:
      r = ""
      for y in range(self.min_y, self.max_y+1):
         r += "".join(self.g.get(x, {}).get(y, '.') for x in range(self.min_x, self.max_x+1)) + "\n"
      return r

class Sand:
   def __init__(self):
      self.x = 500
      self.y = 0

   def fall(self, grid: Grid) -> bool:
      if grid.empty(self.x, self.y+1):
         self.y += 1
      elif grid.empty(self.x-1, self.y+1):
         self.x -= 1
         self.y += 1
      elif grid.empty(self.x+1, self.y+1):
         self.x += 1
         self.y += 1
      else:
         return False
      return True

   def left(self, g: Grid) -> bool:
      return self.y >= g.max_y

grid = Grid()
with open('14.txt') as f:
   for line in f.readlines():
      x0, y0 = None, None
      for m in re.finditer(r'(\d+),(\d+)', line):
         x1,y1 = map(int, m.groups())
         if x0 is not None:
            grid.draw(x0,y0, x1,y1)
         x0, y0 = x1,y1

grid.draw(grid.min_x-200, grid.max_y+2, grid.max_x+200, grid.max_y+2)
sand = Sand()
grains = 1
done = False
while not done:
   while sand.fall(grid):
      assert not sand.left(grid)
   grid.put(sand.x, sand.y, 'o')
   sand = Sand()
   if not grid.empty(sand.x, sand.y):
      break
   grains += 1

# grains -= 2  # One about to fall off, one new already created
print(f"{grid} with {grains} grains")
