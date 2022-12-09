from dataclasses import dataclass, field
import re

@dataclass
class Directory:
   parent: "Directory"
   name: str = ""
   size: int = 0
   children: dict = field(default_factory=dict)
   def __repr__(self):
      return f"[{self.name}]: {self.size}"

@dataclass
class File:
   size: int = 0
   name: str = ""
   def __repr__(self):
      return f"[{self.name}]: {self.size}"

root = Directory(name="/", parent=None)
cur_dir = root

path = ['/']
with open("7.txt") as f:
   for line in f.readlines():
      line = line.replace("\n","")
      if line == '$ cd ..':
         cur_dir = cur_dir.parent
         path.pop(-1)
      elif line == '$ cd /':
         cur_dir = root
      elif line == '$ ls':
         pass
      elif m := re.match(r'dir (\S+)', line):
         name = m.group(1)
         assert(name not in cur_dir.children)
         d = Directory(name=name, parent=cur_dir)
         cur_dir.children[name] = d
      elif m := re.match(r'\$ cd (\w+)', line):
         name = m.group(1)
         d = cur_dir.children[name]
         path.append(name)
         cur_dir = d
      elif m := re.match(r'(\d+)\s+(\S+)', line):
         size, name = m.groups()
         size = int(size)
         f = File(name=name, size=size)
         parent = cur_dir
         while parent is not None:
            parent.size += size
            parent = parent.parent
         cur_dir.children[name] = f
      else:
         assert(False)

pass

sum_size = 0
def traverse(d: Directory):
   global sum_size
   if d.size <= 100000:
      print(f"Directory {d.name} has size {d.size}")
      sum_size += d.size
   for child in d.children.values():
      if isinstance(child, Directory):
         traverse(child)

traverse(root)
print(sum_size)

available = 70000000-root.size
print("Free space: " + str(available))
threshold = 30000000-available
print("Threshold: " + str(threshold))
candidate = root

def search(d: Directory):
   global candidate
   if (d.size < candidate.size) and (d.size >= threshold):
      print(f"New candidate: {d.name} has {d.size}")
      candidate = d
   for child in d.children.values():
      if isinstance(child, Directory):
         search(child)

search(root)