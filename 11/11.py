import logging
from typing import List, Callable

Monkeys = []

class Monkey:
   def __init__(self, id: int, initial_stock: List[int], worry_function: Callable[[int], int], throwing_function: Callable[[int], int]):
      self.id = id
      self.stock = initial_stock
      self.worry_function = worry_function
      self.throwing_function = throwing_function
      self.activity = 0

   def throw(self) -> None:
      while len(self.stock) > 0:
         self.activity += 1
         item = self.stock.pop(0)
         logging.debug(f"{self.id} inspects {item} ")
         item = self.worry_function(item) // 3
         target = get_Monkey(self.throwing_function(item))
         logging.debug(f" ... becomes {item}, throw to {target.id}")
         target.get(item)

   def get(self, item: int) -> None:
      self.stock.append(item)

   def __repr__(self) -> str:
      return f"🐒 {self.id}: 💥 {self.activity} {self.stock}"


def get_Monkey(i) -> Monkey:
   global Monkeys
   return next (monkey for monkey in Monkeys if monkey.id == i)


def create_example_Monkeys() -> List[Monkey]:
   return [Monkey(0, [79,98], lambda i: i*19, lambda i: 2 if i%23==0 else 3),
           Monkey(1, [54,65,75,74], lambda i: i + 6, lambda i: 2 if i % 19 == 0 else 0),
           Monkey(2, [79, 60, 97], lambda i: i * i, lambda i: 1 if i % 13 == 0 else 3),
           Monkey(3, [74], lambda i: i + 3, lambda i: 0 if i % 17 == 0 else 1)
           ]

def create_puzzle_Monkeys() -> List[Monkey]:
   return [Monkey(0, [74, 64, 74, 63, 53], lambda i: i*7, lambda i: 1 if i%5==0 else 6),
           Monkey(1, [69,99,95,62], lambda i: i * i, lambda i: 2 if i % 17 == 0 else 5),
           Monkey(2, [59, 81], lambda i: i + 8, lambda i: 4 if i % 7 == 0 else 3),
           Monkey(3, [50, 67, 63, 57, 63, 83, 97], lambda i: i + 4, lambda i: 0 if i % 13 == 0 else 7),
           Monkey(4, [61, 94, 85, 52, 81, 90, 94, 70], lambda i: i + 3, lambda i: 7 if i % 19 == 0 else 3),
           Monkey(5, [69], lambda i: i + 5, lambda i: 4 if i % 3 == 0 else 2),
           Monkey(6, [54, 55, 58], lambda i: i + 7, lambda i: 1 if i % 11 == 0 else 5),
           Monkey(7, [79, 51, 83, 88, 93, 76], lambda i: i * 3, lambda i: 0 if i % 2 == 0 else 6)
           ]
logging.basicConfig(level=logging.DEBUG)
Monkeys.extend(create_puzzle_Monkeys())

for round in range(20):
   for monkey in Monkeys:
      monkey.throw()
   logging.info(f"End of round {round+1}: {Monkeys}")

actives = sorted(Monkeys, key=lambda m: m.activity, reverse=True)

print(f"Most active: {actives[0]},{actives[1]} = {actives[0].activity * actives[1].activity}")