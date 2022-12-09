import re
phase=1
stack = {}
with open("5.txt") as f:
   for line in f.readlines():
      if phase==1:
         i = 0
         while len(line)>3:
            i += 1
            b = line[1]
            line = line[4:]
            if b.isdecimal():
               phase=2
            elif b != ' ':
               if i in stack:
                  stack[i].append(b)
               else:
                  stack[i] = [b]
      elif phase == 2:
         m = re.match(r'move (\d+) from (\d+) to (\d+)', line)
         if m:
            n,f,t = int(m.group(1)),int(m.group(2)),int(m.group(3))
            before = len(stack[t])
            for i in range(n):
               x = stack[f].pop(0)
               stack[t].insert(i, x)
            assert(len(stack[t]) == before + n)
pass
for i in range(1,10,1):
   print(stack[i][0])

