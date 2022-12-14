from json import JSONDecoder

with open("13.txt") as f:
   lines = f.readlines()

def compare(l,r) -> int:
   if type(l)==int and type(r) == int:
      if l < r:
         return 1
      elif l > r:
         return -1
      else:
         return 0
   elif type(l) == int:  # and r is list
      return compare([l], r)
   elif type(r) == int:  # and l is list
      return compare(l, [r])
   else:  # both is list
      if len(l) == 0 and len(r) == 0:
         return 0
      elif len(l) == 0:  # and r is not
         return 1
      elif len(r) == 0:  # and l is not
         return -1
      else:
         res = compare(l[0], r[0])
         if res!=0:
            return res
         else:
            return compare(l[1:], r[1:])

index = 0
sum = 0
while len(lines)>0:
   index+=1
   l = JSONDecoder().decode(s=lines.pop(0))
   r = JSONDecoder().decode(s=lines.pop(0))
   if len(lines)>0:
      lines.pop(0)

   res = compare(l,r)
   print(f"#{index}: {l} and {r} is {res}")
   if res == 1:
      sum += index

print(f"Sum is {sum}")