from collections import deque

food = int(input())

orders = deque([int(el) for el in input().split()])
print(max(orders))

while len(orders)>0:
    if food >= orders[0]:
        food-=orders.popleft()
    else:
        break

if len(orders)==0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(el) for el in orders])}")



