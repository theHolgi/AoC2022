from json import JSONDecoder


class Signal:
   def __init__(self, value):
      self.v = value
   def __lt__(self, other):
      return self.compare(other) == 1

   def __gt__(self, other):
      return self.compare(other) == -1

   def __repr__(self) -> str:
      return str(self.v) + "\n"

   def compare(self,other) -> int:
      if type(self.v)==int and type(other.v) == int:
         if self.v < other.v:
            return 1
         elif self.v > other.v:
            return -1
         else:
            return 0
      elif type(self.v) == int:  # and r is list
         return Signal([self.v]).compare(other)
      elif type(other.v) == int:  # and l is list
         return self.compare(Signal([other.v]))
      else:  # both is list
         if len(self.v) == 0 and len(other.v) == 0:
            return 0
         elif len(self.v) == 0:  # and r is not
            return 1
         elif len(other.v) == 0:  # and l is not
            return -1
         else:
            res = Signal(self.v[0]).compare(Signal(other.v[0]))
            if res!=0:
               return res
            else:
               return Signal(self.v[1:]).compare(Signal(other.v[1:]))

with open("13.txt") as f:
   lines = f.readlines()
   lines = list(map(lambda v: Signal(JSONDecoder().decode(v)), filter(lambda s: s != "\n", lines)))

beacons = [Signal([[2]]), Signal([[6]])]

sorted_lines = sorted(lines + beacons)

p1 = sorted_lines.index(beacons[0])+1
p2 = sorted_lines.index(beacons[1])+1

print(f"{sorted_lines}; {p1}, {p2} = {p1*p2}")
