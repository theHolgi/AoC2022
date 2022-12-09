with open("3.txt") as f:
   lines = list(map(lambda l: l.replace("\n",""), f.readlines()))

elves = []
s=0

for start in range(0,len(lines), 3):
   a,b,c = lines[start:start+3]
   shared = [i for i in a if i in b and i in c][0]

   print (shared)

   score = ord(shared) - ord('a')+1 if 'a'<=shared<='z' else ord(shared)-ord('A')+27
   print (score)
   s+=score

print(s)
