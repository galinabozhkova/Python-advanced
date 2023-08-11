from collections import deque

name = input()
customers = deque()

while name != "End":
    if name =="Paid":
        while len(customers)>0:
            print(customers.popleft())
    else:
        customers.append(name)

    name = input()

print(f"{len(customers)} people remaining.")