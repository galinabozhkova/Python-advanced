from collections import deque

quantity = int(input())
customers = deque()
command = input()

while command!="Start":
    customers.append(command)
    command = input()

command = input()
while command != "End":
    if command.startswith("refill"):
        quantity+=int(command.split(' ')[1])
    else:
        liters = int(command)
        if liters <=quantity:
            print(f"{customers.popleft()} got water")
            quantity-=liters
        else:
            print(f"{customers.popleft()} must wait")
    command = input()

print(f"{quantity} liters left")