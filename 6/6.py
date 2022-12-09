import re
with open("6.txt") as f:
   for line in f.readlines():

      for i in range(14,len(line)):
         chars = set( line[i-14:i].__iter__())
         if len(chars) == 14:
            print (f"Start at index {i}")
            break
