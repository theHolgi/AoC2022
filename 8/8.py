trees = []
with open("8.txt") as f:
   for i, line in enumerate(f.readlines()):
      trees.append([int(c) for c in line.replace("\n","")])

visible = 0
max_score = 0
width = len(trees)
for row in range(1,width-1):
   for col in range(1,width-1):
      h = trees[row][col]
      score = 1
      left, right, up, down = 0,0,0,0
      for n in range(col-1, -1, -1): # left
         left += 1
         if trees[row][n] >= h:
            break

      for n in range(col+1, width): # right
         right += 1
         if trees[row][n] >= h:
            break

      for n in range(row-1, -1, -1): # up
         up += 1
         if trees[n][col] >= h:
            break

      for n in range(row+1, width): # down
         down += 1
         if trees[n][col] >= h:
            break
      score = left*right*up*down
      if score > max_score:
         max_score = score

print(f"Visible: {visible} Score: {max_score}")

